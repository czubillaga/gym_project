from pdb import run
from db.run_sql import run_sql

import repositories.lesson_repository as lesson_repository
import repositories.member_repository as member_repository

from models.lesson import Lesson
from models.member import Member
from models.booking import Booking

def save(booking):
    sql = "INSERT INTO bookings (lesson_id, member_id) VALUES (%s, %s) RETURNING *"
    values = [booking.lesson.id, booking.member.id]
    results = run_sql(sql, values)
    booking.id = results[0]['id']
    booking.lesson.booked += 1
    lesson_repository.update(booking.lesson)
    return booking

def delete(booking):
    sql = "DELETE FROM bookings WHERE id=%s"
    values = [booking.id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)

def select(id):
    sql = "SELECT * from bookings WHERE id=%s"
    values = [id]
    result = run_sql(sql, values)[0]
    member = member_repository.select(result['member_id'])
    lesson = lesson_repository.select(result['lesson_id'])
    booking = Booking(member, lesson, result['id'])
    return booking

def select_all():
    bookings = []
    sql = "SELECT * FROM bookings"
    results = run_sql(sql)
    for row in results:
        lesson = lesson_repository.select(row['lesson_id'])
        member = member_repository.select(row['member_id'])
        booking = Booking(member, lesson, row['id'])
        bookings.append(booking)
    return bookings

def update(booking):
    sql = "UPDATE bookings SET (lesson_id, member_id) = (%s,%s) WHERE id=%s"
    values = [booking.lesson.id, booking.member.id, booking.id]
    run_sql(sql, values)

def select_by_member_lesson_id(member_id, lesson_id):
    sql = "SELECT * FROM bookings WHERE member_id=%s AND lesson_id=%s"
    values = [member_id, lesson_id]
    result = run_sql(sql, values)
    booking_id = result[0]['id']
    member = member_repository.select(member_id)
    lesson = lesson_repository.select(lesson_id)
    booking = Booking(member, lesson, booking_id)
    return booking 