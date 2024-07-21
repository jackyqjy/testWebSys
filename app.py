from flask import Flask
import config
from blueprints.cms import bp as cms_bp
from blueprints.front import bp as front_bp
from blueprints.user import bp as user_bp
from flask_migrate import Migrate
from exts import db
import commands

app = Flask(__name__)
app.config.from_object(config.TestingConfig)
db.init_app(app)

app.register_blueprint(cms_bp)
app.register_blueprint(front_bp)
app.register_blueprint(user_bp)

migrate = Migrate(app, db)

#app.cli.commands("create-permission")(commands.create_permission)
#app.cli.commands("create-role")(commands.create_role)




