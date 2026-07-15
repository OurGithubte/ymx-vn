@echo off
setlocal enabledelayedexpansion
set PORT=8080
title YMX Website - LAN Server

echo ================================================
echo   YMX VIETNAM - WEBSITE LAN SERVER
echo ================================================
echo.

for /f "tokens=2 delims=:" %%a in ('ipconfig ^| findstr /i "IPv4"') do (
    set LOCALIP=%%a
    goto :gotip
)
:gotip
set LOCALIP=!LOCALIP: =!

echo May nay (localhost) xem tai:
echo    http://localhost:%PORT%/
echo.
echo Cac may khac trong cung mang LAN xem tai:
echo    http://!LOCALIP!:%PORT%/
echo.
echo (Neu may khac khong vao duoc, kiem tra lai Windows Firewall
echo  hoac hoi bo phan IT mo port %PORT% cho ket noi noi bo)
echo.
echo Nhan Ctrl+C de dung server nay.
echo ================================================
echo.

cd /d "%~dp0"

where python >nul 2>nul
if %errorlevel%==0 (
    python -m http.server %PORT%
) else (
    where py >nul 2>nul
    if %errorlevel%==0 (
        py -m http.server %PORT%
    ) else (
        echo [LOI] Khong tim thay Python tren may nay.
        echo Vui long cai Python tai https://www.python.org/downloads/
        echo khi cai nho tick chon "Add Python to PATH".
        pause
    )
)
