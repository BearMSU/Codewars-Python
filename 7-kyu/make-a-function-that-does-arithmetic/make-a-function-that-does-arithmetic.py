import operator
def arithmetic(a, b, operators):
    ops = {"add": operator.add, "subtract": operator.sub, "multiply": operator.mul, "divide": operator.truediv}
    return ops[operators] (a, b)