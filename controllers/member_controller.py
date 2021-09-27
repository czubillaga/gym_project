from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
import repositories.member_repository as member_repository

members_blueprint = Blueprint('members', __name__)

@members_blueprint.route('/members')
def members():
    members = member_repository.select_all()
    return render_template('members/index.html', title="All Members", members=members)

@members_blueprint.route('/members/show/<id>')
def show_member(id):
    member = member_repository.select(id)
    lessons = member_repository.lessons(member)
    return render_template('members/show.html', title=member.first + member.last, member=member, lessons=lessons)

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
