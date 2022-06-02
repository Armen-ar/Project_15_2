import sqlite3

with sqlite3.connect("animal.db") as connection:
    cursor = connection.cursor()

    query_1 = """
        CREATE TABLE numbers (
        id INTEGER PRIMARY KEY autoincrement,
        number_id  VARCHAR(40)
    )
    """

    query_2 = """
        CREATE TABLE age_count (
        id INTEGER PRIMARY KEY autoincrement,
        day_month_year VARCHAR(40)
    )
    """

    query_3 = """
        CREATE TABLE number_age_count (
        number_id INTEGER,
        day_month_year_id INTEGER,
        PRIMARY KEY(number_id, day_month_year_id),
        FOREIGN KEY(number_id) REFERENCES numbers(number_id),
        FOREIGN KEY(day_month_year_id) REFERENCES age_count(day_month_year)
    )
    """

    query_4 = """
        CREATE TABLE animal_type (
        id INTEGER PRIMARY KEY autoincrement,
        type_id VARCHAR(40)
    )
    """

    query_5 = """
        CREATE TABLE breed (
        id INTEGER PRIMARY KEY autoincrement,
        breed_id VARCHAR(40)
    )
    """

    query_6 = """
        CREATE TABLE color (
        id INTEGER PRIMARY KEY autoincrement,
        color_id VARCHAR(40)
    )
    """

    query_7 = """
        CREATE TABLE outcome_subtype (
        id INTEGER PRIMARY KEY autoincrement,
        subtype_id VARCHAR(40)
    )
    """

    query_8 = """
        CREATE TABLE outcome_type (
        id INTEGER PRIMARY KEY autoincrement,
        type_id VARCHAR(40)
    )
    """

    query_9 = """
        CREATE TABLE outcome_month (
        id INTEGER PRIMARY KEY autoincrement,
        month_id INTEGER
    )
    """

    query_10 = """
        CREATE TABLE outcome_year (
        id INTEGER PRIMARY KEY autoincrement,
        year_id INTEGER
    )
    """

    query_11 = """
                CREATE TABLE cats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        age_upon_outcome_id INTEGER,
        animal_id VARCHAR(100),
        animal_type_id INTEGER,
        nickname_id VARCHAR(100) NOT NULL,
        breed_id INTEGER,
        color1_id INTEGER NOT NULL,
        color2_id INTEGER NOT NULL,
        date_of_birth_id VARCHAR(100),
        outcome_subtype_id INTEGER,
        outcome_type_id INTEGER,
        outcome_month_id INTEGER,
        outcome_year_id INTEGER,
        FOREIGN KEY(age_upon_outcome_id) REFERENCES age_upon_outcome(id) ON DELETE SET DEFAULT ON UPDATE CASCADE,
        FOREIGN KEY(animal_type_id) REFERENCES animal_type(id) ON DELETE SET DEFAULT ON UPDATE CASCADE,
        FOREIGN KEY(breed_id) REFERENCES breed(id) ON DELETE SET DEFAULT ON UPDATE CASCADE,
        FOREIGN KEY(color1_id) REFERENCES color(id) ON DELETE SET DEFAULT ON UPDATE CASCADE,
        FOREIGN KEY(color2_id) REFERENCES color(id) ON DELETE SET DEFAULT ON UPDATE CASCADE,
        FOREIGN KEY(outcome_subtype_id) REFERENCES outcome_subtype(id) ON DELETE SET DEFAULT ON UPDATE CASCADE,
        FOREIGN KEY(outcome_type_id) REFERENCES outcome_type(id) ON DELETE SET DEFAULT ON UPDATE CASCADE,
        FOREIGN KEY(outcome_month_id) REFERENCES outcome_type(id) ON DELETE SET DEFAULT ON UPDATE CASCADE,
        FOREIGN KEY(outcome_year_id) REFERENCES outcome_type(id) ON DELETE SET DEFAULT ON UPDATE CASCADE
        )
        """

    index_query = """
        CREATE INDEX animals_idx ON cats (animal_id)
    """
    cursor.executescript(query_1)
    cursor.executescript(query_2)
    cursor.executescript(query_3)
    cursor.executescript(query_4)
    cursor.executescript(query_5)
    cursor.executescript(query_6)
    cursor.executescript(query_7)
    cursor.executescript(query_8)
    cursor.executescript(query_9)
    cursor.executescript(query_10)
    cursor.executescript(query_11)
    cursor.executescript(index_query)
