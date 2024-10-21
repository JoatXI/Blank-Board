def valid_state(state):
    # checks if it is a valid solution
    return True

def get_candidate(state):
    return []

def search(state, solutions):
    # checks if the current state is a valid solution
    if valid_state(state):
        # adds the state to the solutions list
        solutions.append(state.copy())
        # return  --- we use the return function when
        # we are asked to find all possible solutions
        
        for candidate in get_candidate(state):
            state.add(candidate)
            search(state, solutions)
            state.remove(candidate) # we use the remove function 
                                    # when the state is stored in a set(),
                                    # for array list we use the pop() function

def solve():
    state, solutions = set(), []
    search(state, solutions)
    
    return solutions