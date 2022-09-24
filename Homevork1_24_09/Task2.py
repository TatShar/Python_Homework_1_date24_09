#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

print ('Input number of quater')
quater = int(input())
if quater == 0:
    print ('There is no quater')
elif quater ==1:
    print ('range x>0 and y>0')
elif quater ==2:
    print ('range: x>0 and y<0')
elif quater ==3:
    print ('range: x<0 and y<0')
elif quater ==4:
    print ('range: x<0 and y>0')
