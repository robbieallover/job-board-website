# Create
job = Job(title='Software Engineer', company='ABC Corp', description='Job description goes here')
session.add(job)
session.commit()

# Read
jobs = session.query(Job).all()

# Update
job = session.query(Job).filter_by(id=1).first()
job.title = 'Updated Title'
session.commit()

# Delete
job = session.query(Job).filter_by(id=1).first()
session.delete(job)
session.commit()
