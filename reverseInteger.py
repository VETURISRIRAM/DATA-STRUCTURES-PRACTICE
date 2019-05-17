def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    
    if x < 10 and x > -10:
        return x
    
    # Handle negative numbers
    flag = 1
    if x < 0:
        flag = 0
        x *= -1
        
    # Store thw reversed integer
    reversed_x = 0
    
    # Reversing the integer
    while x != 0:
        print(x)
        last = x % 10
        reversed_x = (reversed_x * 10) + last
        x = int(x / 10)
        
    # Check bounds and return
    if reversed_x > (2 ** 31) - 1:
        return 0
    else:
        if flag == 1:
            return reversed_x
        else:
            return -1 * reversed_x

print(reverse(123))