from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__, instance_relative_config=True)

os.makedirs(app.instance_path, exist_ok=True)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(app.instance_path, "elections.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize database
db = SQLAlchemy(app)

# Election model
class Election(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    scope = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f"<Election {self.name}>"

@app.route("/")
def home():
    elections = Election.query.all()
    return render_template("home.html", elections=elections)

@app.route("/dbpath")
def dbpath():
    return f"Database file: {db.engine.url}"

@app.route("/elections/<int:election_id>")
def election_detail(election_id):
    election = Election.query.get_or_404(election_id)
    return render_template("election_detail.html", election=election)
if __name__ == "__main__":
    app.run(debug=True)
