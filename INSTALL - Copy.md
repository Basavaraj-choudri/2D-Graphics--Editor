# 2D Graphics Editor - Installation & Build Guide

## Quick Start

### Windows (PowerShell/Command Prompt)
```bash
cd c:\Users\Akshay bk\c.project
build.bat
graphics_editor.exe
```

### Linux/Mac (Terminal)
```bash
cd ~/c.project
chmod +x build.sh
./build.sh
./graphics_editor
```

---

## Prerequisites

### Windows

**MinGW-w64 GCC Compiler** (Recommended)

#### Option 1: Automated Installation (Admin Required)
```powershell
# Using Windows Package Manager
winget install -e --id BrechtSanders.WinLibs.MinGW
```

#### Option 2: Manual Installation (Recommended)

1. **Download MinGW-w64 Online Installer:**
   - Go to: https://www.mingw-w64.org/downloads/
   - Click "Online installer"
   - Save the `.exe` file

2. **Run the Installer:**
   - Double-click the downloaded file
   - Select settings:
     - **Architecture:** x86_64
     - **Version:** Latest (14.1.0 or newer)
     - **Threads:** posix
     - **Exception handling:** seh
   - **Installation path:** `C:\MinGW64`
   - Click "Next" and complete installation

3. **Add to System PATH:**
   - Press `Win + X`
   - Select "System"
   - Click "Advanced system settings"
   - Click "Environment Variables"
   - Under "User variables" or "System variables", select "Path"
   - Click "Edit"
   - Click "New"
   - Add: `C:\MinGW64\bin`
   - Click OK three times
   - **Restart PowerShell/Command Prompt**

4. **Verify Installation:**
   ```powershell
   gcc --version
   ```
   Should display GCC version information

#### Option 3: Visual Studio C++ Tools
If you have Visual Studio installed:
1. Run Visual Studio Installer
2. Click "Modify"
3. Select "Desktop development with C++"
4. Complete installation
5. Use `build.bat` (will auto-detect MSVC)

---

### Linux

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install build-essential
```

**Fedora/RHEL:**
```bash
sudo dnf groupinstall "Development Tools"
```

**Arch Linux:**
```bash
sudo pacman -S base-devel
```

---

### macOS

**Option 1: Using Homebrew:**
```bash
brew install gcc
```

**Option 2: Xcode Command Line Tools:**
```bash
xcode-select --install
```

---

## Building the Project

### Windows

**Using Batch File (Automatic):**
```cmd
cd C:\Users\Akshay bk\c.project
build.bat
```

**Manual Compilation with GCC:**
```cmd
gcc -Wall -std=c99 -o graphics_editor graphics.c main.c -lm
```

**Manual Compilation with MSVC:**
```cmd
cl graphics.c main.c /o graphics_editor.exe
```

### Linux/Mac

**Using Shell Script:**
```bash
cd ~/c.project
chmod +x build.sh
./build.sh
```

**Manual Compilation:**
```bash
gcc -Wall -std=c99 -o graphics_editor graphics.c main.c -lm
```

---

## Running the Program

### Windows
```cmd
graphics_editor.exe
```

### Linux/Mac
```bash
./graphics_editor
```

---

## Build Files Explained

### `build.bat` (Windows)
- Detects available C compiler (GCC or MSVC)
- Compiles with appropriate flags
- Creates `graphics_editor.exe`
- Handles error messages

### `build.sh` (Linux/Mac)
- Detects GCC or Clang compiler
- Compiles with standard C99 flags
- Creates `graphics_editor` executable
- Provides installation guidance if no compiler found

### `Makefile` (Alternative)
```bash
make              # Compile
make run          # Compile and run
make clean        # Remove compiled files
```

---

## Project Structure

```
c.project/
├── graphics.h              # Header file with declarations
├── graphics.c              # Core drawing algorithms
├── main.c                  # Menu-driven interface
├── example.c               # Example usage program
├── graphics_ncurses.c      # Optional ncurses support
├── build.bat               # Windows build script
├── build.sh                # Linux/Mac build script
├── compile.bat             # Alternative Windows build
├── Makefile                # GNU Make build file
├── Makefile.ncurses        # Make with ncurses support
├── README.md               # General README
├── USAGE.md                # Detailed usage guide
└── INSTALL.md              # This file
```

---

## Compilation Flags Explained

### `-Wall`
Enables all compiler warnings. Helps catch potential bugs.

### `-std=c99`
Uses C99 standard (widely compatible, includes modern C features)

### `-o graphics_editor`
Output filename for the executable

### `-lm`
Links against the math library (needed for circle drawing with math.h)

---

## Troubleshooting

### "gcc: command not found"

**Windows:**
- MinGW not installed or not in PATH
- Solution: Install MinGW-w64 and add to PATH
- Verify: Open new PowerShell and run `gcc --version`

**Linux/Mac:**
- Build tools not installed
- **Ubuntu:** `sudo apt install build-essential`
- **Mac:** `brew install gcc` or `xcode-select --install`

### Compilation errors with graphics.c

Most common: Math library not linked
- **Error:** "undefined reference to `sin`" or `cos`
- **Solution:** Ensure `-lm` flag is used

### PATH issues on Windows

After installing MinGW:
1. Close ALL PowerShell/Command Prompt windows
2. Open a NEW PowerShell window
3. Run: `gcc --version`
4. If not found, add to PATH manually (see Instructions above)

### Can't execute on Linux/Mac

```bash
# Make script executable
chmod +x graphics_editor

