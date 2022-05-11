import numpy as np

ALLOWED_CHARS = ['+', '-', '/', '*', '^', ' ', '(', ')', \
                '0', '1', '2', '3', '4', '5', '6', '7' ,'8' ,'9', '.']

def evaluateExpression(expr, lowerBound, upperBound, variableName = 'x', step=1/100):
    """
        Evaluating mathematical expression for the range of values between lowerBound to upperBound (inclusive)
    """

    # Validate input values
    if lowerBound >= upperBound:
        raise ValueError("lowerBound: {} must be greater than upperBound: {}".format(lowerBound, upperBound))
    if not expr:
        raise ValueError('Expression can not be left empty')
    for char in expr:
        if not (char >= 'a' and char <= 'z') and char not in ALLOWED_CHARS:
            raise SyntaxError('invalid expression')
    if '**' in expr or '//' in expr:
        raise SyntaxError('invalid expression')

    expr = expr.replace('^', '**')

    outputValues = np.asarray(1)
    inputValues = np.arange(lowerBound, upperBound + step, step=step)
    noOfPoints = inputValues.size

    if variableName not in expr:
        # Expression evaluates to constant
        outputValues = np.full(noOfPoints, eval(expr))
    else:
        outputValues = eval(expr, {}, {variableName: inputValues})

    return (inputValues, outputValues)

