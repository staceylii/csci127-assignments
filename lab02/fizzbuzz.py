def fizzbuzz(max_value):
    i = 1
    counter = 0

    while i <= max_value:
        if (i % 3 == 0) and (i % 5 == 0):
            print('FizzBuzz')
            counter += 1
        else:
            if (i % 3 == 0):
                print ('Fizz')
            else:
                if (i % 5 == 0):
                    print ('Buzz')
                else:
                    print (i)
            
        i += 1
    return ('FizzBuzz printed ' + str(counter) + ' times.')

print(fizzbuzz(100))