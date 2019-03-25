# David Gallagher
# Shunting Yard Alg
# www.oxfordmathcenter.com/drupal7/node/628

def shunt(infix):

    priorityOps = {'*':50, '.':40, '|':30}

    postFx = ""
    stack = ""

    for c in infix:
        if c == '(':
            stack = stack + c
        elif c == ')':
            while stack[-1] != '(':
                postFx, stack = postFx + stack[-1], stack[:-1]
            stack = stack[:-1]
        elif c in priorityOps:
            while stack and priorityOps.get(c, 0) <= priorityOps.get(stack[-1], 0):
                postFx, stack = postFx + stack[-1], stack[:-1]
            stack = stack + c
        else:
            postFx = stack + c

    while stack:
        postFx, stack = postFx + stack[-1], stack[:-1]

    return postFx

print(shunt("(a.b)|(c*d)"))