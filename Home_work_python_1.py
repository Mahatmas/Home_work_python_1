# Задача 2: Найдите сумму цифр трехзначного числа. 

a = int(input("Введите трехзначное число: "))
print(a % 10 + a // 10 % 10 + a // 100)

'''Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое
количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?'''

total = int(input('Введите общее число сделанных журавликов: '))
Pety = int(total / 6)
Sereja = int(total / 6)
Katy =  int((Pety + Sereja) * 2)

print(f'Петя сделал: {Pety}, Сережа сделал: {Sereja}, Катя сделала: {Katy}')

'''Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и
получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, 
где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, 
т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.'''

ticket = input('Введите шестизначное число: ')

s1 = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
s2 = int(ticket[3]) + int(ticket[4]) + int(ticket[5])
if s1 == s2:
    print('Счастливый билет')
else:
    print('Обычный билет')

'''Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если
разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).'''

n, m, k = map(int, input('Введите три числа через пробел: ').split())
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')