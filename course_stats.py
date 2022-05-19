""" create stats"""
import json

with open('_data/reviews.json', 'r') as f:
  review_data = json.load(f)

stats = {}
stat_types = ['difficulty', 'rating', 'workload']

# get all the stats in dict form
for review in review_data:
    review = dict(review)
    course_id = review['course_id']
    for stat_type in stat_types:
        if course_id in stats:
            val = review[stat_type]
            # ignore  None values
            if val is not None: 
                stats[course_id][stat_type].append(float(val))
        else:
            stats[course_id] = {}
            for stat_type in stat_types:
                val = review[stat_type]
                if val is not None:
                    stats[course_id][stat_type] = [float(val)]
print(stats)
# summarize all the Stats
avg_stats = {}
for course_name, course_stats in stats.items():
    avg_stats[course_name] = {}
    for stat_type in stat_types:
        vals = course_stats[stat_type]
        avg = sum(vals) / len(vals)
        avg_stats[course_name][stat_type] = "{:.2f}". format(avg)


# save Stats
with open('_data/my_avg_statas.json', 'w') as fp:
    json.dump(avg_stats, fp)

