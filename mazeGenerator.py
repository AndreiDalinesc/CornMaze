import random

adiacency_list = {}

visited = set()
stack = []
links = {}

def generate_adiacency_list(height, width):
    for i in range(height):
        for j in range(width):
            if (i, j) not in adiacency_list:
                adiacency_list[(i, j)] = []
            if i - 1 >= 0:
                adiacency_list[(i, j)].append((i - 1, j))
            if i + 1 < height:
                adiacency_list[(i, j)].append((i + 1, j))
            if j - 1 >= 0:
                adiacency_list[(i, j)].append((i, j - 1))
            if j + 1 < width:
                adiacency_list[(i, j)].append((i, j + 1))

    for point in adiacency_list.keys():
        links[point] = []


def neighbors_free():
    for i in adiacency_list.keys():
        for j in adiacency_list[i]:
            if j not in visited:
                return i
    return False


def generate_maze():
    while stack:
        current_point = stack.pop()
        visited.add(current_point)

        neighbors = [
            point
            for point in adiacency_list[current_point]
            if point not in visited and point not in stack
        ]


        number_of_neighbors_to_visit = 0

        if len(neighbors) == 0:
            continue
        elif len(neighbors) == 1:
            number_of_neighbors_to_visit = 1
        else:
            number_of_neighbors_to_visit = random.randint(1, len(neighbors))

        for _ in range(number_of_neighbors_to_visit):
            if len(neighbors) == 0:
                break
            elif len(neighbors) == 1:
                stack.append(neighbors[0])
                links[current_point].append(neighbors[0])
                neighbors.remove(neighbors[0])
                break
            else:
                stack.append(neighbors[random.randint(1, len(neighbors) - 1)])
                links[current_point].append(stack[-1])
                neighbors.remove(stack[-1])


dimOfMaze = [20,20]
generate_adiacency_list(dimOfMaze[0], dimOfMaze[1])

node = neighbors_free()
while node != False:
    stack.append(node)
    generate_maze()

    node = neighbors_free()

#print(links)