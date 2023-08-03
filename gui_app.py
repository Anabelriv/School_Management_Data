import tkinter as tk
from main import connect_to_database
import table_actions

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


# Function to display student details in a new window
def show_student_details():
    query = "SELECT * FROM Students"
    students = connect_to_database(query, type="select")
    show_data_window("Student Details", students)


# Function to display staff details in a new window
def show_staff_info():
    query = "SELECT * FROM Staff"
    staff = connect_to_database(query, type="select")
    show_data_window("Staff Information", staff)


# Function to create and show a new window to display data
def show_data_window(title, data):
    new_window = tk.Toplevel(root)
    new_window.title(title)

    # Fetch the column names from the cursor's description
    headers = list(data[0].keys())

    # Create labels for headers
    for i, header in enumerate(headers):
        tk.Label(new_window, text=header).grid(row=0, column=i)

    # Populate data rows
    for row_index, row_data in enumerate(data):
        for col_index, col_key in enumerate(headers):
            tk.Label(new_window, text=row_data[col_key]).grid(
                row=row_index + 1, column=col_index
            )


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
tk.Button(root, text="Show Student Details", command=show_student_details).grid(
    row=10, column=0
)
tk.Button(root, text="Show Staff Info", command=show_staff_info).grid(row=10, column=1)

# ... (Add buttons for other functions)

root.mainloop()
