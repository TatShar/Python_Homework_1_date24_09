#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

print ('Input x:')
x = int (input())
print ('Input y:')
y = int (int(input()))
print ('Input x1:')
x1 = int (input())
print ('Input y1:')
y1 = int (input())
d1=((x1-x)**2 +(y1-y)**2)**0.5
print (f'Distance is {round(d1,2)}')