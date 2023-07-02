def rpn(tokens: list[str]):
    operators = {"-", "+", "*", "/"}
    operands = []
    for token in tokens:
        if token in operators:
            last_operand = abs(operands.pop())
            first_operand = abs(operands.pop())
            match token:
                case "+":
                    operands.append(first_operand + last_operand)
                case "-":
                    operands.append(first_operand - last_operand)
                case "*":
                    operands.append(first_operand * last_operand)
                case "/":
                    operands.append((first_operand // last_operand))
        else:
            operands.append(int(token))
    return operands.pop()
