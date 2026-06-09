# Step-by-Step Compilation Guide for Windows

## Complete Guide to Compile the 2D Graphics Editor

This guide walks you through exactly how to install a C compiler and compile your program.

---

## Part 1: Install a C Compiler

### Step 1.1: Download MinGW-w64

1. **Open your web browser**
2. **Go to:** https://www.mingw-w64.org/downloads/
3. **Click:** "Online installer" button (about 1 MB file)
4. **Save the file** to your Downloads folder
   - The filename will be something like: `x86_64-w64-mingw32-online-installer.exe`

### Step 1.2: Run the Installer

1. **Double-click** the downloaded installer
2. **Windows may ask:** "Do you want to allow this app to make changes to your device?"
   - Click **"Yes"**
3. **Wait** for the installer window to open (may take 10-20 seconds)

### Step 1.3: Configure Installation Settings

When the installer opens, you'll see a window. Configure these settings:

**Setting 1: Version**
- Leave as default (latest version)

**Setting 2: Architecture**
- Select: **x86_64** ✓ (check this box)
- Uncheck: x86 (if checked)
- Why: Your Windows is 64-bit

**Setting 3: Threads**
- Select: **posix** ✓ (check this box)
- Uncheck: win32 (if checked)
- Why: POSIX threads are standard

**Setting 4: Exception**
- Select: **seh** ✓ (check this box)
- Uncheck: dwarf (if checked)
- Why: SEH (Structured Exception Handling) is modern

**Setting 5: Build Revision**
- Select: **Latest** or **0** ✓
- Default is usually fine

### Step 1.4: Installation Path

You'll be asked where to install. Set it to:
```
C:\MinGW64
```

**Important:** Use exactly this path (makes future steps easier)

### Step 1.5: Install

1. **Click:** "Next" button
2. **Click:** "Install" button
3. **Wait:** Installation will take 2-5 minutes
   - You'll see progress bar
   - A terminal window may open showing installation progress
   - This is normal - let it finish

4. **When complete:**
   - You'll see: "Installation complete"
   - Click: "Finish"

---

## Part 2: Add MinGW to System PATH

After installation, you need to tell Windows where GCC is located. This is called adding to PATH.

### Step 2.1: Open Environment Variables

1. **Press:** `Win + X` (hold Windows key, press X)
2. **Click:** "System" (or "Settings")
3. **Look for and click:** "Advanced system settings" (right side panel)
   - Alternative: Press `Win + Pause`, then "Advanced system settings"

### Step 2.2: Open Environment Variables Dialog

1. **Click:** "Environment Variables..." button (bottom right)
2. **A dialog will open** with two sections:
   - "User variables for [Your Name]"
   - "System variables"

### Step 2.3: Add to PATH

1. **Click:** on "Path" (in "User variables" section - upper half)
   - If "Path" doesn't exist, skip to Step 2.4
2. **Click:** "Edit" button
3. **Click:** "New" button
4. **Type exactly:** `C:\MinGW64\bin`
5. **Click:** "OK"

### Step 2.4: Create PATH if it doesn't exist

If you don't see "Path" in User variables:

1. **Click:** "New..." button (in User variables section)
2. **Enter:**
   - Variable name: `Path`
   - Variable value: `C:\MinGW64\bin`
3. **Click:** "OK"

### Step 2.5: Apply Changes

1. **Click:** "OK" button (closes the Environment Variables dialog)
2. **Click:** "OK" button (closes Advanced System Settings)
3. **Click:** "OK" or close the window

### Step 2.6: Restart PowerShell/Command Prompt

This is **IMPORTANT** - you MUST restart:

1. **Close ALL PowerShell and Command Prompt windows**
2. **Open a NEW PowerShell window** (Start menu → PowerShell)

---

## Part 3: Verify Installation

### Step 3.1: Test GCC

In your NEW PowerShell window:

```powershell
gcc --version
```

**Expected output:**
```
gcc (GCC) 14.1.0
Copyright (C) 2024 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```

✓ **If you see version info:** Installation successful! Go to Part 4.

✗ **If you see "gcc: command not found":**
- Close PowerShell
- Open a NEW PowerShell window again
- Try again
- If still not found, you may need to manually add PATH (see Step 2.3)

---

## Part 4: Compile Your Program

### Step 4.1: Navigate to Project Folder

In PowerShell, type:

```powershell
cd "c:\Users\Akshay bk\c.project"
```

**Verify** you're in the right folder by typing:

```powershell
ls
```

You should see these files:
- graphics.h
- graphics.c
- main.c
- build.bat
- README.md
- And other files

### Step 4.2: Compile

Type this command exactly:

```powershell
gcc -Wall -std=c99 -o graphics_editor graphics.c main.c -lm
```

**Breakdown of this command:**
- `gcc` - the compiler
- `-Wall` - show all warnings
- `-std=c99` - use C99 standard
- `-o graphics_editor` - output filename
- `graphics.c main.c` - source files to compile
- `-lm` - link math library (important!)

**Wait** while it compiles. You should see the prompt return within 10 seconds.

### Step 4.3: Check for Errors

After compilation, you should see:
- No error messages
- The cursor returns
- You're back at the prompt

✓ **Success:** A file called `graphics_editor.exe` was created

✗ **If you see errors:**

**Error: "undefined reference to `sin`"**
- You forgot the `-lm` flag
- Rerun: `gcc -Wall -std=c99 -o graphics_editor graphics.c main.c -lm`

