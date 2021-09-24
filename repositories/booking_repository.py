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
    return booking