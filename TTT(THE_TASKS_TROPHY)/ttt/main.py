from flask import Blueprint

bp = Blueprint('The_task_trophy', __name__, url_prefix = "/The_task_trophy")

@bp.route('/list')
def index():
    return "Lists of task"

@bp.route('/create')
def create():
    return "Crear una tarea"