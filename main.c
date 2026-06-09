#include "graphics.h"

void displayMainMenu() {
    printf("\n");
    printf("╔═══════════════════════════════════════════════╗\n");
    printf("║        2D GRAPHICS EDITOR - MAIN MENU         ║\n");
    printf("╠═══════════════════════════════════════════════╣\n");
    printf("║ 1. View Canvas                                ║\n");
    printf("║ 2. Draw Circle                                ║\n");
    printf("║ 3. Draw Rectangle                             ║\n");
    printf("║ 4. Draw Line                                  ║\n");
    printf("║ 5. Draw Triangle                              ║\n");
    printf("║ 6. View All Shapes                            ║\n");
    printf("║ 7. Modify Shape                               ║\n");
    printf("║ 8. Delete Shape                               ║\n");
    printf("║ 9. Clear Canvas                               ║\n");
    printf("║ 0. Exit                                       ║\n");
    printf("╚═══════════════════════════════════════════════╝\n");
    printf("Enter your choice: ");
}

void drawCircleMenu(Canvas* canvas) {
    int cx, cy, radius;
    char label[20];
    
    printf("\n--- Draw Circle ---\n");
    printf("Canvas dimensions: Width=%d, Height=%d\n", CANVAS_WIDTH, CANVAS_HEIGHT);
    printf("Enter center X (0-%d): ", CANVAS_WIDTH - 1);
    scanf("%d", &cx);
    printf("Enter center Y (0-%d): ", CANVAS_HEIGHT - 1);
    scanf("%d", &cy);
    printf("Enter radius: ");
    scanf("%d", &radius);
    printf("Enter label for this circle: ");
    scanf("%s", label);
    
    if (isInBounds(cx, cy)) {
        Shape shape;
        shape.type = CIRCLE;
        shape.x1 = cx;
        shape.y1 = cy;
        shape.x2 = radius;  // Using x2 to store radius
        strcpy(shape.label, label);
        
        int id = addShape(canvas, shape);
        printf("Circle added successfully! Shape ID: %d\n", id);
    } else {
        printf("Invalid coordinates!\n");
    }
}

void drawRectangleMenu(Canvas* canvas) {
    int x1, y1, x2, y2;
    char label[20];
    
    printf("\n--- Draw Rectangle ---\n");
    printf("Canvas dimensions: Width=%d, Height=%d\n", CANVAS_WIDTH, CANVAS_HEIGHT);
    printf("Enter top-left corner X (0-%d): ", CANVAS_WIDTH - 1);
    scanf("%d", &x1);
    printf("Enter top-left corner Y (0-%d): ", CANVAS_HEIGHT - 1);
    scanf("%d", &y1);
    printf("Enter bottom-right corner X (0-%d): ", CANVAS_WIDTH - 1);
    scanf("%d", &x2);
    printf("Enter bottom-right corner Y (0-%d): ", CANVAS_HEIGHT - 1);
    scanf("%d", &y2);
    printf("Enter label for this rectangle: ");
    scanf("%s", label);
    
    if (isInBounds(x1, y1) && isInBounds(x2, y2)) {
        Shape shape;
        shape.type = RECTANGLE;
        shape.x1 = x1;
        shape.y1 = y1;
        shape.x2 = x2;
        shape.y2 = y2;
        strcpy(shape.label, label);
        
        int id = addShape(canvas, shape);
        printf("Rectangle added successfully! Shape ID: %d\n", id);
    } else {
        printf("Invalid coordinates!\n");
    }
}

