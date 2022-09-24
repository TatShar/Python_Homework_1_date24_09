#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

print('Input x: ')
x = int (input())
print('Input y: ')
y = int (input())
if x==0 and y==0:
    print ('x and y should not equal 0')
elif x==0:
    print ("The point is on y-axis")
elif x>0 and y>0:
    print ('The point is in first quarter')
elif y==0:
    print ('The point is on x-axis')
elif x>0 and y<0:
    print ('The point is int second quater')
elif x<0 and y<0:
    print ('The point is in third quater')
else:
    print ('The point is in fourth quarter')
