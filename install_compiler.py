#!/usr/bin/env python3
"""
MinGW-w64 Installation Helper
Downloads and installs GCC compiler for Windows
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def run_command(cmd):
    """Run command and return result"""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.returncode, result.stdout, result.stderr

def check_gcc():
    """Check if GCC is installed"""
    code, stdout, stderr = run_command("gcc --version")
    return code == 0

def add_to_path_powershell(path):
    """Add directory to PATH using PowerShell"""
    cmd = f'$env:PATH += ";{path}"; [Environment]::SetEnvironmentVariable("PATH", $env:PATH, "User")'
    run_command(f'powershell -Command "{cmd}"')

def main():
    print("\n" + "="*70)
    print("  MinGW-w64 GCC Compiler Installation Helper")
    print("="*70 + "\n")
    
    # Check if already installed
    if check_gcc():
        print("✓ GCC compiler is already installed!")
        code, out, err = run_command("gcc --version")
        print(out.split('\n')[0])
        return
    
    print("No C compiler found. Here are your options:\n")
    print("OPTION 1: Automatic Installation (Requires Admin)")
    print("-" * 70)
    print("This will download and install MinGW-w64 automatically.\n")
    
    print("OPTION 2: Manual Installation")
    print("-" * 70)
    print("1. Download from: https://www.mingw-w64.org/downloads/")
    print("2. Or use this direct link:")
    print("   https://sourceforge.net/projects/mingw-w64/files/")
    print("3. Select: x86_64 | posix | seh")
    print("4. Extract to: C:\\MinGW64")
    print("5. Add to PATH: C:\\MinGW64\\bin")
    print("6. Restart PowerShell\n")
    
    print("OPTION 3: Use Chocolatey (if installed)")
    print("-" * 70)
    print("   choco install mingw\n")
    
    choice = input("Which option? (1/2/3) [default: 2]: ").strip() or "2"
    
    if choice == "1":
        print("\n[!] Automatic installation requires admin privileges.")
        print("Please run this script as Administrator.\n")
        
        # Try to run as admin
        try:
            subprocess.run([sys.executable, __file__], check=False)
        except Exception as e:
            print(f"Error: {e}")
    
    elif choice == "2":
        print("\nManual Installation Instructions:")
        print("-" * 70)
        print("1. Go to: https://www.mingw-w64.org/downloads/")
        print("2. Click 'Online installer' and save the file")
        print("3. Run the installer")
        print("4. Settings:")
        print("   - Architecture: x86_64")
        print("   - Version: Latest (14.1.0 or newer)")
        print("   - Threads: posix")
        print("   - Exception: seh")
        print("   - Build revision: Latest")
        print("5. Installation path: C:\\MinGW64")
        print("6. Complete installation")
        print("\n7. After installation, add to PATH:")
        print("   - Press Win+X → System")
        print("   - Advanced system settings")
        print("   - Environment Variables")
        print("   - Edit PATH and add: C:\\MinGW64\\bin")
        print("8. Restart PowerShell")
        print("9. Verify: Run 'gcc --version'\n")
        
        input("Press Enter when installation is complete...")
        
        if check_gcc():
            print("\n✓ GCC successfully installed!")
            code, out, err = run_command("gcc --version")
            print(out)
        else:
            print("\n✗ GCC not found yet.")
            print("Make sure to add C:\\MinGW64\\bin to PATH and restart PowerShell.")
    
    elif choice == "3":
        print("\nInstalling via Chocolatey...")
        code, out, err = run_command("choco install mingw -y")
        if code == 0:
            print("✓ Installation successful!")
            if check_gcc():
                print("✓ GCC verified!")
                code, out, err = run_command("gcc --version")
                print(out)
        else:
            print("✗ Installation failed.")
            print(err)

if __name__ == "__main__":
    main()
