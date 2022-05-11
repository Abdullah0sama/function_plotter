from EvalExpr import evaluateExpression
import unittest
# evaluteExpression tests

class test_evaluateExpression(unittest.TestCase):

    def test_variableNames(self):
        with self.assertRaises(NameError):
            evaluateExpression('xx', 0, 1, 'x')
        with self.assertRaises(NameError):
            evaluateExpression('xx', 0, 1, 'x')
        with self.assertRaises(NameError):
            evaluateExpression('x + y', 0, 1, 'x')
        with self.assertRaises(NameError):
            evaluateExpression('max', 0, 1,)
            
    def test_invalidExpression(self):
        with self.assertRaises(SyntaxError):
            evaluateExpression('x.', 0, 1)
        with self.assertRaises(SyntaxError):
            evaluateExpression('/8', 0, 1)
        with self.assertRaises(SyntaxError):
            evaluateExpression('/*', 0, 1)
        with self.assertRaises(SyntaxError):
            evaluateExpression(' ', 0, 1)
        with self.assertRaises(SyntaxError):
            evaluateExpression('', 0, 1)

    def test_invalidValues(self):
        with self.assertRaises(ValueError):
            evaluateExpression('x', 5, 0)

if __name__ == '__main__':
    unittest.main()