from pdb import run
from db.run_sql import run_sql

from models.member import Member
from models.lesson import Lesson

def save(member):
    sql = "INSERT INTO members (last, first, type) VALUES (%s, %s, %s) RETURNING *"
    values = [member.last, member.first, member.type]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return member

def select_all():
    sql = "SELECT * FROM members"
    results = run_sql(sql)

    members = []
    for member in results:
        member = Member(member['last'], member['first'], member['type'], member['id'])
        members.append(member)
    return members

def select(id):
    sql = "SELECT * FROM members WHERE id=%s"
    values = [id]
    result = run_sql(sql, values)[0]
    member = Member(result['last'], result['first'], result['type'], result['id'])
    return member
    

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

def delete(member):
    sql = "DELETE FROM members WHERE id=%s"
    values = [member.id]
    run_sql(sql,values)

def update(member):
    sql = "UPDATE members SET (last, first, type) = (%s, %s, %s) WHERE id=%s"
    values = [member.last, member.first, member.type, member.id]
    run_sql(sql, values)

def lessons(member):
    lessons = []
    sql = "SELECT lessons.* FROM lessons INNER JOIN bookings ON bookings.lesson_id = lessons.id WHERE member_id=%s"
    values = [member.id]
    results = run_sql(sql, values)
    for row in results:
        lesson = Lesson(row['date'], row['time'], row['description'], row['duration'], row['capacity'], row['booked'], row['id'])
        lessons.append(lesson)
    return lessons

