[CmdletBinding()]
param(
    [switch]$Smoke,
    [ValidateRange(10, 240)]
    [int]$BuildTimeoutMinutes = 90
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$readerDir = [IO.Path]::GetFullPath($PSScriptRoot)
$projectDir = [IO.Path]::GetFullPath((Split-Path -Parent $readerDir))
$sourceDir = Join-Path $projectDir 'source'
$masterName = 'Al-jabr-2-id-complete-draft'
$masterPath = Join-Path $sourceDir ($masterName + '.tex')
$configPath = Join-Path $readerDir 'reader.cfg'
$driverPath = Join-Path $readerDir 'reader-driver.tex'
$buildFile = Join-Path $readerDir 'reader.mk4'
$cssPath = Join-Path $readerDir 'reader.css'
$accessibilityPath = Join-Path $readerDir 'accessibility.html'
$licensePath = Join-Path $readerDir 'LICENSE.txt'
$mathJaxPath = Join-Path $readerDir 'vendor\mathjax-3.2.2'
$toolsDir = Join-Path $readerDir 'tools'
$buildDir = Join-Path $readerDir 'build'
$distDir = Join-Path $readerDir 'dist'
$texConfigPath = $configPath.Replace('\', '/')
$texDriverPath = $driverPath.Replace('\', '/')
$make4htBuildFile = $buildFile.Replace('\', '/')
$make4htBuildDir = $buildDir.Replace('\', '/')
$make4htDistDir = $distDir.Replace('\', '/')

foreach ($required in @(
    $masterPath, $configPath, $driverPath, $buildFile, $cssPath,
    $accessibilityPath, $licensePath,
    (Join-Path $mathJaxPath 'tex-chtml-full.js'),
    (Join-Path $mathJaxPath 'LICENSE-MathJax.txt'),
    (Join-Path $toolsDir 'postprocess_reader.py'),
    (Join-Path $toolsDir 'validate_reader.py')
)) {
    if (-not (Test-Path -LiteralPath $required -PathType Leaf)) {
        throw "Berkas wajib tidak ditemukan: $required"
    }
}

$readerPrefix = $readerDir.TrimEnd([IO.Path]::DirectorySeparatorChar) +
    [IO.Path]::DirectorySeparatorChar
foreach ($target in @($buildDir, $distDir)) {
    $fullTarget = [IO.Path]::GetFullPath($target)
    if (-not $fullTarget.StartsWith($readerPrefix, [StringComparison]::OrdinalIgnoreCase)) {
        throw "Target build berada di luar reader: $fullTarget"
    }
    if (Test-Path -LiteralPath $fullTarget) {
        Remove-Item -LiteralPath $fullTarget -Recurse -Force
    }
    New-Item -ItemType Directory -Path $fullTarget | Out-Null
}

# Jangkar unit dibuat dari daftar \input aktif pada master, bukan dari daftar
# yang dipelihara terpisah. Dengan demikian semua 146 unit dan dua bridge
# selalu mengikuti urutan sumber yang sedang dibangun.
$masterText = Get-Content -LiteralPath $masterPath -Raw -Encoding UTF8
$unitPattern = '\\input\{((?:prelude-unit-\d{3}|chapter\d+-unit-\d{3}|appendix\d+-unit-\d{3}|mastery-bridge-[^}]+))\}'
$unitMatches = [regex]::Matches($masterText, $unitPattern)
if ($unitMatches.Count -ne 148) {
    throw "Master memuat $($unitMatches.Count) unit/bridge; 148 diharapkan."
}
$hookLines = [Collections.Generic.List[string]]::new()
$hookLines.Add('% Dibuat otomatis oleh build-reader.ps1; jangan sunting.')
foreach ($match in $unitMatches) {
    $stem = $match.Groups[1].Value
    $filename = $stem + '.tex'
    $anchor = 'unit-' + ($stem -replace '[^A-Za-z0-9_-]', '-')
    $hookLines.Add("\AddToHook{file/$filename/before}{\HCode{<section id=`"$anchor`" class=`"reader-unit`" data-unit-file=`"$filename`" role=`"doc-chapter`">\Hnewline}}")
    $hookLines.Add("\AddToHook{file/$filename/after}{\HCode{</section>\Hnewline}}")
}
$hookPath = Join-Path $buildDir 'reader-unit-hooks.tex'
[IO.File]::WriteAllLines($hookPath, $hookLines, [Text.UTF8Encoding]::new($false))

$make4ht = Get-Command make4ht -ErrorAction Stop
$savedEnvironment = @{}
$environmentNames = @('LANG', 'LC_ALL', 'TZ', 'SOURCE_DATE_EPOCH', 'PATH')
foreach ($name in $environmentNames) {
    $savedEnvironment[$name] = [Environment]::GetEnvironmentVariable($name, 'Process')
}

try {
    $env:LANG = 'C.UTF-8'
    $env:LC_ALL = 'C.UTF-8'
    $env:TZ = 'UTC'
    $env:SOURCE_DATE_EPOCH = '1704067200'
    $env:PATH = $toolsDir + [IO.Path]::PathSeparator + $env:PATH

    $arguments = @(
        '-a', 'status',
        '-x',
        '-s',
        '-f', 'html5',
        '-c', $texConfigPath,
        '-B', $make4htBuildDir,
        '-d', $make4htDistDir,
        '-j', 'index'
    )

    if ($Smoke) {
        $arguments += @('-m', 'draft')
    }
    else {
        $arguments += @('-e', $make4htBuildFile)
    }
    $arguments += @(
        $texDriverPath,
        '',
        '',
        '',
        '-interaction=nonstopmode -halt-on-error -file-line-error'
    )

    $processInfo = [Diagnostics.ProcessStartInfo]::new()
    $processInfo.FileName = $make4ht.Source
    $processInfo.WorkingDirectory = $sourceDir
    $processInfo.UseShellExecute = $false
    $processInfo.RedirectStandardOutput = $true
    $processInfo.RedirectStandardError = $true
    # ProcessStartInfo.ArgumentList tidak tersedia pada semua host PowerShell
    # yang dipakai instalasi ini. Tidak ada argumen yang memuat tanda petik;
    # mengutip setiap argumen juga mempertahankan empat argumen kosong TeX4ht.
    $quotedArguments = foreach ($argument in $arguments) {
        '"' + $argument.Replace('"', '\"') + '"'
    }
    $processInfo.Arguments = $quotedArguments -join ' '
    $process = [Diagnostics.Process]::new()
    $process.StartInfo = $processInfo
    $null = $process.Start()
    $stdoutTask = $process.StandardOutput.ReadToEndAsync()
    $stderrTask = $process.StandardError.ReadToEndAsync()
    $timeoutMs = $BuildTimeoutMinutes * 60 * 1000
    if (-not $process.WaitForExit($timeoutMs)) {
        try { $process.Kill($true) } catch { $process.Kill() }
        throw "make4ht melewati batas $BuildTimeoutMinutes menit dan dihentikan."
    }
    $process.WaitForExit()
    $make4htExit = $process.ExitCode
    $stdout = $stdoutTask.GetAwaiter().GetResult()
    $stderr = $stderrTask.GetAwaiter().GetResult()
    [IO.File]::WriteAllText(
        (Join-Path $buildDir 'make4ht.stdout.log'), $stdout,
        [Text.UTF8Encoding]::new($false))
    [IO.File]::WriteAllText(
        (Join-Path $buildDir 'make4ht.stderr.log'), $stderr,
        [Text.UTF8Encoding]::new($false))

    if ($make4htExit -ne 0) {
        throw "make4ht gagal dengan kode keluar $make4htExit"
    }

    Copy-Item -LiteralPath $cssPath -Destination (Join-Path $distDir 'reader.css')
    Copy-Item -LiteralPath $accessibilityPath -Destination (Join-Path $distDir 'accessibility.html')
    Copy-Item -LiteralPath $licensePath -Destination (Join-Path $distDir 'LICENSE.txt')
    Copy-Item -LiteralPath $mathJaxPath -Destination (Join-Path $distDir 'vendor\mathjax-3.2.2') -Recurse

    $entryPoint = Join-Path $distDir 'index.html'
    if (-not (Test-Path -LiteralPath $entryPoint -PathType Leaf)) {
        throw "Titik masuk HTML tidak dibuat: $entryPoint"
    }

    $python = (Get-Command python -ErrorAction Stop).Source
    $ledgerPath = Join-Path $projectDir 'backend\figure-alt-text-id.csv'
    & $python (Join-Path $toolsDir 'postprocess_reader.py') `
        --html $entryPoint --master $masterPath --ledger $ledgerPath `
        --report (Join-Path $buildDir 'figure-alt-application.json')
    if ($LASTEXITCODE -ne 0) {
        throw "Postproses pembaca gagal dengan kode $LASTEXITCODE"
    }
    & $python (Join-Path $toolsDir 'validate_reader.py') `
        --dist $distDir --master $masterPath --ledger $ledgerPath
    if ($LASTEXITCODE -ne 0) {
        throw "Validasi pembaca gagal dengan kode $LASTEXITCODE"
    }

    $modeName = if ($Smoke) { 'smoke' } else { 'produksi' }
    Write-Host "Build pembaca $modeName selesai: $entryPoint"
}
finally {
    foreach ($name in $environmentNames) {
        [Environment]::SetEnvironmentVariable(
            $name,
            $savedEnvironment[$name],
            'Process'
        )
    }
}

