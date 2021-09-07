import json, cmath, re


def quad(a, b, c):
    global formated_equation
    pattern = r"\d+\.\d+1$"
    if isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)) and a != 0:

        equation = f"{a}x^2+{b}x+{c}=0"
        descrim = b ** 2 - 4 * a * c
        sqrt_val = cmath.sqrt(abs(descrim))
        solution1 = (-b + sqrt_val) / (2 * a)
        solution2 = (-b - sqrt_val) / (2 * a)
        r_sol1 = round(solution1.real, 3)
        r_sol2 = round(solution2.real, 3)
        r_descrim = round(float(descrim), 3)
        str_a = str(a)
        str_b = str(b)
        str_c = str(c)
        if r_descrim < 0:
            full_ans = None
        elif r_sol1 == r_sol2:
            full_ans = r_sol1
        elif abs(r_sol2) > abs(r_sol1):
            full_ans = [r_sol2, r_sol1]

        else:
            full_ans = [r_sol1, r_sol2]

        if re.search(pattern, str_a) or re.search(pattern, str_b) or re.search(pattern, str_c):
            formated_equation = equation.replace("+0x", "").replace("+-", "-")
        else:
            formated_equation = equation.replace('1x', 'x').replace("+0x", "").replace("+0", "").replace("+-","-")
        dict1 = {"equation": formated_equation}
        dict2 = {"discriminant": r_descrim, "x": full_ans}
        dict1["solution"] = dict2

        j_dict = json.dumps(dict1, indent=3)

        return j_dict.replace("-0.0", "0.0")
    else:
        return "Cannot generate a quadratic equation."
