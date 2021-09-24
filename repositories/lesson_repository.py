from models.member import Member
from pdb import run
from db.run_sql import run_sql

from models.lesson import Lesson

def save(lesson):
    sql = "INSERT INTO lessons (date, time, description, duration, capacity) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [lesson.date, lesson.time, lesson.description, lesson.duration, lesson.capacity]
    results = run_sql(sql, values)
    lesson.id = results[0]['id']
    return lesson

def select_all():
    sql = "SELECT * FROM lessons"
    results = run_sql(sql)

    lessons = []
    for row in results:
        lesson = Lesson(row['date'], row['time'], row['description'], row['duration'], row['capacity'], row['id'])
        lessons.append(lesson)
    return lessons

def select(id):
    sql = "SELECT * FROM lessons WHERE id=%s"
    values = [id]
    result = run_sql(sql, values)[0]
    lesson = Lesson(result['date'], result['time'], result['description'], result['duration'], result['capacity'], result['id'])
    return lesson
    

def delete_all():
    sql = "DELETE FROM lessons"
    run_sql(sql)

def delete(lesson):
    sql = "DELETE FROM lessons WHERE id=%s"
    values = [lesson.id]
    run_sql(sql,values)

def update(lesson):
    sql = "UPDATE lessons SET (date, time, description, duration, capacity) = (%s, %s, %s, %s, %s) WHERE id=%s"
    values = [lesson.date, lesson.time, lesson.description, lesson.duration, lesson.capacity, lesson.id]
    run_sql(sql, values)

def members(lesson):
    members = []
    sql = "SELECT members.* FROM members INNER JOIN bookings ON bookings.member_id = members.id WHERE lesson_id=%s"
    values =[lesson.id]
    results = run_sql(sql, values)
    for row in results:
        member = Member(row['last'], row['first'], row['type'], row['id'])
        members.append(member)
    return members