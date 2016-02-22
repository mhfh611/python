def is_palindrome(n):
    nss = str(n)
    i = 0
    while(i<len(nss)):
        if(nss[i] == nss[len(nss) - 1 - i]):
            i = i + 1
        else:
            return False                
    if(i == len(nss)):
        return True
    else:
        return False

#Test
output = filter(is_palindrome, range(1,1000))
print(list(output))
