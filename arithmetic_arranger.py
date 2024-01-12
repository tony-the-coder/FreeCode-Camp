def arithmetic_arranger(problems, final_answer=True):
    if len(problems) > 5:
        return "Error: Too many problems"

    first_number = []
    operator = []
    second_number = []
    # print(problems)
    for problem in problems:
        problem = problem.split()

        first_number.append(problem[0])
        operator.append(problem[1])
        second_number.append(problem[2])

    # print("Top Row: ", first_number)
    # print("Operator", operator)
    # print("Second Row: ", second_number)

    if "*" in operator or "/" in operator:
        return "Error: Operator must be '+' or '-'."

    if not all(
        x.isdigit() and y.isdigit() for x, y in zip(first_number, second_number)
    ):
        return "Error: Numbers must only contain digits."

    if not all(map(lambda x, y: len(x) and len(y) < 5, first_number, second_number)):
        return "Error: Numbers cannot be more than four digits."
    # print(first_number, "\n", operator, " ", second_number)

    formatted_problems = []

    # for x, y in zip(operator, second_number):
    #     z = x + " " + y + "    "
    #     formatted_problems.append(z)
    #     a = first_number, "\n ", formatted_problems
    # print(a)
    for x, y, z in zip(first_number, operator, second_number):
        length = max(len(x), len(z)) + 2
        first_line = x.rjust(length)
        second_line = y + " " + z.rjust(length - 2)
        dashes = "-" * length
        # I got stuck about here
        if y == "+":
            answer = str(int(x) + int(z))
        elif y == "-":
            answer = str(int(x) - int(z))
            answer_line = answer.rjust(length)
            # answer_line = y + " " + str(answer)
        formatted_problems.append(first_line)
        formatted_problems.append(second_line)
        formatted_problems.append(dashes)
        # print(formatted_problems)
        if final_answer:
            formatted_problems.append(answer_line)
        first_line = "    ".join(formatted_problems[0::4])
        # second_line = "    ".join(formatted_problems[1::4])
        second_line = "    ".join([" ".join(t) for t in formatted_problems[1::4]])
        # second_line = "    ".join(formatted_problems[1::4])
        dashes = "    ".join(formatted_problems[2::4])
        if final_answer:
            answer_line = "    ".join(formatted_problems[3::4])
            arranged_problems = (
                first_line + "\n" + second_line + "\n" + dashes + "\n" + answer_line
            )
        else:
            arranged_problems = first_line + "\n" + second_line + "\n" + dashes
    return arranged_problems


print(arithmetic_arranger(["3111 - 3110", "3801 - 2", "45 - 43", "123 + 49"]))
