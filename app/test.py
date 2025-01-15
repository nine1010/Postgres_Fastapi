from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Verify the loaded variables
print("PostgreSQL Config:")
print(f"Host: {os.getenv('POSTGRES_HOST')}")
print(f"Port: {os.getenv('POSTGRES_PORT')}")
print(f"User: {os.getenv('POSTGRES_USER')}")
print(f"Database: {os.getenv('POSTGRES_DB')}")