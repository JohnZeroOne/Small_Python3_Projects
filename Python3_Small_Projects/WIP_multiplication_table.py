#import itertools

def mult_table(number):
##    h = 0
##    for i in range(number*number):
##        if i == number:
##            h += 1
##            i = 0
##        print i * h

    
##    mlist = [0, 0]
##    while mlist[1] < number:
##        for item1, item2 in mlist:
##            item1 += 1
##            print item1 * item2

## adder = 0
## math = adder * number
##
## print math +1, math+1, math+1

    num_list  = []
    num_list2 = []
    for i in range(number+1):
        num_list.append(i)
    for i in range(number+1):
        num_list2.append(i)

    for i, j in zip(num_list, num_list2):
        print(i * j)
    
    print(num_list * 1)

    print(num_list * 0)

    for i in range(number+1):
        print(num_list[i])
    #print num_list * 2
        
mult_table(9)
