import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
import os
import random
from datetime import date

# Load environment variables from the .env file
load_dotenv()

# DatabaseService Class
class DatabaseService:
    def __init__(self):
        self.db_user = os.getenv("POSTGRES_USER")
        self.db_password = os.getenv("POSTGRES_PASSWORD")
        self.db_name = os.getenv("POSTGRES_DB")
        self.db_host = os.getenv("POSTGRES_HOST")
        self.db_port = os.getenv("POSTGRES_PORT")

    def _get_connection(self):
        """
        Open a new database connection.
        """
        connection = psycopg2.connect(
            dbname=self.db_name,
            user=self.db_user,
            password=self.db_password,
            host=self.db_host,
            port=self.db_port,
            cursor_factory=RealDictCursor,
        )
        connection.autocommit = True
        return connection

    def create_table(self):
        """
        Create a table in the database if it doesn't exist.
        """
        query = """
        CREATE TABLE IF NOT EXISTS public."Table1" (
            id SERIAL PRIMARY KEY,
            c_text TEXT,
            c_double DOUBLE PRECISION
        );
        """
        with self._get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                print("Table 'Table1' created successfully.")

    def create_record(self, c_text, c_double):
        """
        Insert a new record into the Table1 table.
        """
        query = """
        INSERT INTO public."Table1" (c_text, c_double)
        VALUES (%s, %s) RETURNING id;
        """
        with self._get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (c_text, c_double))
                record_id = cursor.fetchone()["id"]
                print(f"Record created with ID: {record_id}")
                return record_id

    def read_records(self):
        """
        Retrieve all records from the Table1 table.
        """
        query = 'SELECT * FROM public."Table1";'
        with self._get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                records = cursor.fetchall()
                print("Records retrieved successfully.")
                return records

    def update_record(self, record_id, c_text=None, c_double=None):
        """
        Update a record in the Table1 table.
        """
        query = """
        UPDATE public."Table1"
        SET c_text = COALESCE(%s, c_text),
            c_double = COALESCE(%s, c_double)
        WHERE id = %s RETURNING id;
        """
        with self._get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (c_text, c_double, record_id))
                updated_id = cursor.fetchone()
                if updated_id:
                    print(f"Record with ID {record_id} updated successfully.")
                    return updated_id
                else:
                    print(f"Record with ID {record_id} not found.")
                    return None

    def delete_record(self, record_id):
        """
        Delete a record from the Table1 table.
        """
        query = 'DELETE FROM public."Table1" WHERE id = %s RETURNING id;'
        with self._get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (record_id,))
                deleted_id = cursor.fetchone()
                if deleted_id:
                    print(f"Record with ID {record_id} deleted successfully.")
                    return deleted_id
                else:
                    print(f"Record with ID {record_id} not found.")
                    return None
                
    # --------------------Vector table create-------------------------
    def create_vector_table(self):
        """
        Create a table named 'vector_table' with the specified schema.
        """
        query = """
        CREATE TABLE IF NOT EXISTS public."vector_table" (
            id SERIAL PRIMARY KEY,
            date DATE NOT NULL,
            age INTEGER NOT NULL,
            vector FLOAT[]
        );
        """
        with self._get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                print("Table 'vector_table' created successfully.")

    def create_vector_record(self, age):
        """
        create a new record into the 'vector_table' with a random 2D vector.
        """
        # Generate a random 2D vector
        random_vector = [round(random.uniform(0, 100), 2), round(random.uniform(0, 100), 2)]
        today_date = date.today()

        query = """
        INSERT INTO public."vector_table" (date, age, vector)
        VALUES (%s, %s, %s) RETURNING id;
        """
        with self._get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (today_date, age, random_vector))
                record_id = cursor.fetchone()["id"]
                print(f"Record inserted with ID: {record_id}, vector: {random_vector}")
                return record_id
            
    def read_vector_records(self):
        """
        Retrieve all records from the vector table.
        """
        query = 'SELECT * FROM public."vector_table";'
        with self._get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                records = cursor.fetchall()
                print("Records retrieved successfully.")
                return records

    def update_vector_record(self, record_id, date=None, age=None, vector=None):
        query = """
        UPDATE public."vector_table"
        SET date = COALESCE(%s, date),
            age = COALESCE(%s, age),
            vector = COALESCE(%s, vector)
        WHERE id = %s RETURNING id;
        """
        with self._get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (date, age, vector, record_id))
                updated_id = cursor.fetchone()
                if updated_id:
                    print(f"Record with ID {record_id} updated successfully.")
                    return updated_id
                else:
                    print(f"Record with ID {record_id} not found.")
                    return None

    def delete_vector_record(self, record_id):
        """
        Delete a record from the vector_table.
        """
        query = 'DELETE FROM public."vector_table" WHERE id = %s RETURNING id;'
        with self._get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (record_id,))
                deleted_id = cursor.fetchone()
                if deleted_id:
                    print(f"Record with ID {record_id} deleted successfully from vector_table.")
                    return deleted_id
                else:
                    print(f"Record with ID {record_id} not found in vector_table.")
                    return None



# # # Main script to test CRUD operations
if __name__ == "__main__":
    service = DatabaseService()

#     # Step 1: Create the table
    # service.create_table()

    # Step 2: Create a new record
    # record_id = service.create_record("Sample Text", 123.45)

    # Step 3: Read all records
    # records = service.read_records()
    # print(f"Records: {records}")

    # Step 4: Update the created record
    # service.update_record(record_id, c_text="Updated Text", c_double=678.90)

    # Step 5: Read all records again
    # records = service.read_records()
    # print(f"Updated Records: {records}")

    # Step 6: Delete the created record
    # service.delete_record(record_id)

    # Step 7: Verify the deletion
    # records = service.read_records()
    # print(f"Records after deletion: {records}")

# -----------------For vector table-----------------
    #create table
    # service.create_vector_table()

    # insert new record
    # record_id = service.create_vector_record(65)

    #read record
    # records = service.read_vector_records()
    # print(f"Records: {records}")

    #update records
    # service.update_vector_record(record_id=1,
    #         age=20,
    #     )

    # Delete records from vector_table
    record_id = 2
    deleted_id = service.delete_vector_record(record_id)

    if deleted_id:
        print(f"Record with ID {deleted_id['id']} was deleted successfully.")
    else:
        print(f"Record with ID {record_id} not found in vector_table.")


