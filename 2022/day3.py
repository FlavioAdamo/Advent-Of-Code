CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def get_score(char):
   return CHARS.find(char) + 1

#SOLUTION
with open('input.txt', 'r') as input_file:
   rucksacks = input_file.read().split('\n')

chars_list = []
for items in rucksacks:
   middle = len(items)//2
   chars_list.append(
      get_score(list(set(items[:middle]).intersection(items[middle:]))[0])
   )

bedges = []
for index in range(0, len(rucksacks[:-2]), 3):
   common_chars = list(
         set(rucksacks[index])
         .intersection(rucksacks[index + 1])
         .intersection(rucksacks[index + 2])
   )
   bedges.append(get_score(common_chars[0]))

print(sum(chars_list), sum(bedges))

