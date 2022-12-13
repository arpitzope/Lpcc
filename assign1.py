import pandas as pd
data = {
    "MNEUMONIC": ['STOP', 'ADD', 'SUB', 'MULT', 'MOVER', 'MOVEM', 'COMP', 'BC', 'DIV', 'READ', 'PRINT', 'LOAD', 'START', 'END', 'ORIGIN', 'EQU', 'LTORG', 'DS', 'DC', 'AREG', 'BREG', 'CREG', 'EQ', 'LT', 'GT', 'NE', 'LE', 'GE', 'ANY'],
    "CLASS": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 2, 2, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5],
    "OPCODE": ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '01', '02', '03', '04', '05', '01', '02', '01', '02', '03', '01', '02', '03', '04', '05', '06', '07']
}


emot = pd.DataFrame(data)
ST = {}
global lt
lt = {}
LT = {}
pt = []
iLT = 0
iST = 0
size = 1
C = 0


def getClass(s):
    ind = data['MNEUMONIC'].index(s)
    return data["CLASS"][ind]


def getOpcode(s):
    ind = data['MNEUMONIC'].index(s)
    return data["OPCODE"][ind]


def getLT(l):
    global lt
    for i in l:
        if i.startswith("=") and i not in lt:
            lt[i] = 0


def check(s):
    if s in data['MNEUMONIC']:
        pass
    else:
        if s in lt:
            ans.append(f'(L,{s},{iLT})')
        elif s.isnumeric():
            ans.append(f'(C,{s})')
        else:
            ans.append(f'(S,{s})')


def getST(l):
    if (l[0] not in ST) and l[0] not in data['MNEUMONIC']:
        ST[l[0]] = int(C)


def assignLT(iLT, C):
    global lt
    for i in range(len(lt)):
        lt[list(lt.keys())[i]] = C
        C = int(C)+1
        iLT += 1
    if not lt:
        return C, iLT
    LT[pt[-1]] = lt
    lt = {}
    return C, iLT


def assignpt(iLT):
    pt.append(iLT)


print("Intermediate code: ")
f = open("/Users/arpitzope/Downloads/Output.txt", 'r')
for l in f:
    l = l.strip("\n").replace(",", " ").upper().split(" ")
    ans = []
    getST(l)
    getLT(l)
    if l[0] in data['MNEUMONIC']:
        label = 0
        comm = l[0]
        c = getClass(l[0])
        o = getOpcode(l[0])
    if l[0] in ST:
        label = 1
        comm = l[1]
        c = getClass(l[1])
        o = getOpcode(l[1])
    if c == 1:
        ans.append(f'LC={C}')
        ans.append(f'(IS,{o})')
        C = int(C)+1
    elif c == 2:
        ans.append(f'LC={C}')
        if comm == "DS":
            ans.append('(DL,01)')
            C = int(C)+int(l[(l.index("DS")+1)])
        if comm == "DC":
            ans.append('(DL,02)')
            C = int(C)+1
    elif c == 3:
        if comm == "START":
            ans.append('(AD,01)')
            C = l[(l.index("START"))+1]
        if comm == "ORIGIN":
            ans.append('(AD,03)')
            if l[(l.index("ORIGIN"))+1][0] in ST:
                C = int(ST[l[(l.index("ORIGIN"))+1][0]])
                if l[(l.index("ORIGIN"))+1][1] == '+':
                    C = int(C)+int(l[(l.index("ORIGIN"))+1][2])
                if l[(l.index("ORIGIN"))+1][1] == '-':
                    C = int(C)+int(l[(l.index("ORIGIN"))+1][2])
                if l[(l.index("ORIGIN"))+1][1] == '*':
                    C = int(C)+int(l[(l.index("ORIGIN"))+1][2])
                if l[(l.index("ORIGIN"))+1][1] == '/':
                    C = int(C)+int(l[(l.index("ORIGIN"))+1][2])
            else:
                C = l[(l.index("ORIGIN"))+1]
        if comm == "LTORG":
            ans.append('(AD,05)')
            assignpt(iLT)
            iLT = pt[-1]
            C, iLT = assignLT(iLT, C)
        if comm == "EQU":
            ans.append('(AD,04)')
            if l[l.index("EQU")-1] in lt:
                lt[l[l.index("EQU")-1]] = l[l.index("EQU")+1]
            elif l[l.index("EQU")-1] in ST:
                ST[l[l.index("EQU")-1]] = ST[l[l.index("EQU")+1]]
        if comm == "END":
            ans.append('(AD,02)')
            assignpt(iLT)
            C = assignLT(iLT, C)
            break
    elif c == 4:
        ans.append(f'LC={C}')
        ans.append(f'(RG,{o})')
        C = int(C)+1
    elif c == 5:
        ans.append(f'LC={C}')
        ans.append(f'(CC,{o})')
        C = int(C)+1
    else:
        C = int(C)+1
    for i in range(len(l)):
        if i == 0:
            if label == 0:
                check(l[i])
        else:
            if c == 3 and o not in ['04', '01']:
                pass
            else:
                check(l[i])
    print(" ".join(ans))
PT = list(LT.keys())
print("Symbol Table: ", ST)
print("Literal Table: ", LT)
print("Pool Table: ", PT)
print("Counter: ", C)
