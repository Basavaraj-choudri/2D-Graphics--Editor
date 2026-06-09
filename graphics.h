#ifndef GRAPHICS_H
#define GRAPHICS_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define CANVAS_WIDTH 100
#define CANVAS_HEIGHT 40
#define MAX_SHAPES 50

#define CIRCLE 1
#define RECTANGLE 2
#define LINE 3
#define TRIANGLE 4

// Shape structure to store shape data
typedef struct {
    int type;           // Type of shape (CIRCLE, RECTANGLE, LINE, TRIANGLE)
    int x1, y1;        // Starting point / Center point
    int x2, y2;        // Ending point / Other parameters
    int x3, y3;        // For triangle third point
    char label[20];    // Label for the shape
} Shape;

// Canvas structure
typedef struct {
    char canvas[CANVAS_HEIGHT][CANVAS_WIDTH];
    Shape shapes[MAX_SHAPES];
    int shape_count;
} Canvas;

// Function declarations
Canvas* createCanvas();
void initializeCanvas(Canvas* canvas);
void displayCanvas(Canvas* canvas);

// Drawing functions
void drawLine(Canvas* canvas, int x1, int y1, int x2, int y2);
void drawCircle(Canvas* canvas, int cx, int cy, int radius);
void drawRectangle(Canvas* canvas, int x1, int y1, int x2, int y2);
void drawTriangle(Canvas* canvas, int x1, int y1, int x2, int y2, int x3, int y3);

// Shape management functions
int addShape(Canvas* canvas, Shape shape);
int deleteShape(Canvas* canvas, int shape_id);
int modifyShape(Canvas* canvas, int shape_id, Shape new_shape);
void redrawCanvas(Canvas* canvas);
void printShapeList(Canvas* canvas);

// Utility functions
void clearScreen();
void plotPoint(Canvas* canvas, int x, int y, char ch);
int isInBounds(int x, int y);

#endif
