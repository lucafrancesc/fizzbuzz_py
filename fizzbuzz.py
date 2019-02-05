def fizz_buzz(num):
    if num == 0:
        return num

    if num % 15 == 0:
        return 'FizzBuzz'

    if num % 5 == 0:
        return 'Buzz'

    if num % 3 == 0:
        return 'Fizz'

    return num

print fizz_buzz(-6)
