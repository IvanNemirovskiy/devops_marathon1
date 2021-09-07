import re

#r"[^@]+@[^@]+\.[^@]+"


def oper_validation(operator: str) -> bool:
    if operator == "add" or operator == "update" or operator == "delete":
        return True
    else:
        return False


def info_validation(dict1: dict) -> bool:
    for key in dict1:
        dict1_str = str(dict1[key])
        pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.\.[A-Z|a-z]{2,}\b"
        if key == 'name' and not re.match(r"[\w\s]+", dict1_str):
            return False
        elif key == 'email' and not re.match(pattern, dict1_str):
            return False
        elif not dict1.get('name') or not dict1.get('email'):
            return False
        else:
            return True


def contacts(container: dict, info: dict, operation: str) -> bool:
    if oper_validation(operation) and info_validation(info) \
            and isinstance(container, dict) and isinstance(info, dict):
        new_key = info.pop('email')

        if operation == 'add':
            container.update({new_key: info})
        if operation == 'update' or 'delete':
            if not container.get(new_key):
                return False
            if operation == 'update':
                container.get(new_key).update(info)
            if operation == 'delete':
                container.pop(new_key)
            return True
    else:
        return False

