print("---- simple calculator ----")
print("Let's add some numbers")
f_v =input("Input your first value : ")
s_v = input("Input your second value : ")
op = input("Input your operator : ")
f_v = float(f_v)
s_v = float(s_v)
if(op == "+") :
 print(f"{f_v} + {s_v} = {f_v + s_v}")
elif(op == "-") :
 print(f"{f_v} - {s_v} = {f_v - s_v}")
elif(op == "*") :
 print(f"{f_v} * {s_v} = {f_v * s_v}")
elif(op == "/") :
 print(f"{f_v} / {s_v} = {f_v / s_v}")
else :
 print("the operator must be'*' or '+' or '-' or '/'")
