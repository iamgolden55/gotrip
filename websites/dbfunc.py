from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError

# Create a SQLAlchemy engine that will connect to your MySQL database
engine = create_engine('mysql+mysqlconnector://root:alpha12345@localhost:3306/world_hotels')

def load_hotels_from_db():
    # Define your SQL query
    SELECT_statement = text("""
    SELECT h.hotel_name, h.location, c.city_name, r.room_type, r.room_capacity, r.room_price, r.room_id
    FROM hotel_db h
    JOIN city_db c ON h.city_id = c.city_id
    JOIN room_db r ON h.room_id = r.room_id
    """)

    try:
        # Connect to the database and execute the query
        with engine.connect() as connection:
            result = connection.execute(SELECT_statement)
            rows = result.fetchall()
            return rows
    except OperationalError:
        print('DB connection error')
        return []
   
def load_user_from_db():
   with engine.connect() as conn:
    # Execute your query
    result = conn.execute(text("select * from user_db"))

    # Initialize an empty list to store your data
    users = []

    # Iterate over the result set and add each row to the list as a dictionary
    for row in result:
        users.append(dict(row._mapping))

    # Now data_list contains all rows as dictionaries
    return users
   