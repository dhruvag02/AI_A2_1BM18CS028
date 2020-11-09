# Only two locations exist A/B
# Each location has only two state - Clean(0)/Dirty(1)


def vacuum_world():
    goal_state = {'A': '0', 'B': '0'}  # Everything is clean
    state = {'A': '0', 'B': '0'}
    cost = 0

    location = input("Enter location of vacuum cleaner: ")
    status = input("Enter status of location where vacuum cleaner is placed: ")
    status_complement = input("Enter status of other location: ")
    state[location] = status
    if location == 'A':
        location_complement = 'B'
    else:
        location_complement = 'A'
    state[location_complement] = status_complement
    print("\n")
    print("Initial Location condition: " + str(state))

    if location == 'A':
        # Location A is dirty
        print("Vacuum Cleaner is placed in location A")
        if status == '1':
            print("Location A is dirty")
            # Suck the dirt and mark it as clean
            state['A'] = '0'
            cost += 1
            print("Cost for cleaning A " + str(cost))
            print("Location A has been cleaned")

            if status_complement == '1':
                # If B is dirty
                print("Location B is dirty")
                print("Moving right to location B")
                cost += 1
                print("Cost for moving right " + str(cost))
                # Suck the dirt and make it clean
                state['B'] = 0
                cost += 1
                print("Cost for suck " + str(cost))
                print("Location of B has been cleaned")
            else:
                print("No action " + str(cost))
                print("Location B is already clean")

        if status == '0':
            print("Location A is already clean")
            if status_complement == '1':
                print("Location B is dirty")
                print("Moving  right to location B")
                cost += 1
                print("Cost for moving right " + str(cost))
                state['B'] = '0'
                cost += 1
                print("Cost for suck " + str(cost))
                print("Location B has been cleaned")
            else:
                print("No action required " + str(cost))
                print(cost)
                print("Location B is already clean")

    else:
        print("Vacuum is placed in location B")
        if status == '1':
            print("Location B is dirty")
            state['B']='0'
            cost += 1
            print("Cost for cleaning " + str(cost))
            print("Location B has been cleaned")

            if status_complement == '1':
                print("Location A is dirty")
                print("Moving left to location A")
                cost += 1
                print("Cost for moving left " + str(cost))
                state['A'] = '0'
                cost += 1
                print("Cost for suck " + str(cost))
                print("Location A has been cleaned")

        else:
            print(cost)
            print("Location B is already clean")
            if status_complement == '1':
                print("Location A is dirty")
                print("Moving left to location A")
                cost += 1
                print("cost for moving left " + str(cost))
                state['A'] = '0'
                cost += 1
                print("Cost for suck " + str(cost))
                print("Location A has been cleaned")
            else:
                print("NO action " + str(cost))
                print("Location A is already clean")

    print("Goal State")
    print(str(goal_state))
    print()
    print("State")
    print(str(state))
    print("Performance measurement: " + str(cost))


vacuum_world()