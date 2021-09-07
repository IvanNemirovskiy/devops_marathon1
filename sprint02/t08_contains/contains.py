import re

def contains(str1, sub_str):
    result = []
    if isinstance(str1, str) and isinstance(sub_str, list):
        for i in sub_str:
            if(isinstance(i, str)) and re.search(i, str1 ,re.IGNORECASE):
                result.append(i)
    return result
