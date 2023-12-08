pip install flask-sqlalchemy
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'
db = SQLAlchemy(app)
python
from app import db
db.create_all()
@app.route('/')
def index():
    jobs = Job.query.all()  # Retrieve all job listings from the database
    return render_template('index.html', jobs=jobs)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        title = request.form.get('title')
        company = request.form.get('company')
        description = request.form.get('description')

        job = Job(title=title, company=company, description=description)
        db.session.add(job)  # Add the job to the database session
        db.session.commit()  # Commit the changes to the database

        return redirect(url_for('index'))

    return render_template('submit.html')
