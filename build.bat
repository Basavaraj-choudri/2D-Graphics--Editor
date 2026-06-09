@echo off
REM ============================================================================
REM  2D Graphics Editor - Windows Build Script
REM  Compiles C source files and creates executable
REM ============================================================================

setlocal enabledelayedexpansion

echo.
echo ============================================================================
echo  2D Graphics Editor - Compilation Script
echo ============================================================================
echo.

REM Check if source files exist
if not exist "graphics.c" (
    echo ERROR: graphics.c not found!
    exit /b 1
)
if not exist "graphics.h" (
    echo ERROR: graphics.h not found!
    exit /b 1
)
if not exist "main.c" (
    echo ERROR: main.c not found!
    exit /b 1
)

echo [*] Checking for C compiler...
echo.

REM Try GCC first
where gcc >nul 2>nul
if !errorlevel! equ 0 (
    echo [+] Found GCC compiler
    echo.
    echo [*] Compiling with GCC...
    gcc -Wall -std=c99 -o graphics_editor graphics.c main.c -lm
    
    if !errorlevel! equ 0 (
        echo [+] Compilation successful!
        echo.
        echo [*] Created: graphics_editor.exe
        echo.
        echo ============================================================================
        echo  Ready to run! Execute:
        echo    graphics_editor.exe
        echo ============================================================================
        echo.
        exit /b 0
    ) else (
        echo [-] GCC compilation failed!
        exit /b 1
    )
)

REM Try MSVC (cl.exe)
where cl >nul 2>nul
if !errorlevel! equ 0 (
    echo [+] Found MSVC compiler
    echo.
    echo [*] Compiling with MSVC...
    cl graphics.c main.c /o graphics_editor.exe
    
    if !errorlevel! equ 0 (
        echo [+] Compilation successful!
        echo.
        echo [*] Created: graphics_editor.exe
        echo.
        echo ============================================================================
        echo  Ready to run! Execute:
        echo    graphics_editor.exe
        echo ============================================================================
        echo.
        exit /b 0
    ) else (
        echo [-] MSVC compilation failed!
        exit /b 1
    )
)

REM Compiler not found
echo.
echo ============================================================================
echo  ERROR: No C compiler found!
echo ============================================================================
echo.
echo Please install MinGW-w64 or Visual Studio C++ tools.
echo.
echo Download MinGW-w64 from:
echo   https://www.mingw-w64.org/downloads/
echo.
echo Instructions:
echo   1. Download the online installer
echo   2. Install with: Architecture=x86_64, Threads=posix, Exception=seh
echo   3. Installation path: C:\MinGW64
echo   4. Add C:\MinGW64\bin to your PATH environment variable
echo   5. Restart PowerShell/Command Prompt
echo   6. Run this script again
echo.
pause
exit /b 1
