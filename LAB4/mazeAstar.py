import numpy as np


class Node:
    """
    Parent is parent of the current node
    Position is current position of the node
    g is cost from start to node N
    h is estimated cost from node N to goal
    f is the total estimated cost to reach goal
    """

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


# This function returns the path of search
def return_path(current_node, maze):
    path = []
    no_rows, no_columns = np.shape(maze)
    result = [[-1 for i in range(no_columns)] for j in range(no_rows)]
    current = current_node
    while current is not None:
        path.append(current.position)
        current = current.parent
    path = path[::-1]
    start_value = 0
    for i in range(len(path)):
        result[path[i][0]][path[i][1]] = start_value
        start_value += 1
    return result


"""
Return a list of tuples as a path from the start node to the end/goal in the maze
"""


def search(maze, cost, start, end):
    start_node = Node(None, tuple(start))
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, tuple(end))
    end_node.g = end_node.h = end_node.f = 0

    yet_to_visit_list = []
    visited_list = []
    yet_to_visit_list.append(start_node)
    outer_iterations = 0
    max_iterations = (len(maze) // 2) ** 10
    move = [[-1, 0],
            [0, -1],
            [1, 0],
            [0, 1]]
    no_rows, no_columns = np.shape(maze)

    while len(yet_to_visit_list) > 0:
        outer_iterations += 1
        current_node = yet_to_visit_list[0]
        current_index = 0
        for index, item in enumerate(yet_to_visit_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        if outer_iterations > max_iterations:
            print("giving up on path finding too many iterations")
            return return_path(current_node, maze)

        yet_to_visit_list.pop(current_index)
        visited_list.append(current_node)
        if current_node == end_node:
            return return_path(current_node, maze)

        children = []
        for new_position in move:
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            if node_position[0] > (no_rows - 1) or node_position[0] < 0 or node_position[1] > (no_columns - 1) or \
                    node_position[1] < 0:
                continue

            if maze[node_position[0]][node_position[1]] != 0:
                continue

            new_node = Node(current_node, node_position)
            children.append(new_node)
        for child in children:
            if len([visited_child for visited_child in visited_list if visited_child == child]) > 0:
                continue
            child.g = current_node.g + cost
            child.h = (((child.position[0] - end_node.position[0]) ** 2) +
                       ((child.position[1] - end_node.position[1]) ** 2))
            child.f = child.g + child.h

            if len([i for i in yet_to_visit_list if child == i and child.g > i.g]) > 0:
                continue
            yet_to_visit_list.append(child)


if __name__ == '__main__':
    maze = []
    r = int(input("Enter number of rows "))
    for i in range(r):
        row = list(map(int, input().split()))
        maze.append(row)

    start = []
    end = []
    n = 2
    print("Enter start state")
    for i in range(0, n):
        ele = int(input())
        start.append(ele)

    print("Enter end state")
    for j in range(0, n):
        val = int(input())
        end.append(val)
    
    cost = 1
    path = search(maze, cost, start, end)
    print(maze)
    print('\n')

    print(path)
    print('\n')
    print('\n'.join([''.join(["{:" ">3d}".format(item) for item in row]) for row in path]))
