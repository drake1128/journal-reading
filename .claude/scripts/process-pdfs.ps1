# PDF Batch Processing Helper for Claude Code
# Usage: .\process-pdfs.ps1 [-List] [-Process <filename>] [-All]

param(
    [switch]$List,
    [switch]$All,
    [string]$Process,
    [switch]$Help
)

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

# Get all PDFs in current directory (exclude those already in date folders)
function Get-UnprocessedPDFs {
    $allPDFs = Get-ChildItem -Path . -Filter "*.pdf" -File | Where-Object {
        # Exclude PDFs that end with _original.pdf (already processed source files)
        $_.Name -notmatch '_original\.pdf$' -and
        # Exclude handout PDFs (those with corresponding .tex files)
        -not (Test-Path ($_.BaseName + ".tex"))
    }
    return $allPDFs
}

function Get-AllPDFs {
    return Get-ChildItem -Path . -Filter "*.pdf" -File
}

function Show-Help {
    Write-Host ""
    Write-Host "PDF Batch Processing Helper for Claude Code" -ForegroundColor Cyan
    Write-Host "============================================" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Usage:" -ForegroundColor Yellow
    Write-Host "  .\process-pdfs.ps1 -List          List unprocessed PDFs"
    Write-Host "  .\process-pdfs.ps1 -All           List ALL PDFs in folder"
    Write-Host "  .\process-pdfs.ps1 -Process <file> Show command to process specific PDF"
    Write-Host "  .\process-pdfs.ps1 -Help          Show this help message"
    Write-Host ""
    Write-Host "Workflow:" -ForegroundColor Yellow
    Write-Host "  1. Run with -List to see unprocessed PDFs"
    Write-Host "  2. Copy the suggested Claude Code command"
    Write-Host "  3. Run it in your terminal with Claude Code"
    Write-Host ""
    Write-Host "Examples:" -ForegroundColor Yellow
    Write-Host '  claude "整理 NEJMoa2513032.pdf"'
    Write-Host '  claude "請幫我整理 article.pdf, 產生教學講義"'
    Write-Host ""
}

function Show-UnprocessedPDFs {
    $pdfs = Get-UnprocessedPDFs

    if ($pdfs.Count -eq 0) {
        Write-Host ""
        Write-Host "No unprocessed PDFs found!" -ForegroundColor Green
        Write-Host "All PDFs either have corresponding .tex files or are marked as originals."
        Write-Host ""
        return
    }

    Write-Host ""
    Write-Host "Unprocessed PDFs found: $($pdfs.Count)" -ForegroundColor Cyan
    Write-Host "=================================" -ForegroundColor Cyan
    Write-Host ""

    $index = 1
    foreach ($pdf in $pdfs) {
        $size = [math]::Round($pdf.Length / 1KB, 1)
        Write-Host "[$index] " -NoNewline -ForegroundColor Yellow
        Write-Host "$($pdf.Name)" -NoNewline -ForegroundColor White
        Write-Host " ($size KB)" -ForegroundColor Gray
        $index++
    }

    Write-Host ""
    Write-Host "Commands to process:" -ForegroundColor Green
    Write-Host ""

    foreach ($pdf in $pdfs) {
        Write-Host "claude `"整理 $($pdf.Name)`"" -ForegroundColor Cyan
    }

    Write-Host ""
    Write-Host "Or process all at once:" -ForegroundColor Green
    $allNames = ($pdfs | ForEach-Object { $_.Name }) -join ", "
    Write-Host "claude `"請幫我依序整理這些 PDF: $allNames`"" -ForegroundColor Cyan
    Write-Host ""
}

function Show-AllPDFs {
    $pdfs = Get-AllPDFs
    $unprocessed = Get-UnprocessedPDFs

    Write-Host ""
    Write-Host "All PDFs in folder: $($pdfs.Count)" -ForegroundColor Cyan
    Write-Host "=================================" -ForegroundColor Cyan
    Write-Host ""

    foreach ($pdf in $pdfs) {
        $size = [math]::Round($pdf.Length / 1KB, 1)
        $status = ""

        if ($pdf.Name -match '_original\.pdf$') {
            $status = "[ORIGINAL]"
            $color = "DarkGray"
        }
        elseif (Test-Path ($pdf.BaseName + ".tex")) {
            $status = "[PROCESSED]"
            $color = "Green"
        }
        else {
            $status = "[NEW]"
            $color = "Yellow"
        }

        Write-Host "$status " -NoNewline -ForegroundColor $color
        Write-Host "$($pdf.Name)" -NoNewline -ForegroundColor White
        Write-Host " ($size KB)" -ForegroundColor Gray
    }

    Write-Host ""
    Write-Host "Legend: " -NoNewline
    Write-Host "[NEW]" -NoNewline -ForegroundColor Yellow
    Write-Host " = Needs processing  " -NoNewline
    Write-Host "[PROCESSED]" -NoNewline -ForegroundColor Green
    Write-Host " = Has .tex file  " -NoNewline
    Write-Host "[ORIGINAL]" -ForegroundColor DarkGray
    Write-Host ""
}

function Show-ProcessCommand {
    param([string]$filename)

    if (-not (Test-Path $filename)) {
        Write-Host "Error: File '$filename' not found!" -ForegroundColor Red
        return
    }

    Write-Host ""
    Write-Host "To process '$filename', run:" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "claude `"整理 $filename`"" -ForegroundColor Yellow
    Write-Host ""
}

# Main logic
if ($Help) {
    Show-Help
}
elseif ($All) {
    Show-AllPDFs
}
elseif ($Process) {
    Show-ProcessCommand -filename $Process
}
else {
    # Default: show unprocessed PDFs (same as -List)
    Show-UnprocessedPDFs
}
