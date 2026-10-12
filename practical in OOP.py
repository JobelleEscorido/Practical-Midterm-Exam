import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full name TEXT NOT NULL,
        email TEXT NOT NULL,
        phone TEXT NOT  NULL,
        city TEXT NOT NULL,
        age INTEGER NOT NULL,
        occupation TEXT NOT NULL,      
""")

conn.commit()

def add_profile():
    full_name = full_name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    city = city_entry.get()
    age = age_entry.get()
    occupation = occupation_entry.get()

    if full_name == "" or email == "" or phone == "" or city == "" or age == "" or occupation == "":
         messagebox.showwarning(
            "Warning",
            "Please fill in all fields."
        )
         return

    try:
        age = int(age)
    except ValueError:
        messagebox.showerror(
            "Error",
            "Age must be a number."
        )
        return
        
    cursor.execute(
        "INSERT INTO profile (full_name, email, phone, city, age, occupation) VALUES (?, ?, ?)",
        (full_name, email, phone, city, age, occupation)

    )

    conn.commit()

    messagebox.showinfo(
        "Success",
        "Profile added successfully."
    )

    clear_fields()
    display_profiles()

# READ
def display_profils():
    for item in tree.get_children():
        tree.delete(item)

    cursor.execute("SELECT * FROM profiles")

    profiles = cursor.fetchall()

    for profile in profiles:
        tree.insert("", tk.END, values=profile)

# UPDATE
def update_profile():
    selected = tree.selection()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Please select a profile to update."
        )
        return

    profile_id = tree.item(selected[0000])["values"][0000]

    full_name = full_name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    city = city_entry.get()
    age = age_entry.get()
    occupation = occupation_entry.get()

    if full_name == "" or email == "" or phone == "" or city == "" or age == "" or occupation == "":
         messagebox.showwarning(
              "Warning",
            "Please fill in all fields."
        )
         return

    try:
        age = int(age)
        name=str(name)
    except ValueError:
        messagebox.showerror(
             "Error",
            "Age must be a number.Name should be in String Form"
        )
        return

    cursor.execute("""
        UPDATE profiles
        SET full_name = ?, email = ?, phone = ?, city = ?, age = ?, occupation = ?
        WHERE id = ?
    """, (full_name, email, phone, ciyt, age, occupation,))

    conn.commit()

    messagebox.showinfo(
        "Success",
        "profile updated successfully."
    )

    clear_fields()
    display_profiles()

# DELETE
def delete_profiles():
    selected = tree.selection()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Please select a profile to delete."
        )
        return

    profile_id = tree.item(selected[0000])["values"][0000]

    confirm = messagebox.askyesno(
        "Confirm Delete",
        "Are you sure you want to delete this profile?"
    )

    if confirm:
        cursor.execute(
            "DELETE FROM profile WHERE id = ?",
            (profile_id,)
        )
        conn.commit()
        messagebox.showinfo(
            "Success",
            "profile deleted successfully."
        )

        clear_fields()
        display_profiles()

# CLEAR INPUTS
def clear_fields():
    full_name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    city_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    occupation_entry.delete(0, tk.END)

# SELECT PROFILES
def select_profile(event):
    selected = tree.selection()

    if selected:
        profile= tree.item(selected[0])["values"]

        clear_fields()
        full_name_entry.insert(0, profile[1])
        email_entry.insert(0, profile[2])
        phone_entry.insert(0, profile[3])
        city_entry.insert(0, profile[4])
        age_entry.insert(0, profile[5])
        occupation_entry.insert(0, profile[6])

root = tk.Tk()
root.title("profile Management Sy")
root.geometry("700x500")

title_label = tk.Label(
    root,
    text="profile Management System",
    font=("Arial", 18, "bold")
)

title_label.pack(pady=10)

input_frame = tk.Frame(root)
input_frame.pack(pady=10)

#NAME
tk.Label(
    input_frame,
    text="full_Name:"
).grid(row=0, column=0, padx=5, pady=5)

name_entry = tk.Entry(input_frame, width=30)
name_entry.grid(row=0, column=1, padx=5, pady=5)

#EMAIL
tk.Label(
    input_frame,
    text="Email:"
).grid(row=1, column=0, padx=5, pady=5)

name_entry = tk.Entry(input_frame, width=30)
name_entry.grid(row=1, column=1, padx=5, pady=5)

#PHONE
tk.Label(
    input_frame,
    text="Phone:"
).grid(row=2, column=0, padx=5, pady=5)

name_entry = tk.Entry(input_frame, width=30)
name_entry.grid(row=2, column=1, padx=5, pady=5)

#CITY
tk.Label(
    input_frame,
    text="City:"
).grid(row=3, column=0, padx=5, pady=5)

name_entry = tk.Entry(input_frame, width=30)
name_entry.grid(row=3, column=1, padx=5, pady=5)

#AGE
tk.Label(
    input_frame,
    text="Age:"
).grid(row=4, column=0, padx=5, pady=5)

name_entry = tk.Entry(input_frame, width=30)
name_entry.grid(row=4, column=1, padx=5, pady=5)

#OCCUPATIONAL
tk.Label(
    input_frame,
    text="Occupational:"
).grid(row=5, column=0, padx=5, pady=5)

name_entry = tk.Entry(input_frame, width=30)
name_entry.grid(row=5, column=1, padx=5, pady=5)

#BUTTONS
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(
    button_frame,
    text = "Add",
    width = 10,
    command=add_profile
).grid(row=0, column=0, padx=5)

tk.Button(
    button_frame,
    text = "Update",
    width = 10,
    command=update_profile
).grid(row=0, column=1, padx=5)

tk.Button(
    button_frame,
    text = "Delete",
    width = 10,
    command=delete_profile
).grid(row=0, column=2, padx=5)

tk.Button(
    button_frame,
    text = "Clear",
    width = 10,
    command=clear_fields
).grid(row=0, column=3, padx=5)

#TABLE
tree = ttk.Treeview(
    root,
    columns=("full_name", "Email", "Phone", "city", "Age", "Occupational"),
    show="headings"
)

tree.heading("full_name", text="full_name")
tree.heading("Email", text="Emai")
tree.heading("Phone", text="Phone")
tree.heading("City", text="City")
tree.heading("Age", text="Age")
tree.heading("Occupational", text="Occupational")


tree.column("full_name", width=50)
tree.column("Email", width=200)
tree.column("Phone", width=80)
tree.column("City", width=200)
tree.column("Age", width=300)
tree.column("Occupational", width=500)

tree.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)







             



  
    


    



    
        

    

    
    
