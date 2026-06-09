# Makefile for 2D Graphics Editor

CC = gcc
CFLAGS = -Wall -std=c99 -lm
TARGET = graphics_editor
SRCS = graphics.c main.c
OBJS = $(SRCS:.c=.o)

# Default target
all: $(TARGET)

# Build the executable
$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJS)
	@echo "Build successful! Run with ./$(TARGET)"

# Compile source files
%.o: %.c graphics.h
	$(CC) $(CFLAGS) -c $< -o $@

# Run the program
run: $(TARGET)
	./$(TARGET)

# Clean build artifacts
clean:
	rm -f $(OBJS) $(TARGET) $(TARGET).exe

# Help target
help:
	@echo "Available targets:"
	@echo "  make          - Compile the project"
	@echo "  make run      - Compile and run the project"
	@echo "  make clean    - Remove compiled files"
	@echo "  make help     - Show this help message"

.PHONY: all run clean help
