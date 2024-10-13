import tkinter as tk
from tkinter import ttk

SELECTED_KEYS = {}

# Define your parameters dictionary
parameters = {
    "accessories": ["0", "1"],
    "age": ["18-25", "26-36", "37-75"],
    "gender": ["male", "female"],
    "irregularities": ["0", "1"],
    "skinColor": ["dark", "fair", "medium", "very_fair"]
}

# Create the main application window
root = tk.Tk()
root.title("Parameter Selection")

# Create a frame to hold the checkbuttons and entry fields
frame = ttk.Frame(root)
frame.pack(padx=10, pady=10)

# Create a dictionary to store the selected options
selected_options = {}

# Create checkbuttons and entry fields for each parameter and its arguments
for parameter, arguments in parameters.items():
    # Create a label for the parameter
    ttk.Label(frame, text=parameter).pack(side="top", pady=(0, 5))

    # Create a frame to hold the checkbuttons for the arguments
    arg_frame = ttk.Frame(frame)
    arg_frame.pack(side="top")

    # Create a dictionary to store the BooleanVar objects for each argument
    arg_vars = {}

    # Create checkbuttons for each argument
    for i, argument in enumerate(arguments):
        var = tk.BooleanVar()
        checkbutton = ttk.Checkbutton(arg_frame, text=argument, variable=var, onvalue=True, offvalue=False)
        checkbutton.pack(side="left", padx=(0, 5))

        # Store the variable in the arg_vars dictionary
        arg_vars[argument] = var

    # Create an entry field for the quantity
    quantity_var = tk.StringVar()
    quantity_entry = ttk.Entry(frame, textvariable=quantity_var)
    quantity_entry.pack(side="top", pady=(5, 0))

    # Store the arg_vars dictionary and quantity_var in the selected_options dictionary
    selected_options[parameter] = {"args": arg_vars, "quantity": quantity_var}

# Create a button to print the selected options
def print_selected_options():
    global SELECTED_KEYS, selected_options
    sel = {}
    for parameter, options in selected_options.items():
        selected = [argument for argument, var in options["args"].items() if var.get()]
        if selected:
            quantity = options["quantity"].get()
            # print(f"{parameter}: {', '.join(selected)}, Quantity: {quantity}")
            sel[parameter] = {"values": selected, "quantity": quantity}
    print(sel)
    SELECTED_KEYS = sel

ttk.Button(root, text="SET Selected Options", command=print_selected_options).pack(pady=(10, 0))

root.mainloop()