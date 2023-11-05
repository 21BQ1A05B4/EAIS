import numpy as np


def bfsFindGoal(init, goal):
    visited = [init]
    queue = []
    queue.append([init, []])

    while queue:
        current_state, operations = queue.pop(0)

        if np.all(current_state == goal):  # Check if the current state is the goal state
            return operations
        r1, c1 = np.where(current_state == 0)
        r1, c1 = r1[0], c1[0]
        moves = [np.array([0, -1]), np.array([0, 1]), np.array([-1, 0]), np.array([1, 0])]

        for move in moves:
            r2, c2 = r1 + move[0], c1 + move[1]
            if 0 <= r2 < 3 and 0 <= c2 < 3:#validating the moves
                new_state = current_state.copy()
                new_state[r1, c1], new_state[r2, c2] = new_state[r2, c2], new_state[r1, c1]
                if not np.all(visited==new_state):#checking visited
                    visited.append(new_state)
                    queue.append([new_state,operations+[new_state]])
    return None

init = np.array(list(map(int,input("Enter the initial state: ").split()))).reshape(3,3)
print(init)
goal = np.array(list(map(int,input("Enter the goal state: ").split()))).reshape(3,3)

#example input
# init = np.array([0,1,2,3,4,5,6,7,8]).reshape(3,3)
# print(init)
# goal = np.array([3,0,1,6,4,2,7,8,5]).reshape(3,3)

ops=bfsFindGoal(init,goal)
if ops:
    for i in ops:
        print("   |")
        print("   V")
        print(i)
else:
    print(None)# prints after checking all the states which take a lot of time

