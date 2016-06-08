import string

def evaluate(rest):

    # only one digit in rest, just return it
    if (len(rest) == 1):
        return rest

    # rest has at least one + operation
    elif ("+" in rest):
 
        # find occurence of first plus sign
        foundplus = string.find(rest,'+')
 
        # call evaluate on the portion of the expression
        # before the +, handling special case where expression
        # is just one digit
        if (foundplus == 1):
            eval1str = rest[0]
        else:
            val1 = rest[:foundplus]
            eval1str = evaluate(val1)

        # call evaluate on the portion of the expression
        # after the +, handling special case where expression
        # is just one digit
        if (foundplus == len(rest)-1):
            eval2str = rest[-1]
        else:
            val2 = rest[foundplus+1:]
            eval2str = evaluate(val2)
        
        # combine evaluated subexpressions with plus
        return eval1str + eval2str + '+'
        
    # rest has only one or more '*'   
    else:
        # break up expression in first value and remaining expression
        # after '*'
        val1 = rest[0]
        new_rest = rest[2:]
        
        # call evaluate on the remaining expression
        eval2str = evaluate(new_rest)
        
        # combine evaluated subexpressions with multiply 
        return val1 + eval2str + '*'

def answer(str):
    # your code here
    return evaluate(str)
    
    
print answer("2+3*2")
print answer("2*4*3+9*3+5")