**Error: "graphics.h: No such file or directory"**
- Wrong directory
- Check files with: `ls`
- Make sure all three source files are present

**Error: "gcc: command not found"**
- PATH not set correctly
- Close PowerShell completely
- Open NEW PowerShell window
- Try gcc --version first

### Step 4.4: Verify Executable was Created

```powershell
ls -Name *.exe
```

You should see: `graphics_editor.exe`

---

## Part 5: Run Your Program

### Step 5.1: Execute the Program

```powershell
.\graphics_editor.exe
```

Or simply:

```powershell
.\graphics_editor
```

### Step 5.2: Main Menu Should Appear

You'll see:
```
╔═══════════════════════════════════════════════╗
║    Welcome to 2D Graphics Editor              ║
║    Canvas Size: 100 x 40                      ║
╚═══════════════════════════════════════════════╝

╔═══════════════════════════════════════════════╗
║        2D GRAPHICS EDITOR - MAIN MENU         ║
╠═══════════════════════════════════════════════╣
║ 1. View Canvas                                ║
║ 2. Draw Circle                                ║
│ 3. Draw Rectangle                             ║
│ 4. Draw Line                                  ║
│ 5. Draw Triangle                              ║
│ 6. View All Shapes                            ║
│ 7. Modify Shape                               ║
│ 8. Delete Shape                               ║
│ 9. Clear Canvas                               ║
│ 0. Exit                                       ║
╚═══════════════════════════════════════════════╝
Enter your choice:
```

✓ **Perfect!** Your program is running!

### Step 5.3: Test the Program

Try this:
1. **Type:** `2` (Draw Circle)
2. **Press:** Enter
3. **Follow** the prompts to enter coordinates
4. **Type:** `1` (View Canvas)
5. **You should see** a circle drawn!

---

## Troubleshooting

### Problem: "The term 'gcc' is not recognized"

**Cause:** PATH not set or not restarted PowerShell

**Solution:**
1. Verify MinGW is installed: Check if `C:\MinGW64\bin` exists
2. Close ALL PowerShell windows (use Task Manager if needed)
3. Open NEW PowerShell
4. Try: `gcc --version`

If still not working, manually add to PATH:
1. Right-click "This PC" → Properties
2. Click "Advanced system settings"
3. Click "Environment Variables"
4. Click "Path" under System variables
5. Click "Edit"
6. Click "New"
7. Add: `C:\MinGW64\bin`
8. Click OK multiple times
9. Restart PowerShell again

### Problem: Compilation fails with "undefined reference"

**Cause:** Missing `-lm` flag

**Solution:** Rerun with correct command:
```powershell
gcc -Wall -std=c99 -o graphics_editor graphics.c main.c -lm
```

Notice `-lm` at the end!

### Problem: "graphics.h: No such file or directory"

**Cause:** Wrong directory or files missing

**Solution:**
1. Verify directory: `cd "c:\Users\Akshay bk\c.project"`
2. List files: `ls`
3. Make sure you see: graphics.h, graphics.c, main.c
4. If files are missing, extract project again

### Problem: Program runs but crashes immediately

**Cause:** Library issue or PATH problem

**Solution:**
1. Try rebuilding: `gcc -Wall -std=c99 -o graphics_editor graphics.c main.c -lm`
2. Try with debug symbols: `gcc -g -Wall -std=c99 -o graphics_editor graphics.c main.c -lm`
3. Check that all source files are intact

### Problem: Can't find graphics_editor.exe after compilation

**Cause:** Compilation failed silently or executable in different location

**Solution:**
1. Look for it: `ls *.exe` or `dir *.exe`
2. Check for errors in compilation output
3. Try recompiling with verbose output: `gcc -v -Wall -std=c99 -o graphics_editor graphics.c main.c -lm`

---

## Quick Reference

### One-Time Setup
```powershell
# 1. Download MinGW from: https://www.mingw-w64.org/downloads/
# 2. Run installer, set path to C:\MinGW64
# 3. Add C:\MinGW64\bin to PATH
# 4. Restart PowerShell
# 5. Verify: gcc --version
```

### Every Time You Compile
```powershell
cd "c:\Users\Akshay bk\c.project"
gcc -Wall -std=c99 -o graphics_editor graphics.c main.c -lm
.\graphics_editor.exe
```

### Alternative: Using Batch File
```powershell
cd "c:\Users\Akshay bk\c.project"
.\build.bat
.\graphics_editor.exe
```

---

## Success Checklist

- [ ] Downloaded MinGW
- [ ] Ran MinGW installer
- [ ] Set installation path to C:\MinGW64
- [ ] Added C:\MinGW64\bin to PATH environment variable
- [ ] Restarted PowerShell
- [ ] Verified: `gcc --version` shows version info
- [ ] Navigated to project folder: `cd "c:\Users\Akshay bk\c.project"`
- [ ] Compiled: `gcc -Wall -std=c99 -o graphics_editor graphics.c main.c -lm`
- [ ] Verified executable exists: `ls graphics_editor.exe`
- [ ] Ran program: `.\graphics_editor.exe`
- [ ] Main menu appeared
- [ ] Drew a shape and verified it displayed

---

## Next Steps

1. Read [USAGE.md](USAGE.md) for detailed program usage
2. Explore the source code in graphics.c and main.c
3. Try the example program: `gcc -Wall -std=c99 -o example example.c graphics.c -lm`
4. Modify the code and recompile

---

Congratulations! Your 2D Graphics Editor in C is now running! 🎉

If you have any issues, refer to the Troubleshooting section above.
