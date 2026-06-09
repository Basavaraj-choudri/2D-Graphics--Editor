# 2D Graphics Editor - Usage Guide

## Table of Contents
1. [Compilation](#compilation)
2. [Running the Program](#running-the-program)
3. [Menu Options](#menu-options)
4. [Step-by-Step Examples](#step-by-step-examples)
5. [Tips and Tricks](#tips-and-tricks)
6. [Troubleshooting](#troubleshooting)

---

## Compilation

### Prerequisites
- GCC compiler (or MSVC on Windows)
- Make tool (optional, for using Makefile)

### Basic Compilation

**Windows:**
```bash
compile.bat
```

**Linux/Mac with GCC:**
```bash
gcc -o graphics_editor graphics.c main.c -lm
```

**Using Make:**
```bash
make
```

### Compilation with ncurses Support (Linux/Mac)

First, install ncurses libraries:
```bash
# Linux (Ubuntu/Debian)
sudo apt install libncurses-dev

# Mac
brew install ncurses
```

Then compile:
```bash
gcc -o graphics_editor_ncurses graphics.c graphics_ncurses.c main.c -DUSE_NCURSES -lncurses -lm
```

Or using Makefile:
```bash
make -f Makefile.ncurses ncurses
```

---

## Running the Program

### Basic Version
```bash
./graphics_editor          # Linux/Mac
graphics_editor.exe        # Windows
```

### ncurses Version
```bash
./graphics_editor_ncurses
```

---

## Menu Options

### 1. View Canvas
Displays the current canvas with all shapes drawn on it.
- Shows the canvas with box-drawing characters
- Canvas is 100 characters wide and 40 characters tall
- Uses `_` for empty space and `*` for drawn pixels

### 2. Draw Circle
Adds a circle to the canvas.
- **Required inputs:**
  - Center X coordinate (0-99)
  - Center Y coordinate (0-39)
  - Radius (positive integer)
  - Label (up to 19 characters)

### 3. Draw Rectangle
Adds a rectangle to the canvas.
- **Required inputs:**
  - Top-left corner X coordinate
  - Top-left corner Y coordinate
  - Bottom-right corner X coordinate
  - Bottom-right corner Y coordinate
  - Label (up to 19 characters)

### 4. Draw Line
Adds a line to the canvas.
- **Required inputs:**
  - Starting point X
  - Starting point Y
  - Ending point X
  - Ending point Y
  - Label (up to 19 characters)

### 5. Draw Triangle
Adds a triangle to the canvas.
- **Required inputs:**
  - First vertex X and Y
  - Second vertex X and Y
  - Third vertex X and Y
  - Label (up to 19 characters)

### 6. View All Shapes
Displays a list of all shapes currently on the canvas with:
- Shape ID (used for modification/deletion)
- Label (user-defined name)
- Shape type (Circle, Rectangle, Line, or Triangle)
- Coordinates/parameters

### 7. Modify Shape
Edit an existing shape's properties.
- First, select which shape to modify by ID
- Choose to modify:
  - Label only
  - Coordinates (redraw on new position)
- Changes are applied immediately

### 8. Delete Shape
Remove a shape from the canvas.
- Select the shape by ID
- Shape is removed and canvas is redrawn

### 9. Clear Canvas
Remove all shapes and reset the canvas.
- Requires confirmation (y/n)
- All shape data is lost

### 0. Exit
Closes the application and frees all memory.

---

## Step-by-Step Examples

### Example 1: Drawing a Simple Circle

```
1. Run the program: ./graphics_editor
2. Select option 2 (Draw Circle)
3. When prompted:
   - Center X: 25
   - Center Y: 12
   - Radius: 5
   - Label: MyCircle
4. Select option 1 (View Canvas) to see the circle
```

Expected output: A circle with center at (25, 12) and radius 5

### Example 2: Drawing Multiple Shapes

```
1. Draw Circle (option 2)
   - Center: (20, 10), Radius: 4, Label: Circle1
2. Draw Rectangle (option 3)
   - Corners: (30, 5) to (50, 15), Label: Rect1
3. Draw Line (option 4)
   - From (10, 20) to (60, 30), Label: Line1
4. View Canvas (option 1) to see all shapes together
5. View All Shapes (option 6) to see their properties
```

### Example 3: Modifying a Shape

```
1. Draw a circle as above
2. View All Shapes (option 6) - note its ID
3. Select Modify Shape (option 7)
4. Enter the shape ID
5. Choose to modify coordinates
6. Enter new position and radius
7. View Canvas to see the change
```

### Example 4: Deleting and Recreating

```
1. Draw three shapes
2. View All Shapes and note their IDs
3. Delete Shape (option 8) - delete ID 2
4. View Canvas - shape is gone, others remain
5. View All Shapes - IDs are renumbered (1, 2 now)
6. Draw new shapes
```

---

## Tips and Tricks

### Coordinate System Tips
- **Top-left corner** is (0, 0)
- **Bottom-right corner** is (99, 39)
- **X increases** going right
- **Y increases** going down

### Drawing Tips
1. **Start small**: Use smaller radii and close points for precise drawings
2. **Use labels**: Descriptive labels help track shapes
3. **Plan ahead**: Sketch your design on paper first
4. **Test boundaries**: Keep coordinates well within bounds initially

### Performance Tips
- Maximum 50 shapes per canvas
- Large circles take longer to calculate
- Modifying redraws all shapes (optimal for updates)

### Creating Complex Drawings
1. Start with basic shapes (circles, rectangles)
2. Add details (lines, triangles)
3. Use spacing to avoid overlapping shapes
4. Modify positions if needed

### Useful Coordinate Values
- **Canvas center**: X=50, Y=20
- **Corners**: (0,0), (99,0), (0,39), (99,39)
- **Horizontal center**: X=50 (any Y)
- **Vertical center**: Y=20 (any X)

---

## Troubleshooting

### Problem: "Invalid coordinates!"
**Solution**: Check that all coordinates are within bounds:
- X: 0 to 99
- Y: 0 to 39

### Problem: Shapes don't appear as expected
**Possible causes**:
1. Coordinates outside canvas
2. Overlapping with other shapes (both are drawn, may appear merged)
3. Very small radius for circles (less than 1)

**Solution**: Use View All Shapes to verify coordinates

### Problem: Can't modify a shape
**Solutions**:
1. Verify the shape ID is correct (use View All Shapes first)
2. Ensure you input valid coordinates
3. Shape doesn't have to move; you can just change the label

### Problem: Compilation errors

**"gcc: command not found"**
- Install GCC or use Visual Studio/MSVC
- On Windows, use compile.bat

**"undefined reference to `sqrt`"**
- Add `-lm` flag: `gcc -o graphics_editor graphics.c main.c -lm`

**ncurses errors**
- Install libncurses-dev (Linux)
- Use basic version if ncurses unavailable
- On Windows, stick with basic version

### Problem: Program closes immediately
**Solutions**:
1. Run from command line/terminal
2. Check for compilation errors
3. Ensure all files are in the same directory

### Problem: Canvas display looks strange
**Possible causes**:
1. Terminal is too small
2. Terminal doesn't support UTF-8 box drawing
3. Terminal font doesn't display characters properly

**Solution**: Maximize terminal window or use a different terminal

---

## Advanced Usage

### Using as a Library
Include graphics.h in your own C programs:

```c
#include "graphics.h"

int main() {
    Canvas* canvas = createCanvas();
    
    Shape circle;
    circle.type = CIRCLE;
    circle.x1 = 25;
    circle.y1 = 10;
    circle.x2 = 5;
    strcpy(circle.label, "Circle");
    
    addShape(canvas, circle);
    displayCanvas(canvas);
    
    free(canvas);
    return 0;
}
```

Compile:
```bash
gcc -o my_program my_program.c graphics.c -lm
```

### Batch Drawing
Create an example.c file with multiple shapes and compile it:
```bash
gcc -o example example.c graphics.c -lm
./example
```

---

## Canvas Size Reference

The canvas is 100 characters wide and 40 characters tall:

```
(0,0) ──────────────────── (99,0)
  │                           │
  │  ← 100 characters →       │
  │                           │
  ├─ 40 lines of height      │
  │                           │
(0,39) ──────────────────── (99,39)
```

---

## Getting Help

1. Check the README.md for general information
2. Review the code comments in graphics.c and main.c
3. Run the example.c program to see usage
4. Experiment with small shapes first

---

## Example Run Session

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
║ 3. Draw Rectangle                             ║
║ 4. Draw Line                                  ║
║ 5. Draw Triangle                              ║
║ 6. View All Shapes                            ║
║ 7. Modify Shape                               ║
║ 8. Delete Shape                               ║
║ 9. Clear Canvas                               ║
║ 0. Exit                                       ║
╚═══════════════════════════════════════════════╝
Enter your choice: 2

--- Draw Circle ---
Canvas dimensions: Width=100, Height=40
Enter center X (0-99): 25
Enter center Y (0-39): 10
Enter radius: 6
Enter label for this circle: MyCircle
Circle added successfully! Shape ID: 1
```

---

That's all! Enjoy creating your 2D graphics!
