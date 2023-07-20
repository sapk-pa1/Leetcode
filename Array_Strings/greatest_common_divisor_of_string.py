



def gcdOfStrings( str1: str, str2: str) -> str:
    result = [] 
    len_str1 = len(str1)
    len_str2 = len(str2)
    min_str = min(len_str1, len_str2) # Since the gcd is divisible in both the big and small string 

    for i in range(min_str): 
        if (str1[i]==str2[i]) and (str1[i] not in result ): 
            result.append(str1[i])
            # print(result)
    return ''.join(result)





    



str1 = "ABABAB"
str2 = "ABAB"


print(gcdOfStrings(str1, str2))