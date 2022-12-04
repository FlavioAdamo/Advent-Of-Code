# #SOLUTION-1
with open("input.txt", "r") as file:
   file_text = file.read().split('\n\n')

   elfs_calories = [calories.split('\n') for calories in file_text]
   elfs_calories = [list(map(int, calories)) for calories in elfs_calories]

   summed_elfs_calories = [sum(calories) for calories in elfs_calories]
   #PART 1
   most_calories = max(summed_elfs_calories)
   #PART 2
   top_three_calories = sum(sorted(summed_elfs_calories, reverse=True)[0:3])

print(most_calories, top_three_calories)
