# 2D Graphics Editor - C Programming Project

## Overview
A menu-driven 2D Graphics Editor built in C that allows users to draw and manipulate geometric shapes on a 2D character array canvas.

## Features

### Drawing Capabilities
- **Circle**: Draw circles using the Midpoint Circle Algorithm
- **Rectangle**: Draw rectangles with specified corners
- **Line**: Draw lines using Bresenham's Line Algorithm
- **Triangle**: Draw triangles with three vertices

### Shape Management
- **Add Objects**: Dynamically add shapes to the canvas with custom labels
- **Delete Objects**: Remove shapes by their ID
- **Modify Objects**: Edit shape coordinates and labels
- **View All Shapes**: Display a list of all shapes currently on the canvas

### Canvas
- **Canvas Size**: 100 x 40 characters
- **Empty Character**: `_` (underscore)
- **Drawing Character**: `*` (asterisk)
- **Maximum Shapes**: 50 shapes per canvas
- **Clear Canvas**: Reset the entire canvas

## Project Structure

```
c.project/
├── graphics.h          # Header file with function declarations and shape structures
├── graphics.c          # Implementation of drawing algorithms and shape management
├── main.c              # Menu-driven user interface
├── compile.bat         # Windows compilation script
├── Makefile            # Alternative compilation method
└── README.md           # This file
```

## Compilation

### Method 1: Using compile.bat (Windows)
```bash
compile.bat
```
This script automatically detects available compilers (GCC or MSVC) and compiles the project.

### Method 2: Using GCC (Windows/Linux/Mac)
```bash
gcc -o graphics_editor graphics.c main.c -lm
```

### Method 3: Using MSVC (Windows)
```bash
cl graphics.c main.c /o graphics_editor.exe
```

### Method 4: Using Makefile
```bash
make
```

## Usage

### Running the Program
```bash
./graphics_editor          # Linux/Mac
graphics_editor.exe        # Windows
```

### Main Menu Options
1. **View Canvas** - Display the current canvas with all drawn shapes
2. **Draw Circle** - Add a circle (requires center X, Y and radius)
3. **Draw Rectangle** - Add a rectangle (requires two opposite corners)
4. **Draw Line** - Add a line (requires start and end points)
5. **Draw Triangle** - Add a triangle (requires three vertices)
6. **View All Shapes** - Display list of all shapes with their properties
7. **Modify Shape** - Edit an existing shape's coordinates or label
8. **Delete Shape** - Remove a shape from the canvas
9. **Clear Canvas** - Remove all shapes and reset the canvas
0. **Exit** - Close the application

## Examples

### Drawing a Circle
```
1. Select option 2 from main menu
2. Enter center X: 20
3. Enter center Y: 15
4. Enter radius: 8
5. Enter label: MyCircle
```

### Drawing a Rectangle
```
1. Select option 3 from main menu
2. Enter top-left corner X: 10
3. Enter top-left corner Y: 5
4. Enter bottom-right corner X: 40
5. Enter bottom-right corner Y: 25
6. Enter label: MyRectangle
```

### Drawing a Line
```
1. Select option 4 from main menu
2. Enter starting point X: 5
3. Enter starting point Y: 10
4. Enter ending point X: 50
5. Enter ending point Y: 30
6. Enter label: MyLine
```

### Drawing a Triangle
```
1. Select option 5 from main menu
2. Enter three vertices with their X and Y coordinates
3. Enter a label for the triangle
```

## Data Structures

### Shape Structure
```c
typedef struct {
    int type;           // CIRCLE, RECTANGLE, LINE, or TRIANGLE
    int x1, y1;         // Starting/Center point
    int x2, y2;         // Ending/Other parameters
    int x3, y3;         // Third point (for triangle)
    char label[20];     // Shape label
} Shape;
```

### Canvas Structure
```c
typedef struct {
    char canvas[CANVAS_HEIGHT][CANVAS_WIDTH];  // 2D character array
    Shape shapes[MAX_SHAPES];                  // Array of shapes
    int shape_count;                           // Current number of shapes
} Canvas;
```

## Drawing Algorithms

### 1. Bresenham's Line Algorithm
Used for efficient line drawing with integer arithmetic. Determines which pixels to illuminate for a line between two points.

### 2. Midpoint Circle Algorithm
Used for efficient circle drawing. Calculates circle points in one octant and uses symmetry to plot all 8 octants.

### 3. Rectangle Drawing
Draws horizontal and vertical lines connecting the four corners of the specified rectangle.

### 4. Triangle Drawing
Uses the line drawing algorithm to connect three vertices.

## Constants

```c
#define CANVAS_WIDTH 100      // Width of canvas
#define CANVAS_HEIGHT 40      // Height of canvas
#define MAX_SHAPES 50         // Maximum number of shapes
#define CIRCLE 1
#define RECTANGLE 2
#define LINE 3
#define TRIANGLE 4
```

## Limitations

- Canvas is limited to 100x40 characters
- Maximum 50 shapes can be stored
- Filled shapes are not supported (only outlines)
- No rotation or scaling capabilities
- No save/load functionality in this version

## Future Enhancements

- Add ncurses support for better graphics and menu display
- Save and load drawings to/from files
- Undo/Redo functionality
- Filled shapes
- Shape rotation and scaling
- Color support (if using ncurses)
- Multi-layer support
- Shape properties dialog

## Technical Details

### Memory Management
- Canvas and shapes are dynamically allocated
- Clean up with `free()` when program exits
- All input is validated for boundary conditions

### Coordinate System
- X increases from left to right (0 to CANVAS_WIDTH-1)
- Y increases from top to bottom (0 to CANVAS_HEIGHT-1)
- Origin is at top-left corner

## Compilation Issues

### GCC Not Found
Install GCC:
- **Windows**: Use MinGW or WSL
- **Linux**: `sudo apt install build-essential`
- **Mac**: Install Xcode Command Line Tools

### MSVC Not Found
Install Visual Studio with C++ development tools or use MinGW/GCC instead.

## Notes

- The program uses `system("cls")` for Windows. Modify to `system("clear")` for Linux/Mac.
- The canvas uses UTF-8 box-drawing characters for better visualization.
- All coordinates must be within canvas bounds (0-99 for X, 0-39 for Y).
- Shape labels are limited to 19 characters.

## License

This is an educational project for learning C programming concepts.

## Author

2D Graphics Editor - Educational Project

## Support

For any issues or improvements, review the code and test with various shape combinations.
