"""Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь
ввёл число 3. Считаем 3 + 33 + 333 = 369"""


n = input("Please enter a number: ")
a = n + (n + n) + (n + n + n)
b = int(n) + int(n + n) + int(n + n + n)
n_sum = b
print("Answer: ", n_sum, sep="")

n = input("Enter an integer: ")

print(f"{n} + {n + n} + {n + n +n} = {int(n) + int(n +n) + int(n + n +n)}")