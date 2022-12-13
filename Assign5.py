input_expression = "a = b * c + d % e + f + g"
print("\nInput Expression: ")
print(input_expression)
print()
arithmetic = ["+", "-", "/", "*", "%", "^"]
extra = ["if", "else"]
assign = ["="]
res = []
id = 1
temp1 = ""
expression = input_expression
if expression[0] not in extra:
    x = expression.split()
    temp0 = x[-2]
    x[-2] = "$"
    i = 2
    while x[i] != "$":
        if x[i] in arithmetic:
            if x[i+1].startswith("-"):
                temp = "T" + str(id) + "=" + x[i+1]
                res.append(temp)
                del x[i+1]
                x.insert(i+1, "T"+str(id))
                id += 1
        i += 1
    x[-2] = temp0
    while len(x) > 3:
        if x[2].startswith("-"):
            temp = "T" + str(id) + "=" + x[2]
            res.append(temp)
            del x[2]
            x.insert(2, "T" + str(id))
            id += 1
        elif "+" in x:
            oper = x.index('+')
            temp = "T" + str(id) + "=" + x[oper-1] + " " + x[oper] + " " + x[oper+1]
            res.append(temp)
            for i in range(3):
                del x[oper-1]
            x.insert(oper-1, "T"+str(id))
            id += 1
        elif "-" in x:
            oper = x.index('-')
            temp = "T" + str(id) + "=" + x[oper-1] + " " + x[oper] + " " + x[oper+1]
            res.append(temp)
            for i in range(3):
                del x[oper-1]
            x.insert(oper-1, "T"+str(id))
            id += 1
        elif "/" in x:
            oper = x.index('/')
            temp = "T" + str(id) + "=" + x[oper-1] + " " + x[oper] + " " + x[oper+1]
            res.append(temp)
            for i in range(3):
                del x[oper-1]
            x.insert(oper-1, "T"+str(id))
            id += 1
        elif "*" in x:
            oper = x.index('*')
            temp = "T" + str(id) + "=" + x[oper-1] + " " + x[oper] + " " + x[oper+1]
            res.append(temp)
            for i in range(3):
                del x[oper-1]
            x.insert(oper-1, "T"+str(id))
            id += 1
        elif "%" in x:
            oper = x.index('%')
            temp = "T" + str(id) + "=" + x[oper-1] + " " + x[oper] + " " + x[oper+1]
            res.append(temp)
            for i in range(3):
                del x[oper-1]
            x.insert(oper-1, "T"+str(id))
            id += 1
        elif "^" in x:
            oper = x.index('^')
            temp = "T" + str(id) + "=" + x[oper-1] + " " + x[oper] + " " + x[oper+1]
            res.append(temp)
            for i in range(3):
                del x[oper-1]
            x.insert(oper-1, "T"+str(id))
            id += 1
    for i in x:
        temp1 = str(i) + ""
res.append(temp1)
print("\nGenerated Three Address Code:")
for i in res:
    print(i)
f=open("Output.txt","w")
f.write("\n".join(res))
f.close()






























































