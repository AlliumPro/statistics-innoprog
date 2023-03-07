import psycopg2
import datetime


class Database:
    def __init__(self):
        self.db = psycopg2.connect(database='innoprog', user='readonly', password='readonly', host='94.103.93.208',
                                   port=5432)
        self.cursor = self.db.cursor()

    def getAttendance(self, dateFrom: datetime.date, dateTo: datetime.date):
        self.cursor.execute("SELECT id, username, last_visit FROM client;")
        result = self.cursor.fetchall()
        result1 = []
        for i in result:
            if i[2].date() >= dateFrom and i[2].date() <= dateTo:
                result1.append(i)
        return result1
