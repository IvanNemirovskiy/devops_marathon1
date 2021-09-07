import re


def check_address(addr: dict) -> bool:
    ret = []
    pattern = r'^Ukraine,[ ]*[A-Za-z-[ ]*]*,[ ]*[A-Za-z-[ ]*]*[ ]*\d{1,6},[ ]*\d{5}$'
    for k in addr:
            if re.match(pattern, addr[k]):
                ret.append(f"The address of {k} is valid.")
            else:
                ret.append(f"The address of {k} is invalid.")
    return ret