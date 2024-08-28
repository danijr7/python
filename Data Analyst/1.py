data_science_jobs = [
   {'job_title':'Data Scientist', 'job_skills':"['Python', 'SQL', 'Machine Learning']", 'job_date':'2023-05-12'},
   {'job_title':'Data Analyst', 'job_skills':"['Excel', 'SQL', 'Tableau']", 'job_date':'2023-06-25'},
   {'job_title':'Machine Learning Engineer', 'job_skills':"['Python', 'TensorFlow', 'Deep Learning']", 'job_date':'2023-07-08'},
   {'job_title':'Business Intelligence Analyst', 'job_skills':"['SQL', 'Power BI', 'Data Visualization']", 'job_date':'2023-08-15'},
   {'job_title':'Data Engineer', 'job_skills':"['Python', 'ETL', 'Big Data']", 'job_date':'2023-09-02'},
   {'job_title':'Statistician', 'job_skills':"['R', 'Statistical Analysis', 'Data Modeling']", 'job_date':'2023-09-20'},
   {'job_title':'Data Architect', 'job_skills':"['SQL', 'Database Design', 'Data Warehousing']", 'job_date':'2023-10-05'},
   {'job_title':'AI Researcher', 'job_skills':"['Python', 'Natural Language Processing', 'Deep Learning']", 'job_date':'2023-10-18'},
   {'job_title':'Data Science Consultant', 'job_skills':"['Python', 'R', 'Business Strategy']", 'job_date':'2023-11-03'},
   {'job_title':'Data Visualization Specialist', 'job_skills':"['Tableau', 'D3.js', 'Data Storytelling']", 'job_date':'2023-11-22'},
]

from datetime import datetime

datetime.now()

test_date = data_science_jobs[0][['job_date']]

time_now = datetime.strptime(test_date, '%Y-%m-%d')

for job in data_science_jobs:
  job['job_date'] = time_now

#print(data_science_jobs) muestro una lista con las fechas actualizadas