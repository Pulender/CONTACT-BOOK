import tkinter as tk
from tkinter import messagebox

# Initialize the list to store contacts
contacts = []

def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()
    
    if name and phone:
        contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
        messagebox.showinfo("Success", "Contact added successfully!")
        entry_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_address.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Name and phone number are required.")

def view_contacts():
    contacts_list.delete(0, tk.END)
    for contact in contacts:
        contacts_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def search_contact():
    search = entry_search.get()
    contacts_list.delete(0, tk.END)
    results = [contact for contact in contacts if search in contact['name'] or search in contact['phone']]
    if results:
        for contact in results:
            contacts_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")
    else:
        messagebox.showinfo("No Results", "No contacts found.")

def update_contact():
    search = entry_search.get()
    for contact in contacts:
        if search == contact['name'] or search == contact['phone']:
            contact['name'] = entry_name.get()
            contact['phone'] = entry_phone.get()
            contact['email'] = entry_email.get()
            contact['address'] = entry_address.get()
            messagebox.showinfo("Success", "Contact updated successfully!")
            return
    messagebox.showwarning("Update Error", "Contact not found.")

def delete_contact():
    search = entry_search.get()
    for contact in contacts:
        if search == contact['name'] or search == contact['phone']:
            contacts.remove(contact)
            messagebox.showinfo("Success", "Contact deleted successfully!")
            return
    messagebox.showwarning("Delete Error", "Contact not found.")

# Create the main application window
root = tk.Tk()
root.title("Contact Management System")

# Create input fields and labels
tk.Label(root, text="Name:").grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Phone:").grid(row=1, column=0, padx=5, pady=5)
entry_phone = tk.Entry(root)
entry_phone.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Email:").grid(row=2, column=0, padx=5, pady=5)
entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Address:").grid(row=3, column=0, padx=5, pady=5)
entry_address = tk.Entry(root)
entry_address.grid(row=3, column=1, padx=5, pady=5)

# Create buttons for each operation
tk.Button(root, text="Add Contact", command=add_contact).grid(row=4, column=0, columnspan=2, padx=5, pady=5)
tk.Button(root, text="View Contacts", command=view_contacts).grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Create listbox to display contacts
contacts_list = tk.Listbox(root, width=50)
contacts_list.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

# Create search functionality
tk.Label(root, text="Search:").grid(row=7, column=0, padx=5, pady=5)
entry_search = tk.Entry(root)
entry_search.grid(row=7, column=1, padx=5, pady=5)
tk.Button(root, text="Search", command=search_contact).grid(row=8, column=0, columnspan=2, padx=5, pady=5)

# Create update and delete buttons
tk.Button(root, text="Update Contact", command=update_contact).grid(row=9, column=0, columnspan=2, padx=5, pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact).grid(row=10, column=0, columnspan=2, padx=5, pady=5)

# Run the application
root.mainloop()
