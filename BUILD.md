# Build Documentation - 2D Graphics Editor

## Overview

This document explains the build system and compilation process for the 2D Graphics Editor in pure C.

## Project Files

### Source Files
- **graphics.h** - Header file with all function declarations and data structures
- **graphics.c** - Core implementation of drawing algorithms and shape management
- **main.c** - Menu-driven user interface

### Build Files
- **build.bat** - Windows build script (auto-detects GCC or MSVC)
- **build.sh** - Linux/Mac build script (auto-detects GCC or Clang)
- **Makefile** - GNU Make build system for all platforms
- **compile.bat** - Alternative Windows batch compilation

### Documentation Files
- **README.md** - Project overview and features
- **USAGE.md** - Detailed usage guide
- **INSTALL.md** - Installation and setup guide
- **BUILD.md** - This file

### Example Files
- **example.c** - Example program demonstrating all features
- **graphics_ncurses.c** - Optional ncurses terminal UI support
- **install_compiler.py** - Python helper for compiler installation

---

## Compilation Process

### Step 1: Prepare Source Files

All source files should be in the same directory:
```
- graphics.h
- graphics.c
- main.c
```

### Step 2: Choose Compiler

**Recommended: GCC**
- Widely available
- Standard C99 compatible
- Well-tested with this project

**Alternative: MSVC (Windows)**
- Fast compilation
- Good error messages
- Requires Visual Studio

**Alternative: Clang (Linux/Mac)**
- Modern compiler
- Excellent error reporting
- Performance comparable to GCC

### Step 3: Run Build Command

#### Windows (Automatic)
```cmd
cd C:\Users\Akshay bk\c.project
build.bat
```

#### Linux/Mac (Automatic)
```bash
cd ~/c.project
chmod +x build.sh
./build.sh
```

#### Manual Compilation (All Platforms)
```bash
gcc -Wall -std=c99 -o graphics_editor graphics.c main.c -lm
```

### Step 4: Verify Output

**Windows:**
- Check for `graphics_editor.exe`
- Run: `graphics_editor.exe`

**Linux/Mac:**
- Check for `graphics_editor` 
- Run: `./graphics_editor`

---

## Compiler Flags

### `-Wall`
- Enables all standard warnings
- Helps identify potential issues
- Recommended for all builds

### `-std=c99`
- Uses C99 standard (1999 C standard)
- Provides needed C features (variable declarations, inline comments, etc.)
- Widely compatible with C compilers

### `-o graphics_editor`
- Specifies output filename
- Without `-o`, default is `a.out` (Linux/Mac) or `a.exe` (Windows)

### `-lm`
- **IMPORTANT**: Links against math library
- Required for `sin()`, `cos()`, `sqrt()` etc. in graphics.c
- Must be at END of compilation command

### Optional Flags

**Debug Build:**
```bash
gcc -g -Wall -std=c99 -o graphics_editor graphics.c main.c -lm
```
- `-g`: Includes debugging symbols
- Allows debugging with gdb

**Optimized Build:**
```bash
gcc -O2 -Wall -std=c99 -o graphics_editor graphics.c main.c -lm
```
- `-O2`: Optimization level 2 (good speed, reasonable compile time)
- Makes executable faster but larger

**Max Warnings:**
```bash
gcc -Wall -Wextra -Wpedantic -std=c99 -o graphics_editor graphics.c main.c -lm
```
- `-Wextra`: Additional warnings
- `-Wpedantic`: Pedantic warnings (very strict)

---

## Using Make (Optional)

### Build with Make
```bash
make
```

### Build and Run
```bash
make run
```

### Clean Build Artifacts
```bash
make clean
```

### Help
```bash
make help
```

### With ncurses Support
```bash
make -f Makefile.ncurses ncurses
```

---

## Using Visual Studio (MSVC)

### Developer Command Prompt

