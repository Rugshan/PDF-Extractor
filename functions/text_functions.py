import tkinter as tk


# Copy Text
def copy_text(root, content):
    root.clipboard_clear()
    root.clipboard_append(content[-1])


# Display Textbox
def display_textbox(content, row, column, root):
    text_box = tk.Text(root, height=8, width=30, padx=10, pady=10)
    text_box.insert(1.0, content)
    text_box.tag_config("center", justify="center")
    text_box.tag_add("center", 1.0, "end")
    text_box.grid(column=column, row=row, sticky="SW", padx=25, pady=25)
