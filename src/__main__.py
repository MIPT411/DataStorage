from .app import app
from .config import WEB_HOST, WEB_PORT, WEB_DEBUG

# Include modules
from .modules import auth_module

if __name__ == "__main__":
    # Register modules
    app.register_blueprint(auth_module)
    # Run service
    app.run(host=WEB_HOST, port=WEB_PORT, debug=WEB_DEBUG)
