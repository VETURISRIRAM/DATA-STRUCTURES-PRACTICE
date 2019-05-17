def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    
    i = 0
    j = 0
    
    while i < len(haystack) and j < len(needle):
        if haystack[i] == needle[j]:
            start = i
            i += 1
            j += 1
        else:
            i += 1
            
    print(start - len(needle) + 1)


print(strStr('hellelo', 'ee'))