def method_of_middle_square(x, i):
    answer = []
    while i > 0:
        x = int(x)*int(x)
        while len(str(x)) < 8:
            x = "0" + str(x)
        x = str(x)[2:-2]
        i -= 1
        answer.append(x)
    return answer


def linear_konguer_method(A, m, k, i):
    answer = []
    while i > 0:
        A = (k*A)%m
        z = float(A) / float(m)
        answer.append(z)
        i -= 1
    return answer


print method_of_middle_square(1994, 20)
print linear_konguer_method(5, 7, 19, 10)
