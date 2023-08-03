from main import connect_to_database


# General Functions to save, update, delete with database
# Function to insert data into a table
def insert_data(table_name, data):  # tested it works
    query = f"INSERT INTO {table_name} ({', '.join(data.keys())}) VALUES ({', '.join(['%s'] * len(data))})"
    connect_to_database(query, tuple(data.values()), type="insert")


# Function to delete a record from a table
def delete_data(table_name, primary_key, value):
    query = f"DELETE FROM {table_name} WHERE {primary_key} = %s"
    connect_to_database(query, (value,), type="delete")


# Function to add staff
def add_staff(staff_data):  # tested it works
    insert_data("Staff", staff_data)


# Function to add students
def add_student(student_data):  # tested it works
    insert_data("Students", student_data)


# Function to add parents # tested it works
def add_parent(parent_data):
    insert_data("Parents", parent_data)


# Function to delete staff
def delete_staff(staff_id):
    delete_data("Staff", "Staff_id", staff_id)


# Function to delete student
def delete_student(student_id):
    delete_data("Students", "Student_ID", student_id)


# Function to delete parent
def delete_parent(parent_id):
    delete_data("Parents", "Parent_ID", parent_id)


# Function to update student attendance
def update_student_attendance(student_id, is_attend):
    query = "UPDATE Students SET isAttend = %s WHERE student_ID = %s"
    connect_to_database(query, (is_attend, student_id), type="update")


# Function to update group of a student
def update_student_group(student_id, group_id):
    query = "UPDATE Students SET Group_id = %s WHERE student_ID = %s"
    connect_to_database(query, (group_id, student_id), type="update")


# Function to update staff's shift status
def update_staff_shift(staff_id, is_in_shift):
    query = "UPDATE Staff SET isInShift = %s WHERE Staff_id = %s"
    connect_to_database(query, (is_in_shift, staff_id), type="update")


# Function to update staff's role (supervisor)
def update_staff_role(staff_id, role_id):
    query = "UPDATE staff SET role_ID = %s WHERE staff_id = %s"
    connect_to_database(query, (role_id, staff_id), type="update")


# Function to update responsible staff for a hobby
def update_hobby_responsible_staff(hobby_id, staff_id):
    query = "UPDATE hobbies SET responsible_staff_id = %s WHERE hobbies_ID = %s"
    connect_to_database(query, (staff_id, hobby_id), type="update")


# Function to update staff members of a group
def update_group_staff(group_id, staff_member_1, staff_member_2):
    query = "UPDATE group_staff SET group_staff_Member_1 = %s, group_staff_Member_2 = %s WHERE Group_ID = %s"
    connect_to_database(
        query, (staff_member_1, staff_member_2, group_id), type="update"
    )


# Function to print student details
def print_student_details():
    query = "SELECT * FROM Students"
    students = connect_to_database(query, type="select")
    for student in students:
        print(student)


# Function to print student parents
def print_student_parents():
    query = "SELECT * FROM Parents INNER JOIN Student_parents ON Parents.parent_id = Student_parents.parent_ID"
    student_parents = connect_to_database(query, type="select")
    for parent in student_parents:
        print(parent)


# Function to print staff information
def print_staff_info():
    query = "SELECT * FROM Staff"
    staff = connect_to_database(query, type="select")
    for staff_member in staff:
        print(staff_member)


# Function to print groups
def print_groups():
    query = "SELECT * FROM Group"
    groups = connect_to_database(query, type="select")
    for group in groups:
        print(group)


# Function to print hobbies
def print_hobbies():
    query = "SELECT * FROM Hobbies"
    hobbies = connect_to_database(query, type="select")
    for hobby in hobbies:
        print(hobby)


# _______ TEST ________

# staff_data_1 = {
#     "first_name": "John",
#     "last_name": "Simpson",
#     "birth_date": "1980-03-03",
#     "phone_number": "123456789",
#     "isInShift": True,
# }

# student_data_1 = {
#     "first_name": "Alice",
#     "last_name": "Clarkson",
#     "birth_date": "1999-02-03",
#     "phone_number": "23456789",
#     "isattend": True,
#     "group_id": 1,
#     "building_id": 1,
#     "room_id": 2,
# }

# parent_data_1 = {
#     "first_name": "John",
#     "last_name": "Brooklin",
#     "phone_number": "123-456-7890",
#     "address": "122 Main Road",
# }


# # Add staff data

# add_staff(staff_data_1)

# # Add student data
# add_student(student_data_1)


# # # Add parent data
# add_parent(parent_data_1)


# # Print staff information
print_staff_info()

# # Print student details
# print_student_details()

# # # Print student parents
# print_student_parents()

# # Update staff shift status # tested it works
# update_staff_shift(1, True)

# # # Update student group # tested it works
# update_student_group(16, 2)

# # Print updated staff information
# print_staff_info()

# # Print updated student details
# print_student_details()

# delete_parent(4)
