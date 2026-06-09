/* 
   Example usage of the Graphics Editor library
   This file demonstrates how to use the graphics functions programmatically
   Compile with: gcc -o example example.c graphics.c -lm
*/

#include "graphics.h"

int main() {
    // Create a new canvas
    Canvas* canvas = createCanvas();
    
    if (canvas == NULL) {
        printf("Failed to create canvas!\n");
        return 1;
    }
    
    printf("Creating example drawing with multiple shapes...\n\n");
    
    // Example 1: Add a circle in the center
    Shape circle;
    circle.type = CIRCLE;
    circle.x1 = 30;      // Center X
    circle.y1 = 10;      // Center Y
    circle.x2 = 6;       // Radius
    strcpy(circle.label, "MainCircle");
    addShape(canvas, circle);
    printf("Added circle at (30, 10) with radius 6\n");
    
    // Example 2: Add a rectangle
    Shape rect;
    rect.type = RECTANGLE;
    rect.x1 = 5;         // Top-left X
    rect.y1 = 5;         // Top-left Y
    rect.x2 = 20;        // Bottom-right X
    rect.y2 = 15;        // Bottom-right Y
    strcpy(rect.label, "Rectangle1");
    addShape(canvas, rect);
    printf("Added rectangle from (5, 5) to (20, 15)\n");
    
    // Example 3: Add a line
    Shape line;
    line.type = LINE;
    line.x1 = 10;        // Start X
    line.y1 = 20;        // Start Y
    line.x2 = 50;        // End X
    line.y2 = 30;        // End Y
    strcpy(line.label, "DiagonalLine");
    addShape(canvas, line);
    printf("Added line from (10, 20) to (50, 30)\n");
    
    // Example 4: Add a triangle
    Shape triangle;
    triangle.type = TRIANGLE;
    triangle.x1 = 60;    // Vertex 1 X
    triangle.y1 = 5;     // Vertex 1 Y
    triangle.x2 = 70;    // Vertex 2 X
    triangle.y2 = 15;    // Vertex 2 Y
    triangle.x3 = 50;    // Vertex 3 X
    triangle.y3 = 15;    // Vertex 3 Y
    strcpy(triangle.label, "Triangle1");
    addShape(canvas, triangle);
    printf("Added triangle with vertices at (60,5), (70,15), (50,15)\n");
    
    // Example 5: Add another circle
    Shape circle2;
    circle2.type = CIRCLE;
    circle2.x1 = 75;
    circle2.y1 = 25;
    circle2.x2 = 5;
    strcpy(circle2.label, "SmallCircle");
    addShape(canvas, circle2);
    printf("Added small circle at (75, 25) with radius 5\n");
    
    // Display the canvas
    printf("\n");
    displayCanvas(canvas);
    
    // Display list of shapes
    printShapeList(canvas);
    
    // Example 6: Modify a shape (change rectangle coordinates)
    printf("Modifying rectangle to new position...\n");
    Shape modified_rect;
    modified_rect.type = RECTANGLE;
    modified_rect.x1 = 35;
    modified_rect.y1 = 20;
    modified_rect.x2 = 55;
    modified_rect.y2 = 35;
    strcpy(modified_rect.label, "Rectangle1");
    modifyShape(canvas, 2, modified_rect);  // Modify shape ID 2
    
    // Display the modified canvas
    printf("\nCanvas after modification:\n");
    displayCanvas(canvas);
    
    // Example 7: Delete a shape (delete the line)
    printf("Deleting the line (Shape ID 3)...\n");
    deleteShape(canvas, 3);
    
    // Display the final canvas
    printf("\nCanvas after deletion:\n");
    displayCanvas(canvas);
    
    // Final shape list
    printShapeList(canvas);
    
    // Cleanup
    free(canvas);
    
    printf("Example completed successfully!\n");
    return 0;
}
