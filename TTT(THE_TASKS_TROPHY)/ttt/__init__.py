from flask import Flask

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
    
    @app.route('/')
    def index():
        return "<h1>The Tasks Trophy<h1>"
    
    return app