void drawLineMenu(Canvas* canvas) {
    int x1, y1, x2, y2;
    char label[20];
    
    printf("\n--- Draw Line ---\n");
    printf("Canvas dimensions: Width=%d, Height=%d\n", CANVAS_WIDTH, CANVAS_HEIGHT);
    printf("Enter starting point X (0-%d): ", CANVAS_WIDTH - 1);
    scanf("%d", &x1);
    printf("Enter starting point Y (0-%d): ", CANVAS_HEIGHT - 1);
    scanf("%d", &y1);
    printf("Enter ending point X (0-%d): ", CANVAS_WIDTH - 1);
    scanf("%d", &x2);
    printf("Enter ending point Y (0-%d): ", CANVAS_HEIGHT - 1);
    scanf("%d", &y2);
    printf("Enter label for this line: ");
    scanf("%s", label);
    
    if (isInBounds(x1, y1) && isInBounds(x2, y2)) {
        Shape shape;
        shape.type = LINE;
        shape.x1 = x1;
        shape.y1 = y1;
        shape.x2 = x2;
        shape.y2 = y2;
        strcpy(shape.label, label);
        
        int id = addShape(canvas, shape);
        printf("Line added successfully! Shape ID: %d\n", id);
    } else {
        printf("Invalid coordinates!\n");
    }
}

void drawTriangleMenu(Canvas* canvas) {
    int x1, y1, x2, y2, x3, y3;
    char label[20];
    
    printf("\n--- Draw Triangle ---\n");
    printf("Canvas dimensions: Width=%d, Height=%d\n", CANVAS_WIDTH, CANVAS_HEIGHT);
    printf("Enter first vertex X (0-%d): ", CANVAS_WIDTH - 1);
    scanf("%d", &x1);
    printf("Enter first vertex Y (0-%d): ", CANVAS_HEIGHT - 1);
    scanf("%d", &y1);
    printf("Enter second vertex X (0-%d): ", CANVAS_WIDTH - 1);
    scanf("%d", &x2);
    printf("Enter second vertex Y (0-%d): ", CANVAS_HEIGHT - 1);
    scanf("%d", &y2);
    printf("Enter third vertex X (0-%d): ", CANVAS_WIDTH - 1);
    scanf("%d", &x3);
    printf("Enter third vertex Y (0-%d): ", CANVAS_HEIGHT - 1);
    scanf("%d", &y3);
    printf("Enter label for this triangle: ");
    scanf("%s", label);
    
    if (isInBounds(x1, y1) && isInBounds(x2, y2) && isInBounds(x3, y3)) {
        Shape shape;
        shape.type = TRIANGLE;
        shape.x1 = x1;
        shape.y1 = y1;
        shape.x2 = x2;
        shape.y2 = y2;
        shape.x3 = x3;
        shape.y3 = y3;
        strcpy(shape.label, label);
        
        int id = addShape(canvas, shape);
        printf("Triangle added successfully! Shape ID: %d\n", id);
    } else {
        printf("Invalid coordinates!\n");
    }
}

