pip install flask sqlalchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'  # Replace with your preferred database URI
db = SQLAlchemy(app)
class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
db.create_all()
# Create a new job
job = Job(title='Software Engineer', company='ABC Corp', description='Job description goes here')
db.session.add(job)
db.session.commit()

# Retrieve all jobs
jobs = Job.query.all()

# Update a job
job = Job.query.get(1)
job.title = 'Updated Title'
db.session.commit()

# Delete a job
job = Job.query.get(1)
db.session.delete(job)
db.session.commit()
