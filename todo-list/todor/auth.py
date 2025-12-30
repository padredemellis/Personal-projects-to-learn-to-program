from flask import Blueprint, render_template, request, url_for, redirect, flash
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

@bp.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('auth/login.html')