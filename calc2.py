class Operation(object):
    def __init__(self, *args):
        self.data = args

    def operate(self):
        raise NotImplementedError()


class AddOperation(Operation):
    def operate(self):
        return sum(self.data)


class SubtractOperation(Operation):
    def operate(self):
        return sum([self.data[0]]+[-1*x for x in self.data[1:]]) if self.data else 0


class Calculator(Operation):
    def __init__(self, operations):
        self.operations = operations
        
    def calculate(self, *args):
        try:
            calc = self.operations[args[-1]](*args[:-1])
            return calc.operate()
        except KeyError:
            raise OperationInvalidException()
            
class OperationInvalidException(Exception):
    pass


import unittest


class CalculatorTestCase(unittest.TestCase):
    def test_calculator_with_one_operation(self):
        calc = Calculator(
            operations={
                'add': AddOperation
            }
        )
        res = calc.calculate(1, 5, 13, 2, 'add')
        self.assertEqual(res, 21)

    def test_calculator_with_multiple_operations(self):
        calc = Calculator(
            operations={
                'add': AddOperation,
                'subtract': SubtractOperation
            }
        )
        res = calc.calculate(1, 5, 13, 2, 'add')
        self.assertEqual(res, 21)
        res = calc.calculate(13, 3, 7, 'subtract')
        self.assertEqual(res, 3)

    def test_calculator_invoked_with_an_invalid_operation(self):
        calc = Calculator(
            operations={
                'add': AddOperation
            }
        )
        #print (x = calc.calculate(1,2,3, 'multiply'))
        with self.assertRaises(OperationInvalidException):
            res = calc.calculate(1, 5, 13, 2, 'INVALID')
            
            
calctest = CalculatorTestCase()
calctest.test_calculator_with_one_operation()
calctest.test_calculator_with_multiple_operations()
calctest.test_calculator_invoked_with_an_invalid_operation()


class AddOperationTestCase(unittest.TestCase):
    def test_add_operation_with_multiple_arguments(self):
        op = AddOperation(5, 1, 8, 3, 2)
        self.assertEqual(op.operate(), 19)

    def test_add_operation_with_1_arguments(self):
        op = AddOperation(5)
        self.assertEqual(op.operate(), 5)

    def test_add_operation_with_no_arguments(self):
        op = AddOperation()
        self.assertEqual(op.operate(), 0)


class SubtractOperationTestCase(unittest.TestCase):
    def test_subtract_operation_with_multiple_arguments(self):
        op = SubtractOperation(10, 1, 3, 2, 1)
        self.assertEqual(op.operate(), 3)

    def test_subtract_operation_with_1_arguments(self):
        op = SubtractOperation(5)
        self.assertEqual(op.operate(), 5)

    def test_subtract_operation_negative_result(self):
        op = SubtractOperation(5, 3, 3)
        self.assertEqual(op.operate(), -1)

    def test_subtract_operation_with_no_arguments(self):
        op = SubtractOperation()
        self.assertEqual(op.operate(), 0)
test = AddOperationTestCase()
test.test_add_operation_with_multiple_arguments()
test.test_add_operation_with_1_arguments()
test.test_add_operation_with_no_arguments()
test1 = SubtractOperationTestCase()
test1.test_subtract_operation_with_multiple_arguments()
test1.test_subtract_operation_with_1_arguments()
test1.test_subtract_operation_negative_result()
test1.test_subtract_operation_with_no_arguments()
