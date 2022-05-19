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

# gerenate header for each course and save it as md
for course in courses_data:
  course = dict(course)
  course_id = course['id']
  course_name = course['name']
  course_aliases = get_courses_aliases(course['aliases'])

  content = f'---\nlayout: course\ntitle: {course_id} - {course_name}\naliases: {course_aliases}\ncourse_id: {course_id}\npermalink: /{course_id}/\n---'
  print(content)

  with open('courses/'+course['id']+".md", 'w') as f:
      f.write(content)


