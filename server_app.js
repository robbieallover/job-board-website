@app.route('/apply/<int:job_id>', methods=['GET', 'POST'])
@authenticate
def apply(job_id):
    if request.method == 'POST':
        # Code to validate the application form data
        # Save the application to the database, associating it with the relevant job listing
        save_application(job_id, g.current_user['id'], request.form)

        # Provide feedback to the user after submitting the application
        flash('Application submitted successfully!')
        return redirect(url_for('job_details', job_id=job_id))
    
    # Code to retrieve the job details based on the job_id
    job = get_job_details(job_id)

    return render_template('application_form.html', job=job)
