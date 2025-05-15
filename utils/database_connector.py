# services/database_connector.py
from django.db import connection

def connect_db():
    """Fetches data from the database using Django's connection."""
    show_table_query = "SELECT * FROM `survey_results` WHERE is_checked=1"
    names_query = "DESCRIBE survey_results"
    
    with connection.cursor() as cursor:
        cursor.execute(show_table_query)
        result = cursor.fetchall()
        
        cursor.execute(names_query)
        names = cursor.fetchall()
    
    return result, names
