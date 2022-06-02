import sqlite3

with sqlite3.connect("animal.db") as connection:
    cursor = connection.cursor()

    query_1 = """
        CREATE TABLE age_upon_outcome (
        id INTEGER PRIMARY KEY autoincrement,
        age_id INTEGER,
        FOREIGN KEY (age_id) REFERENCES animals(age_upon_outcome)
    )
    """

    query_2 = """
        CREATE TABLE animal_type (
        id INTEGER PRIMARY KEY autoincrement,
        type_id INTEGER,
        FOREIGN KEY (type_id) REFERENCES animals(animal_type)
    )
    """

    query_3 = """
        CREATE TABLE breed (
        id INTEGER PRIMARY KEY autoincrement,
        breed_id INTEGER,
        FOREIGN KEY (breed_id) REFERENCES animals(breed)
    )
    """

    query_4 = """
        CREATE TABLE color (
        id INTEGER PRIMARY KEY autoincrement,
        color_id INTEGER,
        FOREIGN KEY (color_id) REFERENCES animals(color)
    )
    """

    query_5 = """
        CREATE TABLE color_color (
        color_1_id INTEGER,
        color_2_id INTEGER,
        PRIMARY KEY (color_1_id, color_2_id),
        FOREIGN KEY (color_1_id) REFERENCES animals(color1_id),
        FOREIGN KEY (color_2_id) REFERENCES animals(color2_id)
    )
    """

    query_6 = """
        CREATE TABLE outcome_subtype (
        id INTEGER PRIMARY KEY autoincrement,
        subtype_id INTEGER,
        FOREIGN KEY (subtype_id) REFERENCES animals(outcome_subtype)
    )
    """

    query_7 = """
        CREATE TABLE outcome_type (
        id INTEGER PRIMARY KEY autoincrement,
        type_id INTEGER,
        FOREIGN KEY (type_id) REFERENCES animals(outcome_type)
    )
    """

    query_8 = """
        CREATE TABLE outcome_month (
        id INTEGER PRIMARY KEY autoincrement,
        month_id INTEGER,
        FOREIGN KEY (month_id) REFERENCES animals(outcome_month)
    )
    """

    query_9 = """
        CREATE TABLE outcome_year (
        id INTEGER PRIMARY KEY autoincrement,
        year_id INTEGER,
        FOREIGN KEY (year_id) REFERENCES animals(outcome_year)
    )
    """

    query_10 = """
            CREATE TABLE cats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                age_upon_outcome_id INTEGER,
                FOREIGN KEY (age_upon_outcome_id) REFERENCES age_upon_outcome(id),
                animal_id VARCHAR(100), FOREIGN KEY REFERENCES animals(animal_id),
                animal_type_id INTEGER,
                FOREIGN KEY (animal_type_id) REFERENCES animal_type(id),
                nickname_id VARCHAR(100), FOREIGN KEY REFERENCES animals(name),
                breed_id INTEGER,
                FOREIGN KEY (breed_id) REFERENCES breed(id),
                color_id INTEGER,
                FOREIGN KEY (color_id) REFERENCES color(id),
                date_of_birth_id VARCHAR(100), FOREIGN KEY REFERENCES color(date_of_birth),
                outcome_subtype_id INTEGER,
                FOREIGN KEY (outcome_subtype_id) REFERENCES outcome_subtype(id),
                outcome_type_id INTEGER,
                FOREIGN KEY (outcome_type_id) REFERENCES outcome_type(id),
                outcome_month_id INTEGER,
                FOREIGN KEY (outcome_month_id) REFERENCES outcome_type(id),
                outcome_year_id INTEGER,
                FOREIGN KEY (outcome_year_id) REFERENCES outcome_type(id)
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
    cursor.executescript(index_query)
