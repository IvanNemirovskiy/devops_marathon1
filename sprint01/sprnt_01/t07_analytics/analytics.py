def print_str_analytics(str):
    print("|------------------------------------------------|")
    print("|                String analytics                |")
    print("|------------------------------------------------|")
    print(f"| '{str}'")
    print("|------------------------------------------------|")
    print(f"| Number of printable characters is: {sum(i.isprintable() for i in str)}")
    alpha = alpbet = dec = whitespace = 0
   # d = {"UPPER_CASE": 0, "LOWER_CASE": 0}
    # for i in range(len(str)):
    #     if str[i].isalnum():
    #         alpha += 1
    #     else:
    #         pass
    print(f"| Number of alphanumeric characters is: {sum(s.isalnum() for s in str)}")

    # alpbet = 0
    # for i in range(len(str)):
    #     if str[i].isalpha():
    #         alpbet += 1
    #     else:
    #         pass
    print(f"| Number of alphabetic characters is: {sum(s.isalpha() for s in str)}")

    # dec = 0
    # for i in range(len(str)):
    #     if str[i].isdecimal():
    #         dec += 1
    #     else:
    #         pass
    print(f"| Number of decimal characters is: {sum(s.isdecimal() for s in str)}")


    # for c in str:
    #     if c.isupper():
    #         d["UPPER_CASE"] += 1
    #     elif (c.islower()):
    #         d["LOWER_CASE"] += 1
    #     else:
    #         pass
    print(f"| Number of lowercase letters is: {sum(i.islower() for i in str)}")
    print(f"| Number of uppercase letters is: {sum(i.isupper() for i in str)}")

    # for w in str:
    #     if w == " ":
    #         whitespace += 1
    #     else:
    #         pass
    print(f"| Number of whitespace characters is: {sum(i.isspace() for i in str)}")
    print("|------------------------------------------------|")
