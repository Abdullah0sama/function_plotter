from tokenize import Name
import numpy as np

ALLOWED_CHARS = ['+', '-', '/', '*', '^', ' ', '(', ')', \
                '0', '1', '2', '3', '4', '5', '6', '7' ,'8' ,'9', '.']

def evaluateExpression(expr, lowerBound, upperBound, variableName = 'x', step=None):
    """
        Evaluating mathematical expression for the range of values between lowerBound to upperBound (inclusive)
    """
    # Validate input values
    if lowerBound >= upperBound:
        raise ValueError("lowerBound: {} must be greater than upperBound: {}".format(lowerBound, upperBound))
    
    for char in expr:
        if  (char >= 'a' and char <= 'z') and char != variableName:
            raise NameError('Only \'{}\' is accepted as a variable name'.format(variableName))
        elif char != variableName and char not in ALLOWED_CHARS:
            print(char)
            raise SyntaxError('invalid expression')

    if '**' in expr or '//' in expr:
        raise SyntaxError('invalid expression')

    expr = expr.replace('^', '**')

    if step is None:
        step = min(1 / 100, 1 / 100 * (upperBound - lowerBound))   

    outputValues = np.asarray(1)
    inputValues = np.arange(lowerBound, upperBound + step, step=step)
    noOfPoints = inputValues.size

    if variableName not in expr:
        # Expression evaluates to constant
        outputValues = np.full(noOfPoints, eval(expr))
    else:
        outputValues = eval(expr, {}, {variableName: inputValues})

    return (inputValues, outputValues)

