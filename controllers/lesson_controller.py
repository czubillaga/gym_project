from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.lesson import Lesson
import repositories.lesson_repository as lesson_repository

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