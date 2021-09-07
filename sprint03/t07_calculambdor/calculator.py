operations = {"add": lambda num1, num2: num1 + num2,
              "sub": lambda num1, num2: num1 - num2,
              "mul": lambda num1, num2: num1 * num2,
              "div": lambda num1, num2: num1 / num2,
              "pow": lambda num1, num2: num1 ** num2}


def calculator(op, num1, num2):
    if op not in operations:
        raise ValueError("Invalid operation. Available operations: add, sub, mul, div, pow.")
    elif not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Invalid numbers. Second and third arguments must be numerical.")
    else:
        return operations[op](num1, num2)
