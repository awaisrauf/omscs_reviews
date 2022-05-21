"""
Generate a simple markdown page for all the courses in OMSCS.
"""

import json


def get_courses_aliases(aliases: str) -> str:
  """
  get raw aliases and converts them to a useful string after preprocessing.
  """
  print("alias:", aliases)
  course_aliases = aliases.replace("[", "").replace("]", "")
  course_aliases = course_aliases.replace("[", "").replace("\"", "")
  course_aliases = course_aliases.split(',')
  
  course_aliases = [alias for alias in course_aliases]
  course_aliases = ', '. join(course_aliases) if course_aliases else 'None'

  return course_aliases

with open('_data/courses.json', 'r') as f:
  courses_data = json.load(f)

with open('_data/my_avg_stats.json', 'r') as f:
  courses_avg_stats = json.load(f)

# gerenate header for each course and save it as md
for course in courses_data:
  
  course = dict(course)
  # course data
  course_id = course['id']
  course_number = course['number']
  course_name = course['name'].replace(':', ' - ')
  course_aliases = get_courses_aliases(course['aliases'])

  # course avg stats
  if course_id in courses_avg_stats:
    avg_diff = courses_avg_stats[course_id]['difficulty']
    avg_rating = courses_avg_stats[course_id]['rating']
    avg_workload = courses_avg_stats[course_id]['workload']
  else:
    avg_diff = 0
    avg_rating = 0
    avg_workload = 0

  # page header
  start = f'---\n'
  body1 = f'layout: course\ntitle: {course_id} - {course_name}\naliases: {course_aliases}\ncourse_id: {course_id}\npermalink: /{course_id}/\n'
  body2 = f'avg_difficulty: {avg_diff}\navg_rating: {avg_rating}\navg_workload: {avg_workload}\n'
  body3 = f'type: course_page\n'
  body4 = f'course_number: {course_number}\n'
  end = '---'
  content = start+body1+body2+body3+end

  with open('courses/'+course['id']+".md", 'w') as f:
      f.write(content)


