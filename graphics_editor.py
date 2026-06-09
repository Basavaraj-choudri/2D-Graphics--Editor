#!/usr/bin/env python3
"""
2D Graphics Editor - Python Version
Provides the same functionality as the C version
Uses tkinter for GUI (built-in with Python)
"""

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import math
from dataclasses import dataclass
from typing import List

# Shape types
CIRCLE = 1
RECTANGLE = 2
LINE = 3
TRIANGLE = 4

CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 800

@dataclass
class Shape:
    """Shape data class"""
    type: int
    x1: int
    y1: int
    x2: int = 0
    y2: int = 0
    x3: int = 0
    y3: int = 0
    label: str = ""
    canvas_id: int = None  # tkinter canvas item ID

class GraphicsEditor:
    """2D Graphics Editor Application"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("2D Graphics Editor")
        self.root.geometry("1200x900")
        
        self.shapes: List[Shape] = []
        self.selected_shape = None
        
        self.setup_ui()
        self.setup_canvas()
        
    def setup_ui(self):
        """Setup the user interface"""
        # Menu bar
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Clear Canvas", command=self.clear_canvas)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        
        # Toolbar frame
        toolbar = ttk.Frame(self.root)
        toolbar.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        
        ttk.Label(toolbar, text="Draw:").pack(side=tk.LEFT, padx=5)
        ttk.Button(toolbar, text="Circle", command=self.draw_circle).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="Rectangle", command=self.draw_rectangle).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="Line", command=self.draw_line).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="Triangle", command=self.draw_triangle).pack(side=tk.LEFT, padx=2)
        
        ttk.Separator(toolbar, orient=tk.VERTICAL).pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=0)
        
        ttk.Button(toolbar, text="View Shapes", command=self.view_shapes).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="Modify", command=self.modify_shape).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="Delete", command=self.delete_shape).pack(side=tk.LEFT, padx=2)
        
        # Status frame
        status_frame = ttk.Frame(self.root)
        status_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=5)
        
        self.status_label = ttk.Label(status_frame, text="Status: Ready | Shapes: 0")
        self.status_label.pack(side=tk.LEFT)
        
    def setup_canvas(self):
        """Setup the drawing canvas"""
        # Canvas frame
        canvas_frame = ttk.Frame(self.root)
        canvas_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Canvas
        self.canvas = tk.Canvas(
            canvas_frame,
            bg='white',
            width=CANVAS_WIDTH,
            height=CANVAS_HEIGHT,
            relief=tk.SUNKEN,
            bd=2
        )
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<Button-1>", self.on_canvas_click)
        
        # Draw grid
        self.draw_grid()
        
    def draw_grid(self):
        """Draw grid on canvas"""
        grid_spacing = 50
        for i in range(0, CANVAS_WIDTH, grid_spacing):
            self.canvas.create_line(i, 0, i, CANVAS_HEIGHT, fill='lightgray', dash=(2, 2))
        for i in range(0, CANVAS_HEIGHT, grid_spacing):
            self.canvas.create_line(0, i, CANVAS_WIDTH, i, fill='lightgray', dash=(2, 2))
        
    def on_canvas_click(self, event):
        """Handle canvas click events"""
        # Check if clicked on a shape
        item = self.canvas.find_closest(event.x, event.y)
        if item:
            self.selected_shape = item[0]
            
    def draw_circle(self):
        """Draw circle dialog"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Draw Circle")
        dialog.geometry("300x200")
        
        ttk.Label(dialog, text="Center X:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        x_entry = ttk.Entry(dialog, width=20)
        x_entry.grid(row=0, column=1, padx=10, pady=5)
        
        ttk.Label(dialog, text="Center Y:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        y_entry = ttk.Entry(dialog, width=20)
        y_entry.grid(row=1, column=1, padx=10, pady=5)
        
        ttk.Label(dialog, text="Radius:").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
        r_entry = ttk.Entry(dialog, width=20)
        r_entry.grid(row=2, column=1, padx=10, pady=5)
        
        ttk.Label(dialog, text="Label:").grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
        label_entry = ttk.Entry(dialog, width=20)
        label_entry.grid(row=3, column=1, padx=10, pady=5)
        
        def add_circle():
            try:
                x = int(x_entry.get())
                y = int(y_entry.get())
                r = int(r_entry.get())
                label = label_entry.get() or "Circle"
                
                self.add_shape(CIRCLE, x, y, r, 0, 0, 0, label)
                dialog.destroy()
            except ValueError:
                messagebox.showerror("Error", "Please enter valid numbers")
        
        ttk.Button(dialog, text="Add Circle", command=add_circle).grid(row=4, column=0, columnspan=2, pady=20)
        
    def draw_rectangle(self):
        """Draw rectangle dialog"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Draw Rectangle")
        dialog.geometry("300x250")
        
        ttk.Label(dialog, text="Top-Left X:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        x1_entry = ttk.Entry(dialog, width=20)
        x1_entry.grid(row=0, column=1, padx=10, pady=5)
        
        ttk.Label(dialog, text="Top-Left Y:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        y1_entry = ttk.Entry(dialog, width=20)
        y1_entry.grid(row=1, column=1, padx=10, pady=5)
        
        ttk.Label(dialog, text="Bottom-Right X:").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
        x2_entry = ttk.Entry(dialog, width=20)
        x2_entry.grid(row=2, column=1, padx=10, pady=5)
        
        ttk.Label(dialog, text="Bottom-Right Y:").grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
        y2_entry = ttk.Entry(dialog, width=20)
        y2_entry.grid(row=3, column=1, padx=10, pady=5)
        
        ttk.Label(dialog, text="Label:").grid(row=4, column=0, sticky=tk.W, padx=10, pady=5)
        label_entry = ttk.Entry(dialog, width=20)
        label_entry.grid(row=4, column=1, padx=10, pady=5)
        
        def add_rectangle():
            try:
                x1 = int(x1_entry.get())
                y1 = int(y1_entry.get())
                x2 = int(x2_entry.get())
                y2 = int(y2_entry.get())
                label = label_entry.get() or "Rectangle"
                
                self.add_shape(RECTANGLE, x1, y1, x2, y2, 0, 0, label)
                dialog.destroy()
            except ValueError:
                messagebox.showerror("Error", "Please enter valid numbers")
        
        ttk.Button(dialog, text="Add Rectangle", command=add_rectangle).grid(row=5, column=0, columnspan=2, pady=20)
        
    def draw_line(self):
        """Draw line dialog"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Draw Line")
        dialog.geometry("300x250")
        
        ttk.Label(dialog, text="Start X:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        x1_entry = ttk.Entry(dialog, width=20)
        x1_entry.grid(row=0, column=1, padx=10, pady=5)
        
        ttk.Label(dialog, text="Start Y:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        y1_entry = ttk.Entry(dialog, width=20)
        y1_entry.grid(row=1, column=1, padx=10, pady=5)
        
        ttk.Label(dialog, text="End X:").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
        x2_entry = ttk.Entry(dialog, width=20)
        x2_entry.grid(row=2, column=1, padx=10, pady=5)
        
        ttk.Label(dialog, text="End Y:").grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
        y2_entry = ttk.Entry(dialog, width=20)
        y2_entry.grid(row=3, column=1, padx=10, pady=5)
        
        ttk.Label(dialog, text="Label:").grid(row=4, column=0, sticky=tk.W, padx=10, pady=5)
        label_entry = ttk.Entry(dialog, width=20)
        label_entry.grid(row=4, column=1, padx=10, pady=5)
        
        def add_line():
            try:
                x1 = int(x1_entry.get())
                y1 = int(y1_entry.get())
                x2 = int(x2_entry.get())
                y2 = int(y2_entry.get())
                label = label_entry.get() or "Line"
                
                self.add_shape(LINE, x1, y1, x2, y2, 0, 0, label)
                dialog.destroy()
            except ValueError:
                messagebox.showerror("Error", "Please enter valid numbers")
        
        ttk.Button(dialog, text="Add Line", command=add_line).grid(row=5, column=0, columnspan=2, pady=20)
        
    def draw_triangle(self):
        """Draw triangle dialog"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Draw Triangle")
        dialog.geometry("300x350")
        
        labels = [
            ("Vertex 1 X:", 0), ("Vertex 1 Y:", 1),
            ("Vertex 2 X:", 2), ("Vertex 2 Y:", 3),
            ("Vertex 3 X:", 4), ("Vertex 3 Y:", 5),
            ("Label:", 6)
        ]
        
        entries = {}
        for label, row in labels:
            ttk.Label(dialog, text=label).grid(row=row, column=0, sticky=tk.W, padx=10, pady=5)
            entry = ttk.Entry(dialog, width=20)
            entry.grid(row=row, column=1, padx=10, pady=5)
            entries[label] = entry
        
        def add_triangle():
            try:
                x1 = int(entries["Vertex 1 X:"].get())
                y1 = int(entries["Vertex 1 Y:"].get())
                x2 = int(entries["Vertex 2 X:"].get())
                y2 = int(entries["Vertex 2 Y:"].get())
                x3 = int(entries["Vertex 3 X:"].get())
                y3 = int(entries["Vertex 3 Y:"].get())
                label = entries["Label:"].get() or "Triangle"
                
                self.add_shape(TRIANGLE, x1, y1, x2, y2, x3, y3, label)
                dialog.destroy()
            except ValueError:
                messagebox.showerror("Error", "Please enter valid numbers")
        
        ttk.Button(dialog, text="Add Triangle", command=add_triangle).grid(row=7, column=0, columnspan=2, pady=20)
        
    def add_shape(self, shape_type, x1, y1, x2, y2, x3, y3, label):
        """Add a shape to the canvas"""
        shape = Shape(
            type=shape_type,
            x1=x1, y1=y1, x2=x2, y2=y2, x3=x3, y3=y3,
            label=label
        )
        
        # Draw on canvas
        if shape_type == CIRCLE:
            canvas_id = self.canvas.create_oval(
                x1-x2, y1-x2, x1+x2, y1+x2,
                outline='blue', width=2
            )
            self.canvas.create_text(x1, y1+x2+15, text=label, fill='blue')
        
        elif shape_type == RECTANGLE:
            canvas_id = self.canvas.create_rectangle(
                x1, y1, x2, y2,
                outline='red', width=2
            )
            self.canvas.create_text((x1+x2)//2, y1-15, text=label, fill='red')
        
        elif shape_type == LINE:
            canvas_id = self.canvas.create_line(
                x1, y1, x2, y2,
                fill='green', width=2
            )
            mid_x, mid_y = (x1+x2)//2, (y1+y2)//2
            self.canvas.create_text(mid_x+15, mid_y, text=label, fill='green')
        
        elif shape_type == TRIANGLE:
            canvas_id = self.canvas.create_polygon(
                x1, y1, x2, y2, x3, y3,
                outline='purple', fill='', width=2
            )
            mid_x = (x1+x2+x3)//3
            mid_y = (y1+y2+y3)//3
            self.canvas.create_text(mid_x, mid_y, text=label, fill='purple')
        
        shape.canvas_id = canvas_id
        self.shapes.append(shape)
        self.update_status()
        messagebox.showinfo("Success", f"{label} added successfully!")
        
    def view_shapes(self):
        """View all shapes"""
        if not self.shapes:
            messagebox.showinfo("Shapes", "No shapes on canvas")
            return
        
        info = "Shapes on Canvas:\n" + "="*50 + "\n"
        for i, shape in enumerate(self.shapes, 1):
            type_name = {CIRCLE: "Circle", RECTANGLE: "Rectangle", 
                        LINE: "Line", TRIANGLE: "Triangle"}[shape.type]
            info += f"\n{i}. {shape.label} ({type_name})\n"
            
            if shape.type == CIRCLE:
                info += f"   Center: ({shape.x1}, {shape.y1}), Radius: {shape.x2}\n"
            elif shape.type == RECTANGLE:
                info += f"   Corners: ({shape.x1}, {shape.y1}) to ({shape.x2}, {shape.y2})\n"
            elif shape.type == LINE:
                info += f"   Points: ({shape.x1}, {shape.y1}) to ({shape.x2}, {shape.y2})\n"
            elif shape.type == TRIANGLE:
                info += f"   Vertices: ({shape.x1}, {shape.y1}), ({shape.x2}, {shape.y2}), ({shape.x3}, {shape.y3})\n"
        
        messagebox.showinfo("All Shapes", info)
        
    def modify_shape(self):
        """Modify a shape"""
        if not self.shapes:
            messagebox.showinfo("Modify", "No shapes to modify")
            return
        
        # Show list and get selection
        shape_list = "\n".join(f"{i}. {s.label}" for i, s in enumerate(self.shapes, 1))
        choice = simpledialog.askinteger(
            "Modify Shape",
            f"Select shape ID to modify:\n{shape_list}",
            minvalue=1,
            maxvalue=len(self.shapes)
        )
        
        if choice is None:
            return
        
        shape = self.shapes[choice - 1]
        new_label = simpledialog.askstring("Modify", f"New label for {shape.label}:", initialvalue=shape.label)
        
        if new_label:
            shape.label = new_label
            self.canvas.delete(shape.canvas_id)
            # Redraw all shapes
            self.redraw_canvas()
            messagebox.showinfo("Success", "Shape modified!")
            
    def delete_shape(self):
        """Delete a shape"""
        if not self.shapes:
            messagebox.showinfo("Delete", "No shapes to delete")
            return
        
        shape_list = "\n".join(f"{i}. {s.label}" for i, s in enumerate(self.shapes, 1))
        choice = simpledialog.askinteger(
            "Delete Shape",
            f"Select shape ID to delete:\n{shape_list}",
            minvalue=1,
            maxvalue=len(self.shapes)
        )
        
        if choice is None:
            return
        
        if messagebox.askyesno("Confirm", f"Delete {self.shapes[choice-1].label}?"):
            self.canvas.delete(self.shapes[choice-1].canvas_id)
            del self.shapes[choice - 1]
            self.redraw_canvas()
            messagebox.showinfo("Success", "Shape deleted!")
            
    def redraw_canvas(self):
        """Redraw all shapes"""
        self.canvas.delete("all")
        self.draw_grid()
        
        for shape in self.shapes:
            if shape.type == CIRCLE:
                self.canvas.create_oval(
                    shape.x1-shape.x2, shape.y1-shape.x2, shape.x1+shape.x2, shape.y1+shape.x2,
                    outline='blue', width=2
                )
                self.canvas.create_text(shape.x1, shape.y1+shape.x2+15, text=shape.label, fill='blue')
            
            elif shape.type == RECTANGLE:
                self.canvas.create_rectangle(
                    shape.x1, shape.y1, shape.x2, shape.y2,
                    outline='red', width=2
                )
                self.canvas.create_text((shape.x1+shape.x2)//2, shape.y1-15, text=shape.label, fill='red')
            
            elif shape.type == LINE:
                self.canvas.create_line(
                    shape.x1, shape.y1, shape.x2, shape.y2,
                    fill='green', width=2
                )
                mid_x, mid_y = (shape.x1+shape.x2)//2, (shape.y1+shape.y2)//2
                self.canvas.create_text(mid_x+15, mid_y, text=shape.label, fill='green')
            
            elif shape.type == TRIANGLE:
                self.canvas.create_polygon(
                    shape.x1, shape.y1, shape.x2, shape.y2, shape.x3, shape.y3,
                    outline='purple', fill='', width=2
                )
                mid_x = (shape.x1+shape.x2+shape.x3)//3
                mid_y = (shape.y1+shape.y2+shape.y3)//3
                self.canvas.create_text(mid_x, mid_y, text=shape.label, fill='purple')
        
        self.update_status()
        
    def clear_canvas(self):
        """Clear all shapes"""
        if messagebox.askyesno("Confirm", "Clear entire canvas?"):
            self.canvas.delete("all")
            self.shapes.clear()
            self.draw_grid()
            self.update_status()
            messagebox.showinfo("Success", "Canvas cleared!")
            
    def update_status(self):
        """Update status bar"""
        self.status_label.config(text=f"Status: Ready | Shapes: {len(self.shapes)}")

def main():
    root = tk.Tk()
    app = GraphicsEditor(root)
    root.mainloop()

if __name__ == "__main__":
    main()
