@echo off
setlocal enabledelayedexpansion

REM Store the original CSV files in a temporary list
set "fileList="
for %%f in (*.csv) do (
    set "fileList=!fileList! %%f"
)

REM Run the script only if CSV files exist
if defined fileList (
    for %%f in (!fileList!) do (
        echo "%%f"
        python3.9.exe .\bank_csv_converter.py "%%f"
    )
) else (
    echo No CSV files found.
)
