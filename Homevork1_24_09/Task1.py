 #Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

print ('Input a number: ')
a = int (input ())
if a == 6 or a==7:
    print ('This day will be a weekand')
elif a>7 or a<1:
    print ('There is no such day of the week')
else:
    print ('This day will not be a weekand')