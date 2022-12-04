import re


PATTERN = re.compile(r"(\d+)-(\d+),(\d+)-(\d+)")

with open('input.txt','r') as f:
   pairs = [row.replace('\n', '') for row in f.readlines()]

fully_overlapped_jobs = 0
overlapped_jobs = 0
for pair in pairs:
   first, first_last, second, second_last = map(int, re.match(PATTERN, pair).groups())
   #PROBLEM1
   p1_overlap1 = first >= second and first_last <= second_last
   p1_overlap2 = first <= second and first_last >= second_last
   #PROBLEM2
   p2_overlap = first <= second_last and first_last >= second

   if p1_overlap1 or p1_overlap2:
      fully_overlapped_jobs += 1
   if p2_overlap:
      overlapped_jobs += 1


print(fully_overlapped_jobs,overlapped_jobs)


