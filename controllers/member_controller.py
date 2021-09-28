from flask import Flask, render_template, request, redirect
from flask import Blueprint
from flask.helpers import url_for
from models.member import Member
import repositories.member_repository as member_repository
import repositories.lesson_repository as lesson_repository
import repositories.booking_repository as booking_repository

members_blueprint = Blueprint('members', __name__)

@members_blueprint.route('/members')
def members():
    members = member_repository.select_all()
    return render_template('members/index.html', title="All Members", members=members)

@members_blueprint.route('/members/show/<id>')
def show_member(id):
    member = member_repository.select(id)
    lessons = member_repository.lessons(member)
    return render_template('members/show.html', title=member.first + " " + member.last, member=member, lessons=lessons)

@members_blueprint.route('/members/new')
def new_member():
    return render_template('/members/new.html', title="New Member")

@members_blueprint.route('/members', methods=["POST"])
def post_member():
    first = request.form['first']
    last = request.form['last']
    type = request.form['type']
    member = Member(last, first, type)
    member_repository.save(member)
    return redirect('/members')

@members_blueprint.route('/members/edit/<id>', methods=["GET"])
def edit_member(id):
    member = member_repository.select(id)
    return render_template('/members/edit.html', title="Edit Member", member=member)

@members_blueprint.route('/members/<id>', methods=["POST"])
def update_member(id):
    first = request.form['first']
    last = request.form['last']
    type = request.form['type']
    member = Member(last, first, type, id)
    member_repository.update(member)
    return redirect('/members')

@members_blueprint.route('/members/book/<id>')
def book_member(id):
    lessons = lesson_repository.select_all()
    members = member_repository.select_all()
    member_selected = member_repository.select(id)
    return render_template('members/book_member.html', title = "Book " + member_selected.first, lessons=lessons, members=members, member_selected = member_selected)

@members_blueprint.route('/members/cancel_booking/<member_id>/<lesson_id>')
def cancel_booking(member_id, lesson_id):
    booking = booking_repository.select_by_member_lesson_id(member_id, lesson_id)
    booking_repository.delete(booking)
    lesson = lesson_repository.select(lesson_id)
    lesson.booked -= 1
    lesson_repository.update(lesson)
    return redirect(f'/members/show/{member_id}')
