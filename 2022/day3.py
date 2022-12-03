LOWER = 'abcdefghijklmnopqrstuvwxyz'
UPPER = LOWER.upper()


def get_score(char):
   if char in LOWER:
      return LOWER.find(char) +1
   return UPPER.find(char) + 27


#SOLUTION
with open('input.txt', 'r') as input_file:
   rucksacks = input_file.read().split('\n')
chars_list = []
bedges = []
for items in rucksacks:
   common_chars = list(set(items[:len(items)//2])
            .intersection(items[len(items)//2:]))

   chars_list.append(get_score(common_chars[0]))

for index in range(0, len(rucksacks[:-2]), 3):
   common_chars = list(
         set(rucksacks[index])
         .intersection(rucksacks[index + 1])
         .intersection(rucksacks[index + 2])
   )
   bedges.append(get_score(common_chars[0]))

print(sum(chars_list), sum(bedges))

