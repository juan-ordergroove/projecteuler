import json

# File input was altered to include '[' and ']' - to allow 
# for simple data set load using json.loads(s)
f = open('problem22_names.txt')
names = json.loads(f.readline())
names.sort()

name_score_total = 0
for i in range(len(names)):    
    name = names[i]
    name_score = 0
    for c in name:
        name_score = name_score + (ord(c)-ord('A') + 1)
    name_score_total = name_score_total + (name_score*(i+1))
print name_score_total