# Then run
./graphics_editor
```

---

## Advanced Build Options

### Debug Build (with debugging symbols)
```bash
gcc -g -Wall -std=c99 -o graphics_editor graphics.c main.c -lm
```

### Optimized Build (faster execution)
```bash
gcc -O2 -Wall -std=c99 -o graphics_editor graphics.c main.c -lm
```

### With All Warnings
```bash
gcc -Wall -Wextra -Wpedantic -std=c99 -o graphics_editor graphics.c main.c -lm
```

### 32-bit Build (if needed)
```bash
gcc -m32 -Wall -std=c99 -o graphics_editor graphics.c main.c -lm
```

---

## Building Example Program

Compile the example demonstrating all features:

**Windows:**
```cmd
gcc -Wall -std=c99 -o example example.c graphics.c -lm
example.exe
```

**Linux/Mac:**
```bash
gcc -Wall -std=c99 -o example example.c graphics.c -lm
./example
```

---

## Verification Checklist

After building:

- [ ] Compilation completed without errors
- [ ] Executable file created (`graphics_editor.exe` or `graphics_editor`)
- [ ] Program starts when executed
- [ ] Main menu displays
- [ ] Can draw shapes
- [ ] Shapes are visible on canvas
- [ ] Can add/modify/delete shapes
- [ ] Program closes cleanly

---

## Next Steps

1. **Build the project** using `build.bat` (Windows) or `build.sh` (Linux/Mac)
2. **Run the program** to test functionality
3. **Read USAGE.md** for detailed program usage
4. **Explore the code** in graphics.c and main.c

---

## Quick Reference Commands

| Task | Windows | Linux/Mac |
|------|---------|----------|
| Build | `build.bat` | `./build.sh` |
| Build (manual) | `gcc -Wall -std=c99 -o graphics_editor graphics.c main.c -lm` | Same |
| Run | `graphics_editor.exe` | `./graphics_editor` |
| Clean | `del *.o graphics_editor.exe` | `rm *.o graphics_editor` |
| Build example | `gcc -Wall -std=c99 -o example example.c graphics.c -lm` | Same |

---

## Support

For issues:
1. Check troubleshooting section above
2. Verify compiler is installed: `gcc --version`
3. Check that source files are in the same directory
4. Ensure correct compilation command (with `-lm` for math library)

---

## Additional Resources

- **C Programming:**
  - https://www.cprogramming.com/
  - https://en.cppreference.com/w/c

- **GCC Documentation:**
  - https://gcc.gnu.org/

- **Algorithm References:**
  - Bresenham's Line Algorithm
  - Midpoint Circle Algorithm

---

That's all! Your 2D Graphics Editor in pure C is ready to build and use! 🚀
