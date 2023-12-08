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
