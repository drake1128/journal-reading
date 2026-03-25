@echo off
REM PDF Batch Processing Helper - Wrapper for PowerShell script
REM Usage: process-pdfs [list|all|help]

cd /d "%~dp0"

if "%1"=="" (
    powershell -ExecutionPolicy Bypass -File "%~dp0process-pdfs.ps1"
) else if /i "%1"=="list" (
    powershell -ExecutionPolicy Bypass -File "%~dp0process-pdfs.ps1" -List
) else if /i "%1"=="all" (
    powershell -ExecutionPolicy Bypass -File "%~dp0process-pdfs.ps1" -All
) else if /i "%1"=="help" (
    powershell -ExecutionPolicy Bypass -File "%~dp0process-pdfs.ps1" -Help
) else (
    powershell -ExecutionPolicy Bypass -File "%~dp0process-pdfs.ps1" -Process "%1"
)
