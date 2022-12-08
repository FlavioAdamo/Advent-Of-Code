with open('input.txt','r') as f:
   command_history =  f.read().splitlines()

pwd = []
filemap = {}
for command in command_history:
   is_command = command[0] == '$'

   if is_command and 'cd' in command:
      new_dir = command.split()[2]
      if new_dir == '/':
         pwd = ['/']
      elif new_dir == '..':
         pwd.pop()
      else:
         pwd.append(new_dir)
         filemap[" ".join(pwd)] = 0
      continue
   
   command = command.split()
   if command[0].isnumeric():
      path = " ".join(pwd)
      if path in filemap:
         filemap[path] += int(command[0])
         while(path != '/'):
            path = path.split()
            path = " ".join(path[:-1])
            filemap[path] += int(command[0])
      else:
         filemap[path]= int(command[0])


needed_space = 30000000 - (70000000 - filemap['/'])
size_sum = 0
diff = []
for key, value in filemap.items():
   if value >= needed_space:
      diff.append(value)
   if value > 100000:
      continue
   size_sum += value


print(size_sum)
print(min(diff))

