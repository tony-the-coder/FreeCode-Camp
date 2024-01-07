def arithmetic_arranger(problems):
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
    # 1

    if "*" in operator or "/" in operator:
        return "Error: Operator must be '+' or '-'."

    if not all(
        x.isdigit() and y.isdigit() for x, y in zip(first_number, second_number)
    ):
        return "Error: Numbers must only contain digits."

    if not all(map(lambda x, y: len(x) and len(y) < 5, first_number, second_number)):
        return "Error: Numbers cannot be more than four digits."


print(arithmetic_arranger(["3111112 - 62398", "3801 - 2", "45 - 43", "123 + 49"]))
