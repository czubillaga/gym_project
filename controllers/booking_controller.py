from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booking import Booking
import repositories.booking_repository as booking_repository
import repositories.lesson_repository as lesson_repository
import repositories.member_repository as member_repository

bookings_blueprint = Blueprint('bookings', __name__)

@bookings_blueprint.route('/bookings')
def bookings():
    bookings = booking_repository.select_all()
    return render_template('/bookings/index.html', title = "All Bookings", bookings = bookings)

@bookings_blueprint.route('/bookings/show/<id>')
def show_booking(id):
    booking = booking_repository.select(id)
    return render_template('/bookings/show.html', title = "Booking", booking = booking)

@bookings_blueprint.route('/bookings/new')
def new_booking():
    members = member_repository.select_all()
    lessons = lesson_repository.select_all()
    return render_template('/bookings/new.html', title="New Booking", members=members, lessons=lessons)

@bookings_blueprint.route('/bookings', methods=["POST"])
def post_booking():
    member_id = request.form['member_id']
    lesson_id = request.form['lesson_id']
    member = member_repository.select(member_id)
    lesson = lesson_repository.select(lesson_id)
    booking = Booking(member, lesson)
    try:
        booking_repository.save(booking)
    except:
        return redirect('/bookings')
    return redirect('/bookings')

@bookings_blueprint.route('/bookings/cancel/<id>')
def cancel_booking(id):
    booking = booking_repository.select(id)
    booking_repository.delete(booking)
    lesson = lesson_repository.select(booking.lesson.id)
    lesson.booked -= 1
    lesson_repository.update(lesson)
    return redirect('/bookings')