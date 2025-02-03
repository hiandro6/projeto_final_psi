from Flask import flask
from database.config import engine
from database import Base
from controllers.users import login_manager, user_bp

app = Flask(__name__)


app.config['SECRET_KEY'] = 'hashdhfiogoq3812021fsa'


login_manager.init_app(app)

with app.app_context():
    Base.metadata.create_all(bind=engine)


app.register_blueprint(user_bp)

