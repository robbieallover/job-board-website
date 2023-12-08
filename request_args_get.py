@app.route('/search', methods=['GET', 'POST'])
def search():
    query = request.args.get('q')
    jobs = Job.query.filter(or_(Job.title.ilike(f'%{query}%'), Job.company.ilike(f'%{query}%'))).all()
    return render_template('search.html', jobs=jobs, query=query)
