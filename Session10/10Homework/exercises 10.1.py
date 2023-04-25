numList = [1, 2, 3, 4, 5]


#point a
def fun_list_sum():
    sum = 0
    for i in numList:
        sum += i
    return sum


print(fun_list_sum())

# point b
def fun_list_sum_lambda():
    lambda_add = lambda x, y: x + y
    sum = 0
    for i in numList:
        sum = lambda_add(sum, i)
    return sum

print(fun_list_sum_lambda())


