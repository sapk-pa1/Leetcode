


def mergeAlternately( word1: str, word2: str) -> str:
    """Returns the Merged String from the given two strings

    Args:
        word1 (str): string1 
        word2 (str): string2 

    Returns:
        str: merged string from word1 and word2 
    """
    # help(max)
    len_word1 = len(word1)
    len_word2 = len(word2)
    iter_n = min(len_word1, len_word2)
    res_list = []
    for i in range(iter_n): 
        res_list.append(word1[i])
        res_list.append(word2[i])
    # This will only append from the remaining letter if exist else there will be blank
    res_list.append(word1[iter_n:])
    res_list.append(word2[iter_n:])
    return "".join(res_list)



word1 = "ab"
word2 = "pqrs"

print(mergeAlternately(word1, word2))