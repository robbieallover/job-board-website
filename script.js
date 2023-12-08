// JavaScript code for the job board

// Dummy data for jobs
const jobs = [
  {
    title: "Software Engineer",
    company: "ABC Inc.",
    description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
  },
  {
    title: "Web Developer",
    company: "XYZ Corp.",
    description: "Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas."
  }
];

// Render jobs on the page
function renderJobs() {
  const jobList = document.getElementById("jobList");

  // Clear existing job list
  jobList.innerHTML = "";

  // Render each job
  jobs.forEach(job => {
    const jobElement = document.createElement("div");
    jobElement.classList.add("job");

    const titleElement = document.createElement("div");
    titleElement.classList.add("title");
    titleElement.textContent = job.title;
    jobElement.appendChild(titleElement);

    const companyElement = document.createElement("div");
    companyElement.classList.add("company");
    companyElement.textContent = job.company;
    jobElement.appendChild(companyElement);

    const descriptionElement = document.createElement("div");
    descriptionElement.classList.add("description");
    descriptionElement.textContent = job.description;
    jobElement.appendChild(descriptionElement);

    jobList.appendChild(jobElement);
  });
}

// Call the renderJobs function to initially render the jobs
renderJobs();
