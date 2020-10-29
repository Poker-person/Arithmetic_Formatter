def arithmetic_arranger(problems, solution=False):
    # Check for error: To many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    x1 = ''
    x2 = ''
    x3 = ''
    x4 = ''

    # Split problems and pick operator and operands
    for i, x in enumerate(problems):
        c = x.split(' ')
        num1 = c[0]
        num2 = c[2]
        sig = c[1]

        if sig not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        if not num1.isnumeric() or not num2.isnumeric():
            return "Error: Numbers must only contain digits."

        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Format output
        wid = max(len(num1), len(num2)) + 2
        i1 = num1.rjust(wid)
        i2 = sig + num2.rjust(wid - 1)
        dash = '-' * wid

        # Solve problems
        if sig == '+':
            z = int(num1) + int(num2)
        else:
            z = int(num1) - int(num2)

        x1 += i1
        x2 += i2
        x3 += dash
        x4 += str(z).rjust(wid)

        # insert spaces between problems
        if i < len(problems)-1:
            x1 += '    '
            x2 += '    '
            x3 += '    '
            x4 += '    '

    cy = x1 + "\n" + x2 + "\n" + x3

    if solution:
        cy += "\n" + x4

    return cy
