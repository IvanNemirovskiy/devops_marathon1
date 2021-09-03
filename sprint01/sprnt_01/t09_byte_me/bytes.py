def convert_to_bytes(pos1, pos2, pos3):
    casted_pos1 = int(pos1)
    casted_pos3 = str(pos3)

    b_int = bytes(casted_pos1)
    b_str = bytes(casted_pos3, 'utf-8')

    print(f'-- The int value is "{pos1}"')
    print(f'bytes: "{b_int}"')
    if(pos2 == "True"):
        print(f'-- The bool value is "{pos2}"')
        print(f'bytes: "{bytes(True)}"')
    else:
        print(f'-- The bool value is "{pos2}"')
        print(f'bytes: "b\'\'"')

    print(f'-- The string value is "{pos3}"')
    print(f'bytes: "{b_str}"')
