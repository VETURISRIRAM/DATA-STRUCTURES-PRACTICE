# print(1 in range(-1, 3))

# # # print(ord('0'))
# # # print(ord('9'))
# # # print(ord(' '))
# # # print(ord('-'))


def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """
    
    if not str:
        return None
    
    flag = 1
    integer = 0
    num_found = False
    
    i = 0
    while i < len(str):
        
        if num_found is True and (ord(str[i]) not in range(48, 58)):
        	break

        else:

        	if str[i] == ' ':
        		print("Space found")
        		i += 1
        		continue

        	elif str[i] == '-':
        		print("Minus found")
        		i += 1
        		flag = 0
        		continue

        	elif ord(str[i]) in range(48, 58):
        		print("Number found")
        		num_found = True
        		integer = integer * 10 + (ord(str[i]) - 48)

        	else:
        		break

        	i += 1
            
    if flag == 1:
    	if integer <= ((2 ** 31) - 1):
    		return integer
    	else:
    		return ((2 ** 31) - 1)
    else:
    	integer = -1 * integer
    	if integer >= -(2 ** 31):
    		return integer
    	else:
    		return -(2 ** 31)


print(myAtoi('-9999999999999999999999999999987'))