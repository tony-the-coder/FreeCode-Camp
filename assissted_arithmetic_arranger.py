def arithmetic_arranger(problems, final_answer=True):
    if len(problems) > 5:
        return "Error: Too many problems"

    first_number = []
    operator = []
    second_number = []

    for problem in problems:
        problem = problem.split()

        first_number.append(problem[0])
        operator.append(problem[1])
        second_number.append(problem[2])

    if "*" in operator or "/" in operator:
        return "Error: Operator must be '+' or '-'."

    if not all(
        x.isdigit() and y.isdigit() for x, y in zip(first_number, second_number)
    ):
        return "Error: Numbers must only contain digits."

    if not all(
        map(lambda x, y: len(x) < 5 and len(y) < 5, first_number, second_number)
    ):
        return "Error: Numbers cannot be more than four digits."

    formatted_problems = []

    for x, y, z in zip(first_number, operator, second_number):
        length = max(len(x), len(z)) + 2
        first_line = x.rjust(length)
        second_line = y + z.rjust(length - 1)
        dashes = "-" * length

        if y == "+":
            answer = str(int(x) + int(z))
        elif y == "-":
            answer = str(int(x) - int(z))

        answer_line = answer.rjust(length)

        if final_answer:
            formatted_problems.append([first_line, second_line, dashes, answer_line])
        else:
            formatted_problems.append([first_line, second_line, dashes])
    print(formatted_problems)
    first_line = "    ".join([problem[0] for problem in formatted_problems])
    second_line = "    ".join([problem[1] for problem in formatted_problems])
    dashes = "    ".join([problem[2] for problem in formatted_problems])

    if final_answer:
        answer_line = "    ".join([problem[3] for problem in formatted_problems])
        arranged_problems = (
            first_line + "\n" + second_line + "\n" + dashes + "\n" + answer_line
        )
    else:
        arranged_problems = first_line + "\n" + second_line + "\n" + dashes

    return arranged_problems


print(arithmetic_arranger(["3111 - 6398", "3801 - 2", "45 + 43", "123 + 49"]))
