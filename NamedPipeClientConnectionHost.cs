app.get('/job-listings', (req, res) => {
  const query = 'SELECT * FROM job_listings';
  
  db.query(query, (error, results) => {
    if (error) {
      console.error(error);
      res.status(500).send('Error fetching job listings');
    } else {
      res.render('job-listings', { jobListings: results }); // Render a template with the job listings data
    }
  });
});
