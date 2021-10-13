import sqlite3


class DB:
    def __init__(self):
        super().__init__()

        self.conn = sqlite3.connect("contacts.db")
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        self.query = self.cursor.execute(
            'select first_name, last_name, email from contacts;'
        )

    @property
    def persons(self):
        with self.conn as connection:
            peoples_data = list(dict(person_data) for person_data in self.query)
        connection.close()
        return peoples_data


db = DB()
