class Database:
    def __init__(self):
        print("Connecting to database...")


class Service:
    def __init__(self):
        self._db = None  # not created yet

    @property
    def db(self) -> Database:
        if self._db is None:
            self._db = Database()  # created lazily
        return self._db


# Usage
service = Service()
print("Service created")
print(service.db)  # database is created here
