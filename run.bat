@echo off
setlocal enabledelayedexpansion

REM Store the original CSV files in a temporary list
REM Ignore generated files
set "fileList="

for %%f in (*.csv) do (
    REM Extract the filename without extension
    set "basename=%%~nf"

    REM Skip files that match output patterns (out_*.csv, out_*.csv_ignored, out_*.csv_ambiguous)
    echo %%f | findstr /R "^out_.*_ambiguous$ ^out_.*_ignored$ ^out_.*$" >nul
    if errorlevel 1 (
        REM Only add files that do not match the output patterns
        set "fileList=!fileList! %%f"
    )
)

REM Run the script only if CSV files exist
if defined fileList (
    for %%f in (!fileList!) do (
        echo Processing "%%f"
        python3.9.exe .\bank_csv_converter.py "%%f"
    )
) else (
    echo No CSV files found.
)
