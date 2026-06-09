@echo off
REM Compilation script for 2D Graphics Editor
echo Compiling 2D Graphics Editor...

REM Using Microsoft Visual C++ Compiler (cl.exe) which is available with MSVC
REM Or using gcc if available

REM Check if gcc is available
where gcc >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    echo Using GCC compiler...
    gcc -o graphics_editor graphics.c main.c -lm
    if %ERRORLEVEL% EQU 0 (
        echo Compilation successful!
        echo Running Graphics Editor...
        graphics_editor.exe
    ) else (
        echo Compilation failed!
    )
) else (
    REM Try using cl.exe (MSVC)
    where cl >nul 2>nul
    if %ERRORLEVEL% EQU 0 (
        echo Using MSVC compiler...
        cl graphics.c main.c /o graphics_editor.exe
        if %ERRORLEVEL% EQU 0 (
            echo Compilation successful!
            echo Running Graphics Editor...
            graphics_editor.exe
        ) else (
            echo Compilation failed!
        )
    ) else (
        echo Neither GCC nor MSVC found. Please install a C compiler.
        exit /b 1
    )
)
