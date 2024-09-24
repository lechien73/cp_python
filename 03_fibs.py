def fibs(n):
    result = [0, 1]
    for i in range(n-2):
        result.append(result[-2] + result[-1])
    return result

if __name__ == '__main__':
    n = int(input('How many Fibonacci numbers do you want? '))
    print(fibs(n))
