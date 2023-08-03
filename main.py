# This is a sample Python script.
import psycopg2

def connect_to_database():
    try:
        connection = psycopg2.connect(
            host='localhost',   # or your server's address
            database='BoardingSchoolManagement',
            user='postgres',
            password='password'
        )

        # Create a cursor object
        cursor = connection.cursor()

        # Execute SQL queries as needed
        cursor.execute("""SELECT
    s.First_name,
    s.Last_name,
    sg.Group_name
FROM
    Students s
JOIN
    StudentGroup sg ON s.Group_id = sg.group_ID
WHERE
    sg.group_ID = 1; -- Replace with the desired group ID""")

        # Fetch the result
        result = cursor.fetchall()
        print(f'Connected to: {result}')

        # Close the cursor and connection
        cursor.close()
        connection.close()

    except Exception as error:
        print(f'An error occurred: {error}')

# Call the function to connect to the database
connect_to_database()
