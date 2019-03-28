def shunt(infix):

    # need to add other operators here + ? and set precedence
    priorityOps = {'*':50, '?':45, '+':45, '.':40, '|':30}

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
# shunt test
print(shunt("(a.b)|(c*d)"))
print(shunt("(a+b)|(c*d)"))
print(shunt("(a?b)|(c*d)"))
