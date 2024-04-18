@echo off
setlocal

rem Path to the fonts directory
set "fonts_dir=.\fonts"

rem Loop through each file in the fonts directory
for %%A in ("%fonts_dir%\*.ttf") do (
    rem Check if the file is a TrueType font
    if /I "%%~xA"==".ttf" (
        rem Copy the font file to the Windows Fonts directory
        copy "%%A" "C:\Windows\Fonts"
    )
)

endlocal
