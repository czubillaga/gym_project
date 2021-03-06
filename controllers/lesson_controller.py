from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.lesson import Lesson
import repositories.lesson_repository as lesson_repository
import repositories.member_repository as member_repository
import repositories.booking_repository as booking_repository

lessons_blueprint = Blueprint('lessons', __name__)

@lessons_blueprint.route('/upcoming')
def upcoming():
    lessons = lesson_repository.select_all()
    return render_template('lessons/index.html', title='Upcoming', lessons=lessons)

@lessons_blueprint.route('/lessons/show/<id>')
def show(id):
    lesson = lesson_repository.select(id)
    members = lesson_repository.members(lesson)
    return render_template('lessons/show.html', title=lesson.description, lesson=lesson, members=members)

@lessons_blueprint.route('/lessons/new')
def new_lesson():
    return render_template('lessons/new.html', title="New Class")

@lessons_blueprint.route('/upcoming', methods=["POST"])
def post_lesson():
    date = request.form['date']
    time = request.form['time']
    description = request.form['description']
    duration = request.form['duration']
    capacity = request.form['capacity']
    lesson = Lesson(date, time, description, duration, capacity)
    lesson_repository.save(lesson)
    return redirect('/upcoming')

@lessons_blueprint.route('/lessons/edit/<id>', methods=["GET"])
def edit_lesson(id):
    lesson = lesson_repository.select(id)
    return render_template('lessons/edit.html', title="Edit Class", lesson=lesson)

@lessons_blueprint.route('/lessons/<id>', methods=["POST"])
def update_lesson(id):
    date = request.form['date']
    time = request.form['time']
    description = request.form['description']
    duration = request.form['duration']
    capacity = request.form['capacity']
    lesson = lesson_repository.select(id)
    lesson = Lesson(date, time, description, duration, capacity, lesson.booked, id)
    lesson_repository.update(lesson)
    return redirect('/upcoming')

@lessons_blueprint.route('/lessons/book/<id>')
def book_lesson(id):
    lesson_selected = lesson_repository.select(id)
    lessons = lesson_repository.select_all()
    members = member_repository.select_all()
    return render_template('/bookings/book_lesson.html', title ="Book " + lesson_selected.description, lesson_selected = lesson_selected, lessons = lessons, members = members)

@lessons_blueprint.route('/lessons/cancel_booking/<member_id>/<lesson_id>')
def cancel_booking(member_id, lesson_id):
    booking = booking_repository.select_by_member_lesson_id(member_id, lesson_id)
    booking_repository.delete(booking)
    lesson = lesson_repository.select(lesson_id)
    lesson.booked -= 1
    lesson_repository.update(lesson)
    return redirect(f"/lessons/show/{lesson_id}")