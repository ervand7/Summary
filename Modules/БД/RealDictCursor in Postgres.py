# хоть какая-то чуть-чуть понятная информация есть здесь:
# https://coderoad.ru/45399347/psycopg2-DictCursor-против-RealDictCursor
"""RealDictCursor-это специализированный DictCursor, который позволяет получить
доступ к столбцам только из ключей (он же имя столбцов), в то время как DictCursor
позволяет получить доступ к данным как из ключей, так и из индексного номера. """
from psycopg2.extras import RealDictCursor


class DB:

    def __init__(self):
        self.host = ...
        self.port = ...
        self.username = ...
        self.password = ...
        self.conn = psycopg2.connect(
            host=self.host,
            port=self.port,
            user=self.username,
            password=self.password
        )
        self.cur = self.conn.cursor(cursor_factory=RealDictCursor)

    def execute(self, query):
        self.cur.execute(query)
        return self.cur.fetchall()


my_db = DB()
my_query = "select * from my_table"
my_db.execute(query=my_query)
