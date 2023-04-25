# Function definition
def basic_function(x):
    return 3 * x ** - 2 * x + 5


print(f"{basic_function(2)}")


# Pure function
def pure_function(x, y):
    # use only the local function inputs
    return x + y


# Lambda
labmda_add = lambda x, y: x + y


def greeting1(name):
    print('Ciao ', name)


greeting2 = lambda name: print('Ciao ', name)


# random functions
# returns None
def do_nothing_useful(i, j):
    x = i + j
    x = i - j


result = do_nothing_useful(10, 12)
print(result)


# Callback --- GUI

# import sys
#
# from tkinter import Button, mainloop, messagebox, ttk
# import tkinter as tk
#
# win = tk.Tk()
# win.geometry('400x300')
# win.title('LMAO')
#
# combo = ttk.Combobox(
#     state='readonly',
#     values=['iMpEraTive', 'O-O', 'fuNcTioNal', 'DisTriButeD']
# )
#
# combo.place(x=100, y=50)
#
# btn = Button(
#     win, text='LOL click',
#     command=(lambda : messagebox.showinfo(
#         'pArAdiGmN', combo.get() +
#         '\n okay bro'
#     ))
# )
#
# btn.pack()
# win.mainloop()


# Recursion

def add(x, y):
    if x == 0:
        return y
    else:
        return add(x - 1, y + 1)


print(f"{add(3, 2)}")

# Mutable / Immutabale

mutadata = ['Aleksey', 123456, ['PME', 'PCL', 'ALI1']]
immudata = ('Aleksey', 123456, ['PME', 'PCL', 'ALI1'])
# works
mutadata[1] = 111111
print(mutadata[1])
# doesnt work
# immudata[1] = 111111
# print(mutadata[1])


coffee_price = [(2018, 25.05), (2022, 24.08)]

print(max(coffee_price))
# max is 2022
print(max(coffee_price, key=lambda cprice: cprice[1]))
# now its 2018


# adding 1 to every element in a list
list_values = [1, 2, 3, 4, 5, 6, 7]
add_one = list(map(lambda y: y + 1, list_values))
print(add_one)

# odd numbers
odd_num = list(filter(lambda n: n % 2 == 1, list_values))
print(odd_num)

# summ
from functools import reduce

summed_val = reduce(lambda n, m: n + m, list_values)
print(summed_val)

# increase by 1 using comprehension
inc_vlst = [i + 1 for i in list_values]
print(inc_vlst)

# filter even numbers
even_filter = [i for i in list_values if i % 2 == 0]
print(even_filter)

# The sorted() function takes an iterable(list) creates a new iterable map object with the list sorted
gtg_sales = [('Coffee', 2018, 525.05),
             ('Juice', 2021, 526.03),
             ('Apple', 2020, 525.12),
             ('Green Tea', 2019, 525.02),
             ('Banana', 2022, 524.08)]
sorted_in_order = sorted(gtg_sales)
sorted_in_order_years = sorted(gtg_sales, key=lambda a: a[1])
print(sorted_in_order)
print(sorted_in_order_years)


#just exercises
#1

numLst= [1, 2, 3, 4, 5]
def recursive_sum(list):
    if len(list) == 0:
        return 0
    else:
        return list[0] + recursive_sum(list[1:])


recursive_sum_lambda = lambda a: a[0] + recursive_sum_lambda(a[1:]) if len(a) > 0 else 0

print(recursive_sum(numLst))
print(recursive_sum_lambda(numLst))