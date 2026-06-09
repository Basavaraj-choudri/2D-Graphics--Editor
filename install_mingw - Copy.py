#!/usr/bin/env python3
"""
Automated MinGW Installation Script for Windows
This script downloads and installs MinGW-w64 GCC compiler
"""

import os
import sys
import urllib.request
import zipfile
import shutil
import subprocess
from pathlib import Path

def print_status(msg):
    print(f"\n{'='*60}")
    print(f"  {msg}")
    print(f"{'='*60}\n")

def download_file(url, destination):
    """Download a file with progress indication"""
    print(f"Downloading from: {url}")
    print(f"Saving to: {destination}")
    
    try:
        urllib.request.urlretrieve(url, destination)
        print("✓ Download complete!")
        return True
    except Exception as e:
        print(f"✗ Download failed: {e}")
        return False

def extract_zip(zip_file, extract_to):
    """Extract zip file"""
    print(f"Extracting to: {extract_to}")
    try:
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        print("✓ Extraction complete!")
        return True
    except Exception as e:
        print(f"✗ Extraction failed: {e}")
        return False

def add_to_path(gcc_bin_path):
    """Add GCC to system PATH"""
    print(f"Adding {gcc_bin_path} to PATH...")
    try:
        # Read current PATH
        result = subprocess.run(
            'echo %PATH%',
            shell=True,
            capture_output=True,
            text=True
        )
        current_path = result.stdout.strip()
        
        # Check if already in PATH
        if gcc_bin_path.lower() in current_path.lower():
            print("✓ Already in PATH")
            return True
        
        # Set new PATH using setx (persistent)
        new_path = f"{gcc_bin_path};{current_path}"
        subprocess.run(
            f'setx PATH "{new_path}"',
            shell=True,
            capture_output=True
        )
        print("✓ Added to PATH (restart terminal to take effect)")
        return True
    except Exception as e:
        print(f"✗ Failed to add to PATH: {e}")
        return False

def verify_gcc():
    """Verify GCC installation"""
    print("Verifying GCC installation...")
    try:
        result = subprocess.run(
            'gcc --version',
            shell=True,
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print("✓ GCC verified!")
            print(result.stdout.split('\n')[0])
            return True
        else:
            print("✗ GCC not found in current PATH")
            return False
    except Exception as e:
        print(f"✗ Verification failed: {e}")
        return False

def compile_project(project_dir):
    """Compile the graphics editor project"""
    print(f"Compiling project in: {project_dir}")
    try:
        os.chdir(project_dir)
        result = subprocess.run(
            'gcc -o graphics_editor graphics.c main.c -lm',
            shell=True,
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            print("✓ Compilation successful!")
            return True
        else:
            print(f"✗ Compilation failed:")
            print(result.stderr)
            return False
    except Exception as e:
        print(f"✗ Error during compilation: {e}")
        return False

def run_program(exe_path):
    """Run the compiled program"""
    print(f"Running: {exe_path}")
    try:
        subprocess.Popen(exe_path)
        print("✓ Program started!")
        return True
    except Exception as e:
        print(f"✗ Failed to run: {e}")
        return False

def main():
    print_status("MinGW-w64 Automated Installer for Windows")
    
    # Setup paths
    home_dir = Path.home()
    install_dir = home_dir / "AppData" / "Local" / "MinGW64"
    gcc_bin_path = install_dir / "bin"
    temp_dir = Path(os.getenv('TEMP'))
    zip_file = temp_dir / "mingw.zip"
    project_dir = Path(__file__).parent
    
    print(f"Installation directory: {install_dir}")
    print(f"Project directory: {project_dir}")
    
    # Check if already installed
    if (install_dir / "bin" / "gcc.exe").exists():
        print("\n✓ MinGW appears to be already installed!")
        if verify_gcc():
            print_status("MinGW Installation Verified")
            # Try to compile
            if compile_project(project_dir):
                print_status("Ready to Run!")
                exe_path = project_dir / "graphics_editor.exe"
                if exe_path.exists():
                    run_program(str(exe_path))
            return
    
    # Step 1: Download
    print_status("Step 1: Downloading MinGW-w64")
    
    # Try multiple mirror sources
    download_urls = [
        "https://github.com/brechtsanders/winlibs_mingw/releases/download/16.1.0-14.0.0-r1/winlibs-x86_64-posix-seh-gcc-14.1.0-mingw-w64-11.0.0-r1.zip",
        "https://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win64/Personal%20Builds/mingw-builds/8.1/threads-posix/seh/x86_64-8.1.0-release-posix-seh-rt_v6-rev0.7z",
    ]
    
    download_success = False
    for url in download_urls:
        if download_file(url, str(zip_file)):
            download_success = True
            break
    
    if not download_success:
        print("\n✗ All download attempts failed.")
        print("Please download manually from: https://www.mingw-w64.org/downloads/")
        sys.exit(1)
    
    # Step 2: Extract
    print_status("Step 2: Extracting Files")
    
    # Create installation directory
    install_dir.mkdir(parents=True, exist_ok=True)
    
    # For zip files
    if zip_file.suffix == '.zip':
        if not extract_zip(str(zip_file), str(install_dir.parent)):
            print("✗ Extraction failed!")
            sys.exit(1)
    
    # Step 3: Add to PATH
    print_status("Step 3: Adding to System PATH")
    add_to_path(str(gcc_bin_path))
    
    # Step 4: Verify
    print_status("Step 4: Verifying Installation")
    if verify_gcc():
        print("✓ Installation successful!")
    else:
        print("⚠ GCC not found. Please restart your terminal and run this script again.")
        print("Or add this to PATH manually: " + str(gcc_bin_path))
    
    # Step 5: Compile
    print_status("Step 5: Compiling Graphics Editor")
    if compile_project(project_dir):
        exe_path = project_dir / "graphics_editor.exe"
        print("\n✓ Compilation successful!")
        print(f"Executable: {exe_path}")
        
        # Ask to run
        print_status("Ready to Run!")
        response = input("Do you want to run the program now? (y/n): ").strip().lower()
        if response == 'y':
            run_program(str(exe_path))
    else:
        print("✗ Compilation failed!")
        sys.exit(1)
    
    # Cleanup
    if zip_file.exists():
        os.remove(zip_file)
    
    print_status("Installation Complete!")
    print("You can now run: graphics_editor.exe")

if __name__ == "__main__":
    main()
