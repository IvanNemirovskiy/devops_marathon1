f_str = input("Enter your first string: ")
s_str = input("Enter your second string: ")
c_str = input("Enter your command: ")
if(c_str == "find") :
 f = f_str.find(s_str)
 print(bool(f))
elif(c_str == "concat") :
 print(f"Your string is: {f_str + s_str}")
elif(c_str == "beatbox") :
 b_num1 = input("Enter your first beatbox number: ")
 b_num2 = input("Enter your second beatbox number: ")
 b_num1 = int(b_num1)
 b_num2 = int(b_num2)
 print(f_str * b_num1 +  s_str * b_num2)
elif(f_str or s_str  == "" | c_str != "find" or "concat" or "beatbox") :
 print("One of the strings is empty or usage: command find | concat | beatbox")