1. Open "x64 Native Tools Command Prompt for VS 2022"
2. Navigate to project:
   ```cmd
   cd C:\Users\Akshay bk\c.project
   ```
3. Compile:
   ```cmd
   cl graphics.c main.c /o graphics_editor.exe
   ```

### MSVC Flags

| Flag | GCC Equivalent | Purpose |
|------|---|---|
| `/Wall` | `-Wall` | Show all warnings |
| `/O2` | `-O2` | Optimization level 2 |
| `/Zi` | `-g` | Debug symbols |
| `/o` | `-o` | Output file |

### Build with batch file (Auto-detects MSVC)
```cmd
build.bat
```

---

## Troubleshooting Build Issues

### Issue: "undefined reference to `sin`" or `cos`

**Cause:** Math library not linked

**Solution:** Add `-lm` at END of command
```bash
gcc -Wall -std=c99 -o graphics_editor graphics.c main.c -lm
                                                                    ^^^
```

### Issue: "graphics.h: No such file or directory"

**Cause:** Not in correct directory or file is missing

**Solution:**
1. Verify you're in project directory: `pwd` (Linux/Mac) or `cd` (Windows)
2. List files: `ls` (Linux/Mac) or `dir` (Windows)
3. All three files must be present: graphics.h, graphics.c, main.c

### Issue: "gcc: command not found"

**Cause:** Compiler not installed or not in PATH

**Solution:**
- Install compiler (see INSTALL.md)
- Or add to PATH
- Close and reopen terminal after PATH change

### Issue: Compiler crashes or hangs

**Cause:** Usually rare, but can happen with corrupted files

**Solution:**
1. Clean build: `rm *.o` (Linux/Mac) or `del *.o` (Windows)
2. Try again: `gcc -Wall -std=c99 -o graphics_editor graphics.c main.c -lm`
3. If persists, check files for corruption

### Issue: "C99 not supported"

**Cause:** Very old compiler or configuration issue

**Solution:**
```bash
# Try C11 instead
gcc -Wall -std=c11 -o graphics_editor graphics.c main.c -lm

# Or no standard specified
gcc -Wall -o graphics_editor graphics.c main.c -lm
```

### Issue: Executable runs but program crashes

**Cause:** Usually PATH or library issues

**Solution:**
1. Rebuild with debug symbols: `gcc -g -Wall -std=c99 -o graphics_editor graphics.c main.c -lm`
2. Run with debugger: `gdb ./graphics_editor` (Linux/Mac)
3. Or try with `-v` flag to see verbose output

---

## Build Verification

### After compilation completes, verify:

1. **Executable exists:**
   ```bash
   # Windows
   dir graphics_editor.exe
   
   # Linux/Mac
   ls -la graphics_editor
   ```

2. **Executable has execute permissions (Linux/Mac):**
   ```bash
   chmod +x graphics_editor
   ```

3. **File size is reasonable:**
   - Usually 50-200 KB depending on compiler and flags
   - Very small (<10 KB) usually indicates linking issue
   - Very large (>1 MB) usually indicates not stripped/debug symbols included

4. **Program runs:**
   ```bash
   # Windows
   graphics_editor.exe
   
   # Linux/Mac
   ./graphics_editor
   ```

5. **Main menu displays**

---

## Advanced Build Options

### Cross-Compilation

**Build 32-bit from 64-bit:**
```bash
gcc -m32 -Wall -std=c99 -o graphics_editor graphics.c main.c -lm
```

**Build for Different Platform:**
- Windows cross-compile on Linux: Use MinGW-w64
- Requires: `x86_64-w64-mingw32-gcc`
- Command:
  ```bash
  x86_64-w64-mingw32-gcc -Wall -std=c99 -o graphics_editor.exe graphics.c main.c -lm
  ```

### Static Build (No Runtime Dependencies)

```bash
gcc -Wall -std=c99 -static -o graphics_editor graphics.c main.c -lm
```

### Stripped Executable (Smaller size)

