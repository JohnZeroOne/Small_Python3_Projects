# 5m
# could concatenate "fizz" & "buzz" when both occur

def fizzbuzz(number):
    for i in range(1, number +1):
        if i % 15 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print("i:", i)
   
fizzbuzz(100)
