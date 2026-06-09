# Using 2D Graphics Editor with OnlineGDB

## Quick Setup (2 Minutes)

### Step 1: Open OnlineGDB
Go to: **https://www.onlinegdb.com/**

### Step 2: Create New C Project
1. Click **"File"** menu
2. Click **"New"**
3. Select **"C"** 
4. Click **"Create"**

### Step 3: Copy the Code
1. Copy the entire content from **graphics_editor_online.c**
2. Paste it into the OnlineGDB editor (delete any existing code first)
3. Click **"Save"** (optional)

### Step 4: Compile & Run
1. Click **"Compile & Run"** button (or press `Ctrl+Shift+B`)
2. Program will start - follow the menu prompts

---

## How to Use the Program

### Example: Draw a Circle
```
1. Program shows main menu
2. Type: 2 (Draw Circle)
3. Enter center X: 25
4. Enter center Y: 10
5. Enter radius: 5
6. Enter label: MyCircle
7. Type: 1 (View Canvas) to see the circle
```

### Example: Draw a Rectangle
```
1. Type: 3 (Draw Rectangle)
2. Enter top-left X: 10
3. Enter top-left Y: 5
4. Enter bottom-right X: 40
5. Enter bottom-right Y: 20
6. Enter label: MyRect
7. Type: 1 (View Canvas)
```

### Menu Options
```
1. View Canvas      - See all shapes
2. Draw Circle      - Add a circle
3. Draw Rectangle   - Add a rectangle
4. Draw Line        - Add a line
5. Draw Triangle    - Add a triangle
6. View All Shapes  - List all shapes with IDs
7. Modify Shape     - Edit a shape
8. Delete Shape     - Remove a shape
9. Clear Canvas     - Remove all shapes
0. Exit             - Close program
```

---

## Canvas Information
- **Width:** 100 characters
- **Height:** 40 lines
- **Empty:** `_` (underscore)
- **Drawn:** `*` (asterisk)

### Valid Coordinates
- **X:** 0 to 99
- **Y:** 0 to 39

---

## Tips for Online Use

### Tip 1: Input Multiple Values
When prompted for coordinates, you can type them all with spaces:
```
Enter center X: 25
Enter center Y: 10
Enter radius: 5
```

### Tip 2: View Output
Click **"Output"** tab to see the canvas display

### Tip 3: Save Your Work
OnlineGDB saves code automatically. You can:
- Fork the project
- Share the link
- Export the code

### Tip 4: Debug Issues
If something goes wrong:
1. Check coordinates are within bounds (0-99 X, 0-39 Y)
2. Make sure radius is positive
3. Verify all three points for triangles are different
4. Try simpler shapes first (circle at center 50,20)

---

## Example Test

Try this sequence to test:

```
Menu: 2 (Draw Circle)
Center X: 50
Center Y: 20
Radius: 5
Label: Circle1

Menu: 3 (Draw Rectangle)
Top-left X: 30
Top-left Y: 10
Bottom-right X: 70
Bottom-right Y: 30
Label: Rect1

Menu: 1 (View Canvas)
→ You'll see both shapes!

Menu: 6 (View All Shapes)
→ Lists: Circle1 and Rect1

Menu: 0 (Exit)
```

---

## Alternative Online Compilers

If OnlineGDB doesn't work:

### **Replit.com**
1. Go to https://replit.com
2. Click "Create Repl"
3. Select "C"
4. Paste code
5. Click "Run"

### **TutorialsPoint**
1. Go to https://www.tutorialspoint.com/compile_c_online.php
2. Copy-paste code
3. Click "Compile & Execute"

---

## Full Code Location

The complete C code is saved as:
```
c:\Users\Akshay bk\c.project\graphics_editor_online.c
```

You can:
- Copy from that file
- Or copy directly from this guide below

---

## When Ready for Local Compilation

Once you have MinGW installed:

```powershell
cd "C:\Users\Akshay bk\c.project"
gcc -Wall -std=c99 -o graphics_editor graphics.c main.c -lm
.\graphics_editor.exe
```

Or use the separate files:
- graphics.h
- graphics.c  
- main.c

---

**Go to OnlineGDB now and paste the code to start testing!** 🚀
