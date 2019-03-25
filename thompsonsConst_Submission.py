# David Gallagher
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
        
        if c == '.':
            # Pop two nfa's off the stack
            nfa2 = nfaStack.pop()
            nfa1 = nfaStack.pop()

            #Connect the first NFA's accept state's to the second's initial state
            nfa1.accept.edge1 = nfa2.initial

            # Push to the stack
            new_nfa = nfa(nfa1.initial, nfa2.accept)
            nfaStack.append(new_nfa)

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

        elif c == '*':
            #pop single nfa from the stack
            nfa1 = nfaStack.pop()
            #create new init and accept state
            initial1 = state()
            accept1 = state()
            #join new initial state to nfa's initial state and the new accept state
            initial1.edge1 = nfa.initial
            initial1.edge2 = accept
            #join the old accept state to the new accept, and nfa1's initial state
            nfa1.accept.edge1 = nfa1.initial
            nfa1.accept.edge2 = accept
            #push new nfa to stack
            new_nfa = nfa(nfa1.initial, nfa2.accept)
            nfaStack.append(new_nfa)
        else:
            #new states for accept and initial
            accept = state()
            initial = state()

            #set initial state vars(pointers)
            initial.label = c
            initial.edge1 = accept

            #new instance of nfa class - send initial and accept using constructor
            new_nfa = nfa(nfa1.initial, nfa2.accept)
            nfaStack.append(new_nfa)

    return nfaStack.pop()
