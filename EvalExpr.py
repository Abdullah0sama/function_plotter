import numpy as np

ALLOWED_CHARS = ['+', '-', '/', '*', '^', 'x', ' ', '(', ')', \
                '0', '1', '2', '3', '4', '5', '6', '7' ,'8' ,'9', '.']

def evaluateExpression(expr, lowerBound, upperBound, step=1/100):
    """
        Evaluating mathematical expression for the range of values between lowerBound to upperBound (inclusive)
    """

    # Validate input values
    if lowerBound >= upperBound:
        raise ValueError("lowerBound: {} must be greater than upperBound: {}".format(lowerBound, upperBound))
    if not expr:
        raise ValueError('Expression can not be left empty')
    for char in expr:
        if char not in ALLOWED_CHARS:
            raise SyntaxError('Using invalid characters in expression')
    if '**' in expr:
        raise SyntaxError('Using invalid characters in expression')

    expr = expr.replace('^', '**')

    outputValues = np.asarray(1)
    inputValues = np.arange(lowerBound, upperBound + step, step=step)
    noOfPoints = inputValues.size

    if 'x' not in expr:
        # Expression evaluates to constant
        outputValues = np.full(noOfPoints, eval(expr))
    else:
        outputValues = eval(expr, {}, {'x': inputValues})

    return (inputValues, outputValues)

