from flask import Blueprint, render_template, request, redirect, url_for
from .models import Task
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@main.route('/add', methods=['POST'])
def add():
    task_content = request.form.get('content')
    if task_content:
        new_task = Task(content=task_content)
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/delete/<int:id>')
def delete(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/complete/<int:id>')
def complete(id):
    task = Task.query.get_or_404(id)
    task.complete = not task.complete
    db.session.commit()
    return redirect(url_for('main.index'))
