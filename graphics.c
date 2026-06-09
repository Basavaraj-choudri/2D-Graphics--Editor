#include "graphics.h"

// Create a new canvas
Canvas* createCanvas() {
    Canvas* canvas = (Canvas*)malloc(sizeof(Canvas));
    if (canvas == NULL) {
        printf("Memory allocation failed!\n");
        return NULL;
    }
    canvas->shape_count = 0;
    initializeCanvas(canvas);
    return canvas;
}

// Initialize canvas with underscores
void initializeCanvas(Canvas* canvas) {
    for (int i = 0; i < CANVAS_HEIGHT; i++) {
        for (int j = 0; j < CANVAS_WIDTH; j++) {
            canvas->canvas[i][j] = '_';
        }
    }
}

// Check if coordinates are in bounds
int isInBounds(int x, int y) {
    return (x >= 0 && x < CANVAS_WIDTH && y >= 0 && y < CANVAS_HEIGHT);
}

// Plot a point on the canvas
void plotPoint(Canvas* canvas, int x, int y, char ch) {
    if (isInBounds(x, y)) {
        canvas->canvas[y][x] = ch;
    }
}

// Draw line using Bresenham's line algorithm
void drawLine(Canvas* canvas, int x1, int y1, int x2, int y2) {
    int dx = abs(x2 - x1);
    int dy = abs(y2 - y1);
    int sx = (x1 < x2) ? 1 : -1;
    int sy = (y1 < y2) ? 1 : -1;
    int err = dx - dy;
    
    int x = x1, y = y1;
    
    while (1) {
        plotPoint(canvas, x, y, '*');
        
        if (x == x2 && y == y2) break;
        
        int e2 = 2 * err;
        if (e2 > -dy) {
            err -= dy;
            x += sx;
        }
        if (e2 < dx) {
            err += dx;
            y += sy;
        }
    }
}

// Draw circle using Midpoint circle algorithm
void drawCircle(Canvas* canvas, int cx, int cy, int radius) {
    int x = 0;
    int y = radius;
    int d = 3 - 2 * radius;
    
    while (x <= y) {
        // Plot 8 octants
        plotPoint(canvas, cx + x, cy + y, '*');
        plotPoint(canvas, cx - x, cy + y, '*');
        plotPoint(canvas, cx + x, cy - y, '*');
        plotPoint(canvas, cx - x, cy - y, '*');
        plotPoint(canvas, cx + y, cy + x, '*');
        plotPoint(canvas, cx - y, cy + x, '*');
        plotPoint(canvas, cx + y, cy - x, '*');
        plotPoint(canvas, cx - y, cy - x, '*');
        
        if (d < 0) {
            d = d + 4 * x + 6;
        } else {
            d = d + 4 * (x - y) + 10;
            y--;
        }
        x++;
    }
}

// Draw rectangle
void drawRectangle(Canvas* canvas, int x1, int y1, int x2, int y2) {
    // Ensure x1 < x2 and y1 < y2
    if (x1 > x2) { int temp = x1; x1 = x2; x2 = temp; }
    if (y1 > y2) { int temp = y1; y1 = y2; y2 = temp; }
    
    // Draw top and bottom lines
    for (int x = x1; x <= x2; x++) {
        plotPoint(canvas, x, y1, '*');
        plotPoint(canvas, x, y2, '*');
    }
    
    // Draw left and right lines
    for (int y = y1; y <= y2; y++) {
        plotPoint(canvas, x1, y, '*');
        plotPoint(canvas, x2, y, '*');
    }
}

// Draw triangle
void drawTriangle(Canvas* canvas, int x1, int y1, int x2, int y2, int x3, int y3) {
    // Draw three sides
    drawLine(canvas, x1, y1, x2, y2);
    drawLine(canvas, x2, y2, x3, y3);
    drawLine(canvas, x3, y3, x1, y1);
}

// Display the canvas
void displayCanvas(Canvas* canvas) {
    printf("\n");
    printf("╔");
    for (int i = 0; i < CANVAS_WIDTH; i++) printf("═");
    printf("╗\n");
    
    for (int i = 0; i < CANVAS_HEIGHT; i++) {
        printf("║");
        for (int j = 0; j < CANVAS_WIDTH; j++) {
            printf("%c", canvas->canvas[i][j]);
        }
        printf("║\n");
    }
    
    printf("╚");
    for (int i = 0; i < CANVAS_WIDTH; i++) printf("═");
    printf("╝\n\n");
}

