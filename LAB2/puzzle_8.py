class Node:
    def __init__(self, data, level, fval):
        # Initialize Node with data, level, fval
        self.data = data
        self.level = level
        self.fval = fval

    def generateChild(self):
        # Generate Child nodes from the given Node by moving the blank space in either of 4 directions
        x, y = self.find(self.data, '_')
        # val_list contains 4 directions
        val_list = [[x, y-1], [x, y+1], [x-1, y], [x+1, y]]
        children = []
        for i in val_list:
            child = self.shuffle(self.data, x, y, i[0], i[1])
            if child is not None:
                child_node = Node(child, self.level+1, 0)
                children.append(child_node)
        return children

    def shuffle(self, puz, x1, y1, x2, y2):
        # Move the blank space in the given direction and if the position values are out of limits
        # return None
        if 0 <= x2 < len(self.data) and 0 <= y2 < len(self.data):
            temp_puz = []
            temp_puz = self.copy(puz)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None

    def copy(self, root):
        # Copy Function to create a similar matrix of node
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp

    def find(self, puz, x):
        # Specifically used to find functions of blank space
        for i in range(0, len(self.data)):
            for j in range(0, len(self.data)):
                if puz[i][j] == x:
                    return i, j


class Puzzle:
    def __init__(self, size):
        # Specify the puzzle size, open lists and empty lists
        self.n = size
        self.open = []
        self.close = []

    def accept(self):
        # Accepts the puzzle form the user
        puz = []
        for i in range(0, self.n):
            temp = input().split(" ")
            puz.append(temp)
        return puz

    def f_val(self, start, goal):
        # Heuristic Function to calculate Heuristic value f(x) = g(x) + h(x)
        return self.h(start.data, goal) + start.level

    def h(self, start, goal):
        # Calculates Difference between the given puzzles
        temp = 0
        for i in range(0, self.n):
            for j in range(0, self.n):
                if start[i][j] != goal[i][j] and start[i][j] != '_':
                    temp += 1
        return temp

    def process(self):
        # Accepts Start and Goal Puzzle states
        print("Using BFS method with two queues")
        print("Enter the start state matrix")
        start = self.accept()
        print("Enter the Goal state matrix")
        goal = self.accept()
        count = 0

        start = Node(start, 0, 0)
        start.fval = self.f_val(start, goal)
        # Put the Start Mode in the Open List
        self.open.append(start)
        print("\n\n")
        while True:
            cur = self.open[0]
            count = count+1
            print("")
            print(" | ")
            print(" | ")
            print("\\\'/\n")
            for i in cur.data:
                for j in i:
                    print(j, end=" ")
                print("")
            print("Number of moves: ", count)
            # If the difference between current and goal node is 0, we have reached the goal state
            if self.h(cur.data, goal) == 0:
                break
            for i in cur.generateChild():
                i.fval = self.f_val(i, goal)
                self.open.append(i)
            self.close.append(cur)
            del self.open[0]

            # Sort the open list based on f value
            self.open.sort(key=lambda x:x.fval, reverse=False)


if __name__ == "__main__":
    puz = Puzzle(3)
    puz.process()



