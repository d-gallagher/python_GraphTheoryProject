# David Gallagher
# Shunting Yard Alg
# www.oxfordmathcenter.com/drupal7/node/628

def shunt(infix):

    # need to add other operators here + ? and set precedence
    priorityOps = {'*':50, '+':45, '?':45, '.':40, '|':30}

    postFx = "" #string output    
    stack = "" #stack of chars, operators and parenthesis

    #loop through infix string
    for c in infix:
        if c == '(':
            # if opening parenthesis, push to stack
            stack = stack + c
        elif c == ')':
            # loop until closing parenthesis is found
            while stack[-1] != '(':
                # concat next char on stack to string
                postFx = postFx + stack[-1]
                # pop the char from stack
                stack = stack[:-1]
            # remove closing parenthesis from the stack
            stack = stack[:-1]

        elif c in priorityOps:
            # if theres an operator, push to stack after popping lower or equal precedence operators from top of stack output
            while stack and priorityOps.get(c, 0) <= priorityOps.get(stack[-1], 0):
                # get the special character from the dict
                # concatenate the next character on the stack
                # to the return string
                postFx = postFx + stack[-1]
                # pop the char from the stack
                stack = stack[:-1]

            stack = stack + c
        else:
            # push any regular chars to return string
            postFx = postFx + c

    while stack:
        # pop the remaining operators from the stack
        postFx= postFx + stack[-1]

        stack = stack[:-1]

    return postFx
print("shunt test - (a.b)|(c*d)" +" " + shunt("(a.b)|(c*d)"))
#print(shunt("(a.b)|(c*d)"))


# Thompsons Construction 
# https://swtch.com/~rsc/regexp/regexp1.html

# State w/Two arrows, labeled by the label.
# Using 'None' for a label representing 'e'arrows.
class state:
    label = None
    edge1 = None
    edge2 = None

# An NFA is represented by its initial and accept states.
class nfa:
    initial = None
    accept = None

    #nfa conctructor
    #More convenient to set values of initial and accept w/constructor
    def __init__(self, initial, accept):
        self.initial = initial
        self.accept = accept

def compile(pofix):
    nfaStack = []

    for c in pofix:
        # Operator - Concatenate
        if c == '.':
            # Pop two nfa's off the stack
            nfa2 = nfaStack.pop()
            nfa1 = nfaStack.pop()

            #Connect the first NFA's accept state's to the second's initial state
            nfa1.accept.edge1 = nfa2.initial

            # Push to the stack
            new_nfa = nfa(nfa1.initial, nfa2.accept)
            nfaStack.append(new_nfa)
        
        # Operator - OR 
        elif c == '|':
            #Pop two nfa's off the stack
            nfa2 = nfaStack.pop()
            nfa1 = nfaStack.pop()

            #Create a new initial state
            #Connect to initial states of the nfa's popped from stack
            initial = state()
            initial.edge1 = nfa1.initial
            initial.edge2 = nfa2.initial

            #Create new accept state
            #Connect the accept states of the two nfa's popped from the stack, to newly created accept state
            accept = state()
            nfa1.accept.edge1 = accept
            nfa2.accept.edge1 = accept

            #push new nfa to stack
            new_nfa = nfa(nfa1.initial, nfa2.accept)
            nfaStack.append(new_nfa)

        # Operator - 0 or more
        elif c == '*':
            #pop single nfa from the stack
            nfa1 = nfaStack.pop()
            #create new init and accept state
            initial1 = state()
            accept1 = state()
            #join new initial state to nfa's initial state and the new accept state
            initial1.edge1 = nfa.initial
            initial1.edge2 = accept1
            #join the old accept state to the new accept, and nfa1's initial state
            nfa1.accept.edge1 = nfa1.initial
            nfa1.accept.edge2 = accept1
            #push new nfa to stack
            new_nfa = nfa(initial1, accept1)
            nfaStack.append(new_nfa)
        
        # Operator - 1 or more
        elif c == '+':
            #pop single nfa from the stack
            nfa1 = nfaStack.pop()
            #create new init and accept state
            initial1 = state()
            accept1 = state()
            #join new initial state to nfa's initial state and the new accept state
            initial1.edge1 = nfa.initial
            
            #join the old accept state to the new accept, and nfa1's initial state
            nfa1.accept.edge1 = nfa1.initial
            nfa1.accept.edge2 = accept1
            #push new nfa to stack
            new_nfa = nfa(initial1, accept1)
            nfaStack.append(new_nfa)
        

        # Handle all non special characters
        else:
            #new states for accept and initial
            accept = state()
            initial = state()

            #set initial state vars(pointers)
            initial.label = c
            initial.edge1 = accept

            #new instance of nfa class - send initial and accept using constructor
            new_nfa = nfa(initial, accept)
            nfaStack.append(new_nfa)

    return nfaStack.pop()


def followes(state):
    """
    Returns the state or set of states which can be reached from a state by following 'E' arrows.
    """
# Create a new set with only a state as a member
    states = set()
    states.add(state)

    #Check if state has arrows labelled e leading out of it
    if state.label is None:
        #if there's an edge 1 - follow
        if state.edge1 is not None:
            states |= followes(state.edge1)
        #if there's an edge 2 - follow
        if state.edge2 is not None:
            states |= followes(state.edge2)
    
    # return the set of states
    return states


""" Match compiles the infix regular expression to postfix and creates an NFA from it.
    Sets up two empty sets of states both present and future states will be located here.
    Present set is comprised of any state we land in after following e-arrows from the initial state.
    We can now take a string and loop through it to find all states we can access from that character in the string.
    Repeat for each character in the string.
"""
def match(infix, string):
    # shunt and compile the regex..
    pofix = shunt(infix)
    nfa = compile(pofix)

    # Present and future set of states
    present = set()
    future = set()

    #Add initial state to the present set
    present |= followes(nfa.initial)

    #loop through each char in string s
    for s in string:
        #loop through the present set of states
        for c in present:
            #check if any are labelled 's'
            if c.label == s:
                future |= followes(c.edge1)
        #Set present to future and reset future to empty
        present = future
        future = set()
    
    #check if accept state is in the current set of states
    return (nfa.accept in present)

print(match("a.b.c", "abc"))
print(match("a+b.c", "abc"))
#print(match("a?b.c", "abc"))
print(match("a*b.c", "abc"))
print(match("a|b.c", "abc"))


