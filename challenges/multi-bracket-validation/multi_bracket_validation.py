from stack import Stack as st


def multi_bracket_validation(input):
    """function check for matching braces"""
    if type(input) is str:
        lefty = '({['
        righty = ')}]'
        tocheck = st()
        
        for item in input:
            if item in lefty:
                tocheck.push(item)
            elif item in righty:
                if tocheck.top is None:
                    return False
                if righty.index(item) != lefty.index(tocheck.pop().val):
                    return False
        return tocheck.top is None
    
    else:
        return False


