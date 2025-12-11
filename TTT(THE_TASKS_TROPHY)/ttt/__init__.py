from flask import Flask, render_template

def create_app():
    app = Flask(__name__)
    #Configuracion del proyecto
    app.config.from_mapping(
        DEBUG= True,
        SCRET_KEY = 'dev'
    )
    
    #Registrar Blueprint
    from . import main
    app.register_blueprint(main.bp)
    
    from . import auth
    app.register_blueprint (auth.bp)


    @app.route('/')
    def index():
        return render_template('index.html')
    
    return app
