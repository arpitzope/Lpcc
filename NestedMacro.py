with open('MACRO.asm') as f:
    CODE = f.readlines()

lines = []

MNT = []
MDT = []
IC = []
TC = []

for line in CODE:
    line = line.strip("\n")
    lines.append(line)

def addEntryInMNT(line):
    line = line.replace(',', ' ')
    line = line.split()
    entry = {
        'name': line[1],
        'noOfPara': len(line) - 2
    }
    MNT.append(entry)

FvPPL = []

def addFvPPL(line):
    line = line.split()
    entry = []
    c=0
    for i in range(len(line)-2):
        entry.append([line[i+2], f'#{c+1}'])
        c += 1
    entry = {
        'name': line[1],
        'fvppl': entry
    }
    FvPPL.append(entry)

def addMDT(line, nameOfMACRO):
    paraList = []
    mdtEntry = []
    for entry in FvPPL:
        if entry['name'] == nameOfMACRO:
            paraList = entry['fvppl']
    line = line.split()
    mdtEntry.append(line[0])
    
    for i in range(1, len(line)):
        flag = 0
        for para in paraList:
            if para[0] == line[i]:
                flag = 1
                mdtEntry.append(para[1])
        if flag == 0:
            mdtEntry.append(line[i])
                
    entry = {
        'name': nameOfMACRO,
        'mdtEntry': mdtEntry
    }

    MDT.append(entry)


flag = 0
IC = []
newFile = open('IC.txt', 'w')
for line in lines:
    # MNT entry ke liye
    if 'MACRO' in line:
        addEntryInMNT(line)
        addFvPPL(line)
    
    if 'MACRO' in line:
        flag = 1
    
    if 'MEND' in line:
        flag = 0
        continue
    
    if flag == 0:
        IC.append(line)
        line = line + '\n'
        newFile.write(line)

    if flag == 1 and 'MACRO' in line:
        line = line.split()
        mdt = line[1]
    
    if flag == 1 and 'MACRO' not in line: 
        addMDT(line, mdt)

# print("MNT:\n ", MNT)
print("MDT:\n ", MDT)

newFile.close()

with open('IC.txt') as f:
    CODE = f.readlines()
    
for line in CODE:
    line = line.strip('\n')
    line = line.split()
    IC.append(line)

# print("IC:\n ",IC)

