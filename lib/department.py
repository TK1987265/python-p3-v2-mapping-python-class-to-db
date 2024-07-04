
from __init__ import CURSOR, CONN

class Department:
    def __init__(self, name, location, id=None):
        self.id = id
        self.name = name
        self.location = location

    @classmethod
    def create_table(cls):
        """Creates a departments table if it does not already exist."""
        sql = """
            CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Drops the departments table."""
        CURSOR.execute("DROP TABLE IF EXISTS departments")
        CONN.commit()

    def save(self):
        """Saves the instance to the database."""
        sql = "INSERT INTO departments (name, location) VALUES (?, ?)"
        CURSOR.execute(sql, (self.name, self.location))
        CONN.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, name, location):
        """Creates and saves a new instance directly."""
        department = cls(name, location)
        department.save()
        return department

    def update(self):
        """Updates the corresponding database record."""
        sql = "UPDATE departments SET name = ?, location = ? WHERE id = ?"
        CURSOR.execute(sql, (self.name, self.location, self.id))
        CONN.commit()

    def delete(self):
        """Deletes the corresponding database record."""
        CURSOR.execute("DELETE FROM departments WHERE id = ?", (self.id,))
        CONN.commit()
