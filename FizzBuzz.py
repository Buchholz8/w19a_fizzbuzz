numbers = [1,3,6,15,12,23,45,31,60,80,9,11,22,20,42]
def run_math():
        for num in numbers:
                if(num % 5 == 0 and num % 3 == 0):
                        print('FizzBuzz')
                elif(num % 3 == 0):
                        print('Fizz')
                elif(num % 5 == 0):
                        print('Buzz') 
                else:
                        print(num)
run_math()