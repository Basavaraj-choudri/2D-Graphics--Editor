#!/bin/bash
# ============================================================================
# 2D Graphics Editor - Linux/Mac Build Script
# Compiles C source files and creates executable
# ============================================================================

echo ""
echo "============================================================================"
echo "  2D Graphics Editor - Compilation Script (Linux/Mac)"
echo "============================================================================"
echo ""

# Check if source files exist
if [ ! -f "graphics.c" ]; then
    echo "ERROR: graphics.c not found!"
    exit 1
fi
if [ ! -f "graphics.h" ]; then
    echo "ERROR: graphics.h not found!"
    exit 1
fi
if [ ! -f "main.c" ]; then
    echo "ERROR: main.c not found!"
    exit 1
fi

echo "[*] Checking for C compiler..."
echo ""

# Check for GCC
if command -v gcc &> /dev/null; then
    echo "[+] Found GCC compiler: $(gcc --version | head -n 1)"
    echo ""
    echo "[*] Compiling with GCC..."
    
    gcc -Wall -std=c99 -o graphics_editor graphics.c main.c -lm
    
    if [ $? -eq 0 ]; then
        echo "[+] Compilation successful!"
        echo ""
        echo "[*] Created: ./graphics_editor"
        echo ""
        echo "============================================================================"
        echo "  Ready to run! Execute:"
        echo "    ./graphics_editor"
        echo "============================================================================"
        echo ""
        exit 0
    else
        echo "[-] GCC compilation failed!"
        exit 1
    fi
fi

# Check for Clang
if command -v clang &> /dev/null; then
    echo "[+] Found Clang compiler: $(clang --version | head -n 1)"
    echo ""
    echo "[*] Compiling with Clang..."
    
    clang -Wall -std=c99 -o graphics_editor graphics.c main.c -lm
    
    if [ $? -eq 0 ]; then
        echo "[+] Compilation successful!"
        echo ""
        echo "[*] Created: ./graphics_editor"
        echo ""
        echo "============================================================================"
        echo "  Ready to run! Execute:"
        echo "    ./graphics_editor"
        echo "============================================================================"
        echo ""
        exit 0
    else
        echo "[-] Clang compilation failed!"
        exit 1
    fi
fi

# No compiler found
echo ""
echo "============================================================================"
echo "  ERROR: No C compiler found!"
echo "============================================================================"
echo ""
echo "Install a C compiler:"
echo ""
echo "  Ubuntu/Debian:"
echo "    sudo apt update && sudo apt install build-essential"
echo ""
echo "  Fedora/RHEL:"
echo "    sudo dnf groupinstall 'Development Tools'"
echo ""
echo "  macOS:"
echo "    brew install gcc"
echo "    or install Xcode Command Line Tools: xcode-select --install"
echo ""
exit 1
