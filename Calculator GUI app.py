"""
Now try to build a Calculator GUI app using Python. For Python, it should use tkinter, just like Rock Paper Scissors.
It should have:

Buttons for 0-9 digits.
Buttons for +, -, ×, ÷.
Button for =.
also add reset button to clear the input.

"""
import tkinter as tk
from tkinter import messagebox


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        # Store the current expression shown on the display
        self.expression = ""

        # Display field (Entry) configured for right alignment
        self.display = tk.Entry(
            root, font=("Arial", 24), borderwidth=2, relief="ridge", justify="right"
        )
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # Button layout: digits, operators, equals, and reset
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("÷", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("×", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), ("=", 4, 1), ("+", 4, 2), ("Reset", 4, 3),
        ]

        # Create and place each button in the grid
        for (text, row, col) in buttons:
            button = tk.Button(
                root,
                text=text,
                font=("Arial", 18),
                command=lambda t=text: self.on_button_click(t),  # Pass button text to handler
            )
            button.grid(row=row, column=col, sticky="nsew")

        # Make rows/columns expand to fill window
        for i in range(5):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):
        # Clear the display and expression when Reset (or legacy C) is pressed
        if char in {"Reset", "C"}:
            self.expression = ""
            self.display.delete(0, tk.END)
            return

        # Evaluate the current expression when = is pressed
        if char == "=":
            try:
                result = self.evaluate_expression(self.expression)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
                # Keep the result for further calculations
                self.expression = str(result)
            except Exception:
                messagebox.showerror("Error", "Invalid Expression")
                self.expression = ""
                self.display.delete(0, tk.END)
            return

        # Translate display operators to Python operators
        if char in "÷×-+":
            char = {"÷": "/", "×": "*", "-": "-", "+": "+"}[char]

        # Append the character and update the display
        self.expression += char
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

    def evaluate_expression(self, expr):
        # WARNING: eval is used for simplicity here. Avoid eval on untrusted input.
        return eval(expr)


if __name__ == "__main__":
        # Create the main window and run the app
        root = tk.Tk()
        app = CalculatorApp(root)
        root.mainloop()





