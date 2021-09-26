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
    return render_template('members/show.html', title=member.first + member.last, member=member)