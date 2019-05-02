#Print Fibonacci Numbers
#Print only Even Fibbonacci Numbrers

#current_fib = 0
fib_list = [0] * 100
even_fib_list = [0]*100
fib_list_report = [0] * 40

#Assume the following: 
fib_list[0] = 0
fib_list[1] = 1
fib_list[2] = 1
fib_list[3] = 2
i = 4
j = 0

for i in range(4,100): 
  #while j < 100:

    fib_list[i] = fib_list[i-1] + fib_list[i-2]
    if fib_list[i] % 2 == 0:
        even_fib_list[j]= fib_list[i]
        j+=1

#print(fib_list_report)


print(fib_list)

print('\nCurrent fib num is: ' + str(fib_list[len(fib_list)-1]))

print('\nEven Fib List: \n')
print(even_fib_list)

import numpy
a = numpy.trim_zeros(even_fib_list)

print('\nNew trimmed Even List: ' )
print(a)
