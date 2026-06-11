# --- Simple Calculator ---

import tkinter as tk

# _________________________________________________________________________________________________

# This function handles button clicks 
def click(value):
    current = entry.get()
    entry.delete(0,tk.END)
    entry.insert(0, current + str(value))

# _________________________________________________________________________________________________

# This function will calculate the result 
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))

    except:
        entry.delete(0, tk.END)
        entry.insert(0, 'Error')
        
# _________________________________________________________________________________________________

# This fuction will clear the display 
def clear():
    entry.delete(0,tk.END)
    
# _________________________________________________________________________________________________

# Create the main window

window = tk.Tk()
window.title('Calculator')
window.geometry('320x450')
window.configure(bg = 'black')

# Display the calculator

entry = tk.Entry(
                window, 
                font=('Arial', 24),
                justify='right',
                bg='black',
                fg='white',
                insertbackground='white'
                )

entry.pack(
            fill='both',
            padx=10,
            pady=10,
            ipadx=10
            )

# Button layout
buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]

for row in buttons:
    frame = tk.Frame(window,bg='black')
    frame.pack(expand=True, fill='both')
    
    for button in row:
        
        if button == '=':
            cmd = calculate
            bg_color = "#1E90FF"
            
        elif button in ['+', '-', '*', '/']:
            cmd = lambda b=button: click(b)
            bg_color = "#1E90FF"
            
        else:
            cmd = lambda b=button: click(b)
            bg_color= "#333333" 
            
        tk.Button(
                    frame,
                    text=button,
                    font=('Arial', 18, 'bold'),
                    bg=bg_color,
                    fg='white',
                    activebackground=bg_color,
                    activeforeground='white',
                    bd=0,
                    command=cmd
                    ).pack(side='left', expand=True, fill='both', padx=2, pady=2)

# Clear the display button 
tk.Button(
            window,
            text="CLEAR",
            font=('Arial', 18, 'bold'),
            bg="#00C853",
            fg='white',
            activebackground="#00A844",
            activeforeground='white',
            bd=0,
            command=clear,
).pack(fill="both", padx=10, pady=10)

# Start the Gui application
window.mainloop()

