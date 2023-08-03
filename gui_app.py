# import tkinter as tk
# from tkinter import messagebox
# from main import connect_to_database

# # ... (All the functions defined in the original code)


# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()

#         self.title("Database Functions GUI")
#         self.geometry("500x400")

#         self.create_widgets()

#     def create_widgets(self):
#         # Label
#         self.label = tk.Label(self, text="Database Functions", font=("Helvetica", 16))
#         self.label.pack(pady=20)

#         # Buttons
#         self.add_staff_btn = self.create_button("Add Staff", self.add_staff)
#         self.add_student_btn = self.create_button("Add Student", self.add_student)
#         self.add_parent_btn = self.create_button("Add Parent", self.add_parent)
#         self.update_staff_shift_btn = self.create_button(
#             "Update Staff Shift", self.update_staff_shift
#         )
#         self.update_student_group_btn = self.create_button(
#             "Update Student Group", self.update_student_group
#         )
#         self.print_staff_info_btn = self.create_button(
#             "Print Staff Information", self.print_staff_info
#         )
#         self.print_student_details_btn = self.create_button(
#             "Print Student Details", self.print_student_details
#         )
#         self.print_student_parents_btn = self.create_button(
#             "Print Student Parents", self.print_student_parents
#         )

#         # Layout
#         self.add_staff_btn.pack()
#         self.add_student_btn.pack()
#         self.add_parent_btn.pack()
#         self.update_staff_shift_btn.pack()
#         self.update_student_group_btn.pack()
#         self.print_staff_info_btn.pack()
#         self.print_student_details_btn.pack()
#         self.print_student_parents_btn.pack()

#     def create_button(self, text, command):
#         return tk.Button(self, text=text, width=20, command=command)

#     def add_staff(self):
#         # Implement the GUI for
#         pass


import tkinter as tk
from main import connect_to_database
import table_actions

# ... (Your function definitions remain unchanged)

# Create the main GUI window
root = tk.Tk()
root.title("Database Functions GUI")


# Function to execute the add_staff function
def add_staff_click():
    staff_data = {
        "first_name": first_name_entry.get(),
        "last_name": last_name_entry.get(),
        "birth_date": birth_date_entry.get(),
        "phone_number": phone_number_entry.get(),
        "isInShift": True if shift_status_var.get() == 1 else False,
    }
    table_actions.add_staff(staff_data)


# Function to execute the add_student function
def add_student_click():
    student_data = {
        "first_name": first_name_entry.get(),
        "last_name": last_name_entry.get(),
        "birth_date": birth_date_entry.get(),
        "phone_number": phone_number_entry.get(),
        "isattend": True if attend_status_var.get() == 1 else False,
        "group_id": int(group_id_entry.get()),
        "building_id": int(building_id_entry.get()),
        "room_id": int(room_id_entry.get()),
    }
    table_actions.add_student(student_data)


# ... (Add similar functions for other buttons)

# Create labels and entry widgets
tk.Label(root, text="First Name:").grid(row=0, column=0)
first_name_entry = tk.Entry(root)
first_name_entry.grid(row=0, column=1)

tk.Label(root, text="Last Name:").grid(row=1, column=0)
last_name_entry = tk.Entry(root)
last_name_entry.grid(row=1, column=1)

tk.Label(root, text="Birth Date:").grid(row=2, column=0)
birth_date_entry = tk.Entry(root)
birth_date_entry.grid(row=2, column=1)

tk.Label(root, text="Phone Number:").grid(row=3, column=0)
phone_number_entry = tk.Entry(root)
phone_number_entry.grid(row=3, column=1)

shift_status_var = tk.IntVar()
tk.Checkbutton(root, text="Is in Shift", variable=shift_status_var).grid(
    row=4, column=1
)

attend_status_var = tk.IntVar()
tk.Checkbutton(root, text="Is Attend", variable=attend_status_var).grid(row=5, column=1)

tk.Label(root, text="Group ID:").grid(row=6, column=0)
group_id_entry = tk.Entry(root)
group_id_entry.grid(row=6, column=1)

tk.Label(root, text="Building ID:").grid(row=7, column=0)
building_id_entry = tk.Entry(root)
building_id_entry.grid(row=7, column=1)

tk.Label(root, text="Room ID:").grid(row=8, column=0)
room_id_entry = tk.Entry(root)
room_id_entry.grid(row=8, column=1)

# Create buttons to trigger the functions
tk.Button(root, text="Add Staff", command=add_staff_click).grid(row=9, column=0)
tk.Button(root, text="Add Student", command=add_student_click).grid(row=9, column=1)

# ... (Add buttons for other functions)

root.mainloop()
