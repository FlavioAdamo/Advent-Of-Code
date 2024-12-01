lines = [line.strip() for line in open("input.txt")]
a, b = map(sorted, zip(*map(str.split, lines)))
# SOLUTION 1
sum_distance = sum(abs(int(a) - int(b)) for a, b in zip(a, b))
# SOLUTION 2
sum_similarity = sum(int(id) * b.count(id) for id in a)