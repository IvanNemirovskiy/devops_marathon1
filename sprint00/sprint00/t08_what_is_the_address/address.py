first_int = 1000 
second_int = first_int
third_int = 999
print(f"first_int = {first_int} , address is {id(first_int)} ")
print(f"second_int = {second_int} , address is {id(second_int)} ")
print(f"third_int = {third_int} , address is {id(third_int)} ")
print(f"{first_int} is {second_int} = {first_int is second_int}")
print(f"{first_int} is {third_int} = {second_int is third_int}")

