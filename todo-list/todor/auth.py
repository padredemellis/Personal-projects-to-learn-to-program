from flask import Blueprint, render_template, request, url_for, redirect, flash, session, g
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from todor import db
'''
**¿Qué contiene?** Toda la lógica de **autenticación de usuarios**.

**Ejemplos de rutas que irán aquí:**
- `GET /register` - Mostrar formulario de registro
- `POST /register` - Procesar registro de nuevo usuario
- `GET /login` - Mostrar formulario de login
- `POST /login` - Procesar inicio de sesión
- `GET /logout` - Cerrar sesión

**Concepto clave:** Maneja todo lo relacionado con la identidad del usuario (quién es, puede acceder, etc.).
'''
bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods = ('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User(username, generate_password_hash(password))

        user_name = User.query.filter_by(username = username).first()

        if user_name is None:
            db.session.add(user)
            db.session.commit()

            return redirect(url_for('auth.login'))
        else:
            flash(f"Ese nombre {username} ya existe. Prueba con otro", "error")

    return render_template('auth/register.html')

@bp.route('/login',  methods = ('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']


        user = User.query.filter_by(username = username).first()

        error = None
    #Validacion
        if user is None:
            error = f"{user} es incorrecto"
        elif not check_password_hash(user.password, password):
            error = "Contraseña incorrecta"
    #Iniciar sesion
        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('todo.index'))
        flash(error)

    return render_template('auth/login.html')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get_or_404(user_id)

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

import functools

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view