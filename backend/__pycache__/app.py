from flask import Flask
from extensions import db
from product import product_bp  # product routes
from auth import auth_bp  

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:25062005@localhost/shopdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(product_bp)

if __name__ == "__main__":
    app.run(debug=True)

