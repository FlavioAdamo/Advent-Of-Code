import re 


def parse_stacks(stacks_input):
    stacks = [[] for _ in range(9)]
    for stack in stacks_input[:-1]:
        index = 0
        for item in range(1, 34, 4):
            if stack[item] != ' ':
                stacks[index].append(stack[item])
            index += 1
    return stacks   


def make_moves(part=1):
    reverse = True if part == 1 else False
    for move in moves:
        _move, _from, _to = list(map(int, move))
        if _move == 1:
            element_to_move = stacks[_from-1][-_move]
        else:
            element_to_move = stacks[_from-1][-_move:]

        stacks[_from-1] = stacks[_from-1][:-_move]
        element_to_move = list(element_to_move)
        if reverse:
            element_to_move.reverse()
        stacks[_to-1] = stacks[_to-1] + element_to_move


with open('input.txt','r') as f:
    stacks_input, moves = f.read().split('\n\n')
    stacks_input = stacks_input.split('\n')


moves = [re.findall(r'\b\d+\b', move) for move in moves.split('\n')]
stacks = parse_stacks(stacks_input)
for stack in stacks:
    stack.reverse()

make_moves(part=1)
result = [stack[-1] for stack in stacks]














    
