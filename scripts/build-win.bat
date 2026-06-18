@echo off

:: Переходим в корень проекта
cd /d %~dp0
cd ..
echo Project directory: %cd%

:: Архитектура процессора из окружения
for /f "delims=" %%A in ('powershell -NoProfile -Command "$a=$env:PROCESSOR_ARCHITECTURE; if ($a -eq 'x86' -and $env:PROCESSOR_ARCHITEW6432) { $a=$env:PROCESSOR_ARCHITEW6432 }; $a.ToLower()"') do set ARCH=%%A

:: Имя итогового файла
set BIN_NAME=nca-win-%ARCH%

:: Запускаем PyInstaller
python -m PyInstaller ^
    --name %BIN_NAME% ^
    --onefile ^
    --windowed ^
    --noconfirm ^
    --clean ^
    --add-data=icons;icons ^
    --icon=icons/icon.ico ^
    main.py

:: Удаляем build и .spec-файл
rmdir /s /q build
del %BIN_NAME%.spec

echo Build successful
exit /b 0