// Add shape to canvas
int addShape(Canvas* canvas, Shape shape) {
    if (canvas->shape_count >= MAX_SHAPES) {
        printf("Maximum shapes reached!\n");
        return 0;
    }
    
    canvas->shapes[canvas->shape_count] = shape;
    canvas->shape_count++;
    
    // Draw the shape on canvas
    switch (shape.type) {
        case CIRCLE:
            drawCircle(canvas, shape.x1, shape.y1, shape.x2);
            break;
        case RECTANGLE:
            drawRectangle(canvas, shape.x1, shape.y1, shape.x2, shape.y2);
            break;
        case LINE:
            drawLine(canvas, shape.x1, shape.y1, shape.x2, shape.y2);
            break;
        case TRIANGLE:
            drawTriangle(canvas, shape.x1, shape.y1, shape.x2, shape.y2, shape.x3, shape.y3);
            break;
    }
    
    return canvas->shape_count;
}

// Delete shape from canvas
int deleteShape(Canvas* canvas, int shape_id) {
    if (shape_id < 1 || shape_id > canvas->shape_count) {
        printf("Invalid shape ID!\n");
        return 0;
    }
    
    // Remove shape from list
    for (int i = shape_id - 1; i < canvas->shape_count - 1; i++) {
        canvas->shapes[i] = canvas->shapes[i + 1];
    }
    canvas->shape_count--;
    
    // Redraw canvas
    redrawCanvas(canvas);
    
    return 1;
}

// Modify shape
int modifyShape(Canvas* canvas, int shape_id, Shape new_shape) {
    if (shape_id < 1 || shape_id > canvas->shape_count) {
        printf("Invalid shape ID!\n");
        return 0;
    }
    
    canvas->shapes[shape_id - 1] = new_shape;
    redrawCanvas(canvas);
    
    return 1;
}

// Redraw all shapes on canvas
void redrawCanvas(Canvas* canvas) {
    initializeCanvas(canvas);
    
    for (int i = 0; i < canvas->shape_count; i++) {
        Shape shape = canvas->shapes[i];
        switch (shape.type) {
            case CIRCLE:
                drawCircle(canvas, shape.x1, shape.y1, shape.x2);
                break;
            case RECTANGLE:
                drawRectangle(canvas, shape.x1, shape.y1, shape.x2, shape.y2);
                break;
            case LINE:
                drawLine(canvas, shape.x1, shape.y1, shape.x2, shape.y2);
                break;
            case TRIANGLE:
                drawTriangle(canvas, shape.x1, shape.y1, shape.x2, shape.y2, shape.x3, shape.y3);
                break;
        }
    }
}

// Print list of shapes
void printShapeList(Canvas* canvas) {
    if (canvas->shape_count == 0) {
        printf("No shapes on canvas.\n");
        return;
    }
    
    printf("\n========== SHAPES ON CANVAS ==========\n");
    for (int i = 0; i < canvas->shape_count; i++) {
        printf("ID: %d | Label: %s | Type: ", i + 1, canvas->shapes[i].label);
        switch (canvas->shapes[i].type) {
            case CIRCLE:
                printf("Circle (Center: %d,%d, Radius: %d)\n", 
                       canvas->shapes[i].x1, canvas->shapes[i].y1, canvas->shapes[i].x2);
                break;
            case RECTANGLE:
                printf("Rectangle (P1: %d,%d, P2: %d,%d)\n", 
                       canvas->shapes[i].x1, canvas->shapes[i].y1, 
                       canvas->shapes[i].x2, canvas->shapes[i].y2);
                break;
            case LINE:
                printf("Line (P1: %d,%d, P2: %d,%d)\n", 
                       canvas->shapes[i].x1, canvas->shapes[i].y1, 
                       canvas->shapes[i].x2, canvas->shapes[i].y2);
                break;
            case TRIANGLE:
                printf("Triangle (P1: %d,%d, P2: %d,%d, P3: %d,%d)\n", 
                       canvas->shapes[i].x1, canvas->shapes[i].y1, 
                       canvas->shapes[i].x2, canvas->shapes[i].y2,
                       canvas->shapes[i].x3, canvas->shapes[i].y3);
                break;
        }
    }
    printf("=======================================\n\n");
}

// Clear screen
void clearScreen() {
    system("cls");
}
