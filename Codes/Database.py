import psycopg2
import datetime
import os
from dotenv import load_dotenv

COST = 4900


class Database:
    def __init__(self):
        load_dotenv()
        self.db = psycopg2.connect(
            database=os.getenv('DATABASE'),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            host=os.getenv("HOST"),
            port=os.getenv("PORT"),
        )
        self.cursor = self.db.cursor()

    def getAttendance(self, dateFrom: datetime.date, dateTo: datetime.date):
        self.cursor.execute("SELECT id, username, last_visit FROM client;")
        result = self.cursor.fetchall()
        result1 = []
        for i in result:
            if i[2].date() >= dateFrom and i[2].date() <= dateTo:
                result1.append(i)
        return result1

    def getUsers(self, filter=None):
        self.cursor.execute("SELECT id, username FROM client;")
        result = self.cursor.fetchall()
        result1 = []
        if filter == None:
            return result
        for user in result:
            if (
                filter.lower() in str(user[0]).lower()
                or user[1] is not None
                and filter.lower() in user[1].lower()
            ):
                result1 += [user]
        return result1

    def getPaymentInfo(self, id=None, username=None):
        if id is not None:
            self.cursor.execute(
                f"SELECT id, username, rank FROM client WHERE id = {id};"
            )
        elif username is not None:
            self.cursor.execute(
                f"SELECT id, username, rank FROM client WHERE username = '{username}';"
            )
        else:
            raise Exception("Type username or id")

        user = self.cursor.fetchone()
        if len(user) == 0:
            raise Exception("No data found")

        self.cursor.execute(f"SELECT discount FROM rank WHERE name = '{user[2]}';")
        discount = self.cursor.fetchone()[0]  # (3,) tuple
        payment = COST * (1 - discount * 0.01)
        return user[0], user[1], payment

    def getAuthorizationInfo(self, login, password):
        if login and password:
            self.cursor.execute(
                f"SELECT username, id, name FROM teacher WHERE id = {password} AND username = '{login}';"
            )
            user = self.cursor.fetchone()
            return user
        else:
            return None

    def getTeachers(self):
        self.cursor.execute("SELECT distinct teacher_id FROM office_hours;")
        teachersID = self.cursor.fetchall()
        teachers = []
        for teacher in teachersID:
            self.cursor.execute(f"SELECT name FROM teacher WHERE id={teacher[0]};")
            teachers.append(self.cursor.fetchone()[0])
        return teachers

    def getOfficeHoursByTeacher(self, teacher, month=None, year=None):
        self.cursor.execute(
            f"""SELECT office_hours."time", client.id, client.username, office_hours.recording 
        FROM office_hours 
        JOIN teacher ON office_hours.teacher_id = teacher.id 
        JOIN purchases ON purchases.id = office_hours.purchases_id 
        JOIN client ON client.id = purchases.client_id 
        WHERE teacher.name = '{teacher}';"""
        )
        result = self.cursor.fetchall()
        if month is not None or year is not None:
            return [
                lesson
                for lesson in result
                if lesson[0].month == month + 1 and lesson[0].year == year
            ]
        return result
