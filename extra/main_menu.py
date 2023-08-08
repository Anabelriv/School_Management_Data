import tkinter as tk

from gui_app import add_staff_click, add_student_click


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(MainMenu)

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Set the window size to half the screen width and height
        width = int(screen_width / 2)
        height = int(screen_height / 2)

        # Set the geometry of the window
        self.geometry(f"{width}x{height}")

    def switch_frame(self, target_frame):
        new_frame = target_frame(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class MainMenu(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Main Menu").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Add a Student",
                  command=lambda: master.switch_frame(AddStudent)).pack()
        tk.Button(self, text="Add a Group",
                  command=lambda: master.switch_frame(AddGroup)).pack()
        tk.Button(self, text="Add a Staff Member",
                  command=lambda: master.switch_frame(AddStaffMember)).pack()
        tk.Button(self, text="View All Groups",
                  command=lambda: master.switch_frame(ViewAllGroups)).pack()

class AddStudent(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Add a Student Page").pack(side="top", fill="x", pady=10)
        tk.Label(self, text="First Name:").pack()
        first_name_entry = tk.Entry(self)
        first_name_entry.pack()
        # last_name_entry = tk.Entry(self)
        # last_name_entry.pack()
        # first_name_entry.insert(0, "Enter First Name")
        # last_name_entry = tk.Entry(self)
        # last_name_entry.pack()
        # birth_date_entry = tk.Entry(self)
        # birth_date_entry.pack()
        # phone_number_entry = tk.Entry(self)
        # phone_number_entry.pack()
        tk.Button(self, text="Add Student", command=add_student_click).pack()
        tk.Button(self, text="Return to Main Menu",
                  command=lambda: master.switch_frame(MainMenu)).pack()

class AddGroup(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Add a Student Page").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to Main Menu",
                  command=lambda: master.switch_frame(MainMenu)).pack()
    pass

class AddStaffMember(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Add a Student Page").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to Main Menu",
                  command=lambda: master.switch_frame(MainMenu)).pack()
    pass

class ViewAllGroups(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Add a Student Page").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to Main Menu",
                  command=lambda: master.switch_frame(MainMenu)).pack()
    pass

if __name__ == "__main__":
    app = App()
    app.mainloop()
