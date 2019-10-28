def find_third_side(a, b, perimeter):
    return perimeter - a - b


def is_rectangle(a, b, c):
    return a**2 + b**2 == c**2


def find_solutions(per):
    sol_list = []
    for i in range(1, per):
        for j in range(i, per):
            k = find_third_side(i, j, per)
            if is_rectangle(i, j, k):
                sol_list.append((i, j, k))
    return sol_list



def print_solution(solution_list):
    for el in solution_list:
        msg = "({},{},{})"
        print(msg.format(el[0], el[1], el[2]))


maxCount = 0
for i in range(1, 1001):
    count = len(find_solutions(i))
    if(count > maxCount):
        maxCount = count
        print("Aumentato numero di soluzioni: ", maxCount, "(", i, ")")#, end="\r")
