"""
Generate a simple markdown page for all the courses in OMSCS.
"""

import json

with open('_data/courses.json', 'r') as f:
  data = json.load(f)

for course in data:
  course = dict(course)
  course_id = course['id']
  content = f'---\nlayout: course\ncourse_id: {course_id}\npermalink: /{course_id}/\n---'

  with open('courses/'+course['id']+".md", 'w') as f:
      f.write(content)