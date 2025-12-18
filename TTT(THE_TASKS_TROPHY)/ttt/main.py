from flask import Blueprint, render_template

bp = Blueprint('The_task_trophy', __name__, url_prefix = "/The_task_trophy")

@bp.route('/list')
def index():
    return render_template('ttt/index.html')
@bp.route('/create')
def create():
    return "Crear una tarea"