void modifyShapeMenu(Canvas* canvas) {
    if (canvas->shape_count == 0) {
        printf("No shapes to modify!\n");
        return;
    }
    
    printShapeList(canvas);
    
    int shape_id;
    printf("Enter shape ID to modify: ");
    scanf("%d", &shape_id);
    
    if (shape_id < 1 || shape_id > canvas->shape_count) {
        printf("Invalid shape ID!\n");
        return;
    }
    
    Shape old_shape = canvas->shapes[shape_id - 1];
    Shape new_shape = old_shape;
    
    printf("\nModify which parameter?\n");
    printf("1. Change label\n");
    printf("2. Change coordinates\n");
    printf("Enter choice: ");
    int choice;
    scanf("%d", &choice);
    
    if (choice == 1) {
        printf("Enter new label: ");
        scanf("%s", new_shape.label);
        modifyShape(canvas, shape_id, new_shape);
        printf("Shape modified successfully!\n");
    } else if (choice == 2) {
        printf("This shape is of type: ");
        switch (old_shape.type) {
            case CIRCLE:
                printf("Circle\n");
                printf("Enter new center X: ");
                scanf("%d", &new_shape.x1);
                printf("Enter new center Y: ");
                scanf("%d", &new_shape.y1);
                printf("Enter new radius: ");
                scanf("%d", &new_shape.x2);
                break;
            case RECTANGLE:
                printf("Rectangle\n");
                printf("Enter new top-left X: ");
                scanf("%d", &new_shape.x1);
                printf("Enter new top-left Y: ");
                scanf("%d", &new_shape.y1);
                printf("Enter new bottom-right X: ");
                scanf("%d", &new_shape.x2);
                printf("Enter new bottom-right Y: ");
                scanf("%d", &new_shape.y2);
                break;
            case LINE:
                printf("Line\n");
                printf("Enter new start X: ");
                scanf("%d", &new_shape.x1);
                printf("Enter new start Y: ");
                scanf("%d", &new_shape.y1);
                printf("Enter new end X: ");
                scanf("%d", &new_shape.x2);
                printf("Enter new end Y: ");
                scanf("%d", &new_shape.y2);
                break;
            case TRIANGLE:
                printf("Triangle\n");
                printf("Enter new vertex 1 X: ");
                scanf("%d", &new_shape.x1);
                printf("Enter new vertex 1 Y: ");
                scanf("%d", &new_shape.y1);
                printf("Enter new vertex 2 X: ");
                scanf("%d", &new_shape.x2);
                printf("Enter new vertex 2 Y: ");
                scanf("%d", &new_shape.y2);
                printf("Enter new vertex 3 X: ");
                scanf("%d", &new_shape.x3);
                printf("Enter new vertex 3 Y: ");
                scanf("%d", &new_shape.y3);
                break;
        }
        modifyShape(canvas, shape_id, new_shape);
        printf("Shape modified successfully!\n");
    }
}

void deleteShapeMenu(Canvas* canvas) {
    if (canvas->shape_count == 0) {
        printf("No shapes to delete!\n");
        return;
    }
    
    printShapeList(canvas);
    
    int shape_id;
    printf("Enter shape ID to delete: ");
    scanf("%d", &shape_id);
    
    if (deleteShape(canvas, shape_id)) {
        printf("Shape deleted successfully!\n");
    }
}

void clearCanvasMenu(Canvas* canvas) {
    char confirm;
    printf("Are you sure you want to clear the entire canvas? (y/n): ");
    scanf(" %c", &confirm);
    
    if (confirm == 'y' || confirm == 'Y') {
        canvas->shape_count = 0;
        initializeCanvas(canvas);
        printf("Canvas cleared!\n");
    }
}

int main() {
    Canvas* canvas = createCanvas();
    
    if (canvas == NULL) {
        printf("Failed to create canvas!\n");
        return 1;
    }
    
    printf("╔═══════════════════════════════════════════════╗\n");
    printf("║    Welcome to 2D Graphics Editor              ║\n");
    printf("║    Canvas Size: %d x %d                    ║\n", CANVAS_WIDTH, CANVAS_HEIGHT);
    printf("╚═══════════════════════════════════════════════╝\n");
    
    int choice;
    int running = 1;
    
    while (running) {
        displayMainMenu();
        scanf("%d", &choice);
        
        switch (choice) {
            case 1:
                displayCanvas(canvas);
                break;
            case 2:
                drawCircleMenu(canvas);
                break;
            case 3:
                drawRectangleMenu(canvas);
                break;
            case 4:
                drawLineMenu(canvas);
                break;
            case 5:
                drawTriangleMenu(canvas);
                break;
            case 6:
                printShapeList(canvas);
                break;
            case 7:
                modifyShapeMenu(canvas);
                break;
            case 8:
                deleteShapeMenu(canvas);
                break;
            case 9:
                clearCanvasMenu(canvas);
                break;
            case 0:
                printf("Thank you for using 2D Graphics Editor. Goodbye!\n");
                running = 0;
                break;
            default:
                printf("Invalid choice! Please try again.\n");
        }
        
        if (running && choice != 0) {
            printf("\nPress Enter to continue...");
            getchar();
            getchar();
        }
    }
    
    free(canvas);
    return 0;
}
