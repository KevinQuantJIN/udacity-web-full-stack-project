# Bug Issues can find in this link:https://chat.openai.com/share/6c633683-cb1f-40f0-a46f-255a46d6bd07
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://postgres:061010@localhost:5432/example"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

migrate = Migrate(app, db)


class Person(db.Model):
    __tablename__ = "persons"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f"<Person ID: {self.id}, name: {self.name}>"


# with app.app_context():
#     db.create_all()


@app.route("/")
def index():
    person = Person.query.first()
    return "<h1>Hello " + person.name + "</h1>"


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=6074)
