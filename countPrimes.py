def countPrimes(n):
    """
    :type n: int
    :rtype: int
    """
    if n <= 2:
        return 0
    if n == 3:
        return 1

    output = 0
    for num in range(2, n):
        flag = True
        for x in range(2, int(num**(1/2)) + 1):
            if num % x == 0:
                flag = False
        if flag == True:
            output += 1

    return output

print(countPrimes())