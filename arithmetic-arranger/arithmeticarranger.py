def arithmetic_arranger(problems, show_answers=False):
    arranged_problems = ""
    first_line = ""
    second_line = ""
    dash_line = ""
    answer_line = ""

    # Validate the number of problems
    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        parts = problem.split()

        # Validate the format of the problem
        if not (parts[0].isdigit() and parts[2].isdigit()):
            return "Error: Invalid format."

        operand1 = parts[0]
        operator = parts[1]
        operand2 = parts[2]

        # Validate the length of the operands
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(operand1), len(operand2)) + 2

        first_line += operand1.rjust(width)
        second_line += operator + operand2.rjust(width - 1)
        dash_line += "-" * width

        if show_answers:
            if operator == "+":
                answer = str(int(operand1) + int(operand2))
            elif operator == "-":
                answer = str(int(operand1) - int(operand2))
            else:
                return "Error: Invalid operator."

            answer_line += answer.rjust(width)

        # Add spacing between problems
        if problem != problems[-1]:
            first_line += "    "
            second_line += "    "
            dash_line += "    "
            answer_line += "    "

    arranged_problems = "\n".join([first_line, second_line, dash_line, answer_line if show_answers else dash_line])
    return arranged_problems


# Example usage
problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
print(arithmetic_arranger(problems, True))
