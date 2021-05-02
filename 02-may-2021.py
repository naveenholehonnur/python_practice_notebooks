# check whether paranthisis matched or not in a string

x = "navee((nhol)eh))onnur"
check = 0
for i in x:
    if i == "(":
        check +=1
    elif i == ")":
        check -=1
    if check < 0:
        print(False)
        break
else:
    if check == 0:
        print(True)
    else:
        print(False)


# check whether  parentheses matched or not in a string,if not modify the string

x = list("navee((nhol)eh))onnur")
check = 0
for i in range(len(x)):
    if x[i] == "(":
        check +=1
    elif x[i] == ")":
        check -=1
    if check < 0:
        check +=1
        x[i] = ""
else:
    if check != 0 :
        x.extend([")" for i in range(check)])
    print("".join(x))