#ifdef USE_NCURSES
#include <ncurses.h>
#include "graphics.h"

#define MENU_ITEMS 10

// Function to display menu using ncurses
int displayMenuNCurses() {
    WINDOW *menu_window;
    int choice = 0;
    int highlight = 0;
    char *choices[] = {
        "View Canvas",
        "Draw Circle",
        "Draw Rectangle",
        "Draw Line",
        "Draw Triangle",
        "View All Shapes",
        "Modify Shape",
        "Delete Shape",
        "Clear Canvas",
        "Exit"
    };

    initscr();  // Start ncurses mode
    cbreak();   // Disable line buffering
    noecho();   // Don't echo input
    keypad(stdscr, TRUE);  // Enable function keys

    int max_x, max_y;
    getmaxyx(stdscr, max_y, max_x);

    menu_window = newwin(MENU_ITEMS + 4, 50, (max_y - MENU_ITEMS) / 2, (max_x - 50) / 2);
    box(menu_window, 0, 0);

    while (1) {
        werase(menu_window);
        box(menu_window, 0, 0);

        mvwprintw(menu_window, 1, 15, "2D GRAPHICS EDITOR");

        for (int i = 0; i < MENU_ITEMS; i++) {
            if (i == highlight) {
                wattron(menu_window, A_REVERSE);
            }
            mvwprintw(menu_window, i + 3, 5, "%d. %s", i, choices[i]);
            if (i == highlight) {
                wattroff(menu_window, A_REVERSE);
            }
        }

        wrefresh(menu_window);

        int c = getch();
        if (c == KEY_UP) {
            highlight = (highlight - 1 + MENU_ITEMS) % MENU_ITEMS;
        } else if (c == KEY_DOWN) {
            highlight = (highlight + 1) % MENU_ITEMS;
        } else if (c == '\n') {
            choice = highlight;
            break;
        }
    }

    delwin(menu_window);
    endwin();  // End ncurses mode

    return choice;
}

// Display canvas using ncurses
void displayCanvasNCurses(Canvas* canvas) {
    initscr();
    cbreak();
    noecho();

    int max_x, max_y;
    getmaxyx(stdscr, max_y, max_x);

    clear();
    mvprintw(0, 0, "2D Graphics Canvas");
    mvprintw(1, 0, "═════════════════════════════════════════════════════════════════════════════════════════════════════");

    for (int i = 0; i < CANVAS_HEIGHT; i++) {
        mvprintw(i + 2, 0, "║");
        for (int j = 0; j < CANVAS_WIDTH; j++) {
            addch(canvas->canvas[i][j]);
        }
        printw("║");
    }

    mvprintw(CANVAS_HEIGHT + 2, 0, "═════════════════════════════════════════════════════════════════════════════════════════════════════");
    mvprintw(CANVAS_HEIGHT + 3, 0, "Press any key to continue...");

    refresh();
    getch();
    endwin();
}

#endif
