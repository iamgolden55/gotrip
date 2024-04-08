from sqlalchemy import create_engine, text

# Your database connection string
engine = create_engine('mysql+mysqlconnector://root:alpha12345@localhost:3306/world_hotels')

def load_hotels_from_db():
   with engine.connect() as conn:
    # Execute your query
    result = conn.execute(text("select * from hotel_db"))
    
    # Initialize an empty list to store your data
    hotels = []
    
    # Iterate over the result set and add each row to the list as a dictionary
    for row in result:
        hotels.append(dict(row._mapping))
    
    # Now data_list contains all rows as dictionaries
    return hotels
   
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
   
def load_room_from_db():
    with engine.connect() as conn:
        # Execute your query
        result = conn.execute(text("select * from room_db"))

        # Initialize an empty list to store your data
        rooms = []

        # Iterate over the result set and add each row to the list as a dictionary
        for row in result:
            rooms.append(dict(row._mapping))

        # Now data_list contains all rows as dictionaries
        return rooms
def load_city_from_db():
    with engine.connect() as conn:
        # Execute your query
        result = conn.execute(text("select * from city_db"))

        # Initialize an empty list to store your data
        cities = []

        # Iterate over the result set and add each row to the list as a dictionary
        for row in result:
            cities.append(dict(row._mapping))

        # Now data_list contains all rows as dictionaries
        return cities