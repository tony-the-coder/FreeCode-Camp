def arithmetic_arranger(problems):
    if len(problems) > 5:
        return "Error: Too many problems"

    # Testing to see if compression would work here. I think in the end, it will be more work.
    # problems_size = 1
    # problems_list = [
    #     problems[x : x + problems_size] for x in range(0, len(problems), problems_size)
    # ]

    first_number = []
    operator = []
    second_number = []

    # for problem in problems:
    #     problem = problem.split()
    #     # print(problem)
    #     first_number = problem[0]
    #     operator = problem[1]
    #     second_number = problem[2]
    #     print(first_number, operator, second_number)

    for problem in problems:
        problem = problem.split()

        first_number.append(problem[0])
        operator.append(problem[1])
        second_number.append(problem[2])

    # checking to see if the operator is only a + or a - but this does not look effiecent as there could be something that could have been passed instead of the two operators
    # 1
    # //TODO: #2 Fix the filtery thing down here
    if "*" in operator or "/" in operator:
        return "Error: Operator must be '+' or '-'."


print(arithmetic_arranger(["32 - 698", "3801 - 2", "45 - 43", "123 + 49"]))
