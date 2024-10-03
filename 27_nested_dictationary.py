course={
    'btech':{'duration':'5year','fees':4000},
    'mtech':{'duration':'4year','fees':5000},
    'phd':{'duration':'3year','fees':6000},

}
print(course)
print(course['btech'])
print(course['btech']['fees'])

for k,v in course.items():
    print(k,v)

for k,v in course.items():
    print(k,v['duration'],v['fees'])