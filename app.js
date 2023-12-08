app.post('/create-job', (req, res) => {
  const { job_title, company, location, description } = req.body;
  
  // Validate the form data (e.g., check for empty fields)
  // ...
  
  // Save the job listing to the database
  const query = 'INSERT INTO job_listings (job_title, company, location, description) VALUES (?, ?, ?, ?)';
  const values = [job_title, company, location, description];
  
  db.query(query, values, (error, result) => {
    if (error) {
      console.error(error);
      res.status(500).send('Error saving job listing');
    } else {
      res.redirect('/job-listings'); // Redirect to the job listings page
    }
  });
});
