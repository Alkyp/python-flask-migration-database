from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__, instance_relative_config= True, template_folder='templates')
app.config.from_object("config")
app.config.from_object(Config)
db = SQLAlchemy(app)
Migrate = Migrate(app, db)

from flask_server.app.model import Barang  
from app.model import customers
from flask_server.app.model import Pembeli
from app.model import productnotes
from flask_server.app.model import Transaksi
from app.model import orders
from app.model import orderitems
from app import routes

