# -*- coding: utf-8 -*-
#FizzBuzz

select = int(raw_input("Vnesi število med 1 in 100: "))

for x in range(1,select + 1):
    if x % 3 == 0 and x % 5 != 0:
        print "fizz"
    elif x % 5 == 0 and x % 3 !=0:
        print "buzz"
    elif x % 3 == 0 and x % 5 == 0:
        print "fizzbuzz"
    else:
        print x

