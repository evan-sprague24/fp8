import sqlite3
import tkinter as tk
from tkinter import messagebox, simpledialog

# Create a connection to the database
conn = sqlite3.connect('user_feedback.db')

# Create a cursor
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    feedback TEXT NOT NULL
)
''')
conn.commit()

# Function to insert data into the database
def submit_feedback():
    name = entry_name.get()
    email = entry_email.get()
    feedback = text_feedback.get("1.0", tk.END).strip()

    if name and email and feedback:
        cursor.execute('INSERT INTO feedback (name, email, feedback) VALUES (?, ?, ?)', (name, email, feedback))
        conn.commit()
        messagebox.showinfo("Success", "Feedback submitted successfully!")
        entry_name.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        text_feedback.delete("1.0", tk.END)
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields.")

# Function to retrieve and print all feedback from the database
def print_feedback():
    # Ask for the password
    password = simpledialog.askstring("Password", "Enter the password to view feedback:", show='*')
    
    if password == "Evan":  # Replace with your desired password
        cursor.execute('SELECT * FROM feedback')
        records = cursor.fetchall()
        
        if records:
            for record in records:
                print(f"ID: {record[0]}, Name: {record[1]}, Email: {record[2]}, Feedback: {record[3]}")
        else:
            print("No feedback available.")
    else:
        messagebox.showwarning("Access Denied", "Incorrect password!")
# Create the GUI
app = tk.Tk()
app.title("User Feedback Form")

# Name label and entry
label_name = tk.Label(app, text="Name:")
label_name.pack()
entry_name = tk.Entry(app)
entry_name.pack()

# Email label and entry
label_email = tk.Label(app, text="Email:")
label_email.pack()
entry_email = tk.Entry(app)
entry_email.pack()

# Feedback label and text area
label_feedback = tk.Label(app, text="Feedback:")
label_feedback.pack()
text_feedback = tk.Text(app, height=10, width=40)
text_feedback.pack()

# Submit button
button_submit = tk.Button(app, text="Submit", command=submit_feedback)
button_submit.pack()


# Print button
button_print = tk.Button(app, text="Print All Feedback", command=print_feedback)
button_print.pack()

# Run the application
app.mainloop()

# Close the connection when done (optional)
conn.close()