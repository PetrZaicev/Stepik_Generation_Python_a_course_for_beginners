# Трехзначное число.
# Напишите программу, в которой рассчитывается сумма и произведение цифр положительного трёхзначного числа.

# Формат входных данных
# На вход программе подаётся положительное трёхзначное число.

# Формат выходных данных
# Программа должна вывести два числа с поясняющим текстом: сумма цифр и произведение цифр.

# put your python code here
num = int(input())
num1 = num % 10
num2 = (num // 10) % 10
num3 = num // 100
print("Сумма цифр =", num1 + num2 + num3)
print("Произведение цифр =", num1 * num2 * num3)
