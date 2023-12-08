# Get all jobs
jobs = session.query(Job).all()

# Filter jobs by company
jobs = session.query(Job).filter(Job.company == 'ABC Corp').all()

# Sort jobs by title in ascending order
jobs = session.query(Job).order_by(Job.title.asc()).all()

# Aggregating data - Count jobs
job_count = session.query(Job).count()
