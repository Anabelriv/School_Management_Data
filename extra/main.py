# This is a sample Python script.
import psycopg2


def connect_to_database(query, data=None, type="select"):
    # Connect to the database
    connection = None
    try:
        connection = psycopg2.connect(
            database="BoardingSchoolManagement",
            user="postgres",
            password="root",
            host="localhost",  # or IP address
            port="5432",
        )
        with connection:
            with connection.cursor() as cursor:  # it closes the transaction
                if data:
                    cursor.execute(query, data)
                else:
                    cursor.execute(query)
                if type == "select":
                    # Fetch the column names from the cursor's description
                    columns = [col[0] for col in cursor.description]

                    # Fetch all rows and convert each row to a dictionary
                    rows = [dict(zip(columns, row)) for row in cursor.fetchall()]

                    return rows
                else:
                    connection.commit()
    except Exception as e:
        print(e)
    finally:
        if connection != None:
            connection.close()  # need to specifically close the connection


# print(connect_to_database("Select * from parents"))
