def start_index_stream(stream: str, diff=4):
   for i in range(len(stream[:-diff])):
      chars = stream[i:i+diff]
      if len(chars) == len(set(chars)):
         return i+diff


with open('input.txt','r') as f:
   buffer = f.read()


p1 = start_index_stream(buffer, diff=4)
print(p1)
p2 = start_index_stream(buffer, diff=14)
print(p2)