```bash
gcc -Wall -std=c99 -o graphics_editor graphics.c main.c -lm
strip graphics_editor
```

---

## Build Performance

### Compilation Time

Expected times on modern hardware:
- **First build:** 1-3 seconds
- **Rebuild:** Usually instant (no changes)
- **With -O2 optimization:** May be slightly longer
- **With debug symbols (-g):** Slightly longer

### Executable Size

Typical sizes:
- **Release (stripped):** ~50-80 KB
- **With symbols (-g):** ~200-300 KB
- **Static build:** ~300-500 KB

### Runtime Performance

Program runs quickly on any modern machine:
- Menu response: Instant
- Drawing shapes: < 100ms
- Canvas display: < 50ms

---

## Building for Different OSes

### Windows Build
```cmd
cd C:\Users\Akshay bk\c.project
build.bat
graphics_editor.exe
```

### Linux Build
```bash
cd ~/c.project
chmod +x build.sh
./build.sh
./graphics_editor
```

### macOS Build
```bash
cd ~/c.project
chmod +x build.sh
./build.sh
./graphics_editor
```

All three use the same source code - no changes needed!

---

## Batch Building Multiple Versions

### Build all variants

**Windows:**
```cmd
REM Release build
gcc -O2 -Wall -std=c99 -o graphics_editor_release graphics.c main.c -lm

REM Debug build
gcc -g -Wall -std=c99 -o graphics_editor_debug graphics.c main.c -lm

REM Static build
gcc -Wall -std=c99 -static -o graphics_editor_static graphics.c main.c -lm
```

**Linux/Mac:**
```bash
# Release build
gcc -O2 -Wall -std=c99 -o graphics_editor_release graphics.c main.c -lm

# Debug build
gcc -g -Wall -std=c99 -o graphics_editor_debug graphics.c main.c -lm

# With all warnings
gcc -Wall -Wextra -Wpedantic -std=c99 -o graphics_editor_strict graphics.c main.c -lm
```

---

## CI/CD Integration

### GitHub Actions Example
```yaml
name: Build

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Build
        run: gcc -Wall -std=c99 -o graphics_editor graphics.c main.c -lm
      - name: Test
        run: ./graphics_editor --help 2>/dev/null || echo "Interactive program"
```

---

## Docker Build (Optional)

### Dockerfile
```dockerfile
FROM gcc:latest
WORKDIR /app
COPY . .
RUN gcc -Wall -std=c99 -o graphics_editor graphics.c main.c -lm
CMD ["./graphics_editor"]
```

### Build and run:
```bash
docker build -t graphics-editor .
docker run -it graphics-editor
```

---

## Build Checklist

Before deploying, verify:

- [ ] Builds without errors
- [ ] Builds without warnings (or acceptable warnings)
- [ ] Executable runs
- [ ] All menu items work
- [ ] Can draw all shapes
- [ ] Can add/modify/delete shapes
- [ ] Program exits cleanly
- [ ] No memory leaks (test with valgrind on Linux)

---

## Performance Testing

### Test with Valgrind (Linux/Mac)

```bash
# Install valgrind
# Ubuntu: sudo apt install valgrind
# Mac: brew install valgrind

# Run with memory checking
valgrind --leak-check=full ./graphics_editor
```

### Test execution time
```bash
# Linux/Mac
time ./graphics_editor

# Windows (PowerShell)
Measure-Command { .\graphics_editor.exe }
```

---

## Optimization Tips

### For Faster Compilation
```bash
gcc -O0 -Wall -std=c99 -o graphics_editor graphics.c main.c -lm
```

### For Faster Execution
```bash
gcc -O3 -Wall -std=c99 -o graphics_editor graphics.c main.c -lm
```

### For Smaller Executable
```bash
gcc -O2 -Wall -std=c99 -o graphics_editor graphics.c main.c -lm
strip graphics_editor
```

---

That's everything you need to know about building this project! 🚀
