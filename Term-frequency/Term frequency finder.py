Q = []
D1 = []
D2 = []
D3 = []
D4 = []
Q1R = []
D1R = []
D2R = []
D3R = []
D4R = []
ALLD = []
term = []

Query = list(map(str,input("Enter Query: ").split()))
doc1 = list(map(str,input("Enter doc 1: ").split()))
doc2 = list(map(str,input("Enter doc 2: ").split()))
doc3 = list(map(str,input("Enter doc 3: ").split()))
doc4 = list(map(str,input("Enter doc 4: ").split()))

x1 = len(doc1)
x2 = len(doc2)
x3 = len(doc3)
x4 = len(doc4)

for i in range(x1):
    ALLD.append(doc1[i])
for i in range(x2):
    ALLD.append(doc2[i])
for i in range(x3):
    ALLD.append(doc3[i])
for i in range(x4):
    ALLD.append(doc4[i])
    
for i in ALLD:
    if i not in term:
        term.append(i)

term = sorted(term)
Xt = len(term)
Xq = len(Query)
for i in range(Xt):
    rep = 0
    if term[i] not in Query:
        rep1 = 0 
        Q1R.append(rep1)
    elif term[i] in Query:
        for j in range(Xq):   
            if term[i] == Query[j]:
                rep = rep + 1
                Q1R.append(rep)
for i in range(Xt):
    rep = 0
    if term[i] not in doc1:
        rep1 = 0 
        D1R.append(rep1)
    elif term[i] in doc1:
        for j in range(x1):   
            if term[i] == doc1[j]:
                rep = rep + 1
                if rep >= 2:
                    v = rep - 1
                    for i in range(v):
                        D1R.pop()
                    D1R.append(rep)
                else:
                    D1R.append(rep)
for i in range(Xt):
    rep = 0
    if term[i] not in doc2:
        rep1 = 0 
        D2R.append(rep1)
    elif term[i] in doc2:
        for j in range(x2):   
            if term[i] == doc2[j]:
                rep = rep + 1
                if rep >= 2:
                    v = rep - 1
                    for i in range(v):
                        D2R.pop()
                    D2R.append(rep)
                else:
                    D2R.append(rep)
for i in range(Xt):
    rep = 0
    if term[i] not in doc3:
        rep1 = 0 
        D3R.append(rep1)
    elif term[i] in doc3:
        for j in range(x3):   
            if term[i] == doc3[j]:
                rep = rep + 1
                if rep >= 2:
                    v = rep - 1
                    for i in range(v):
                        D3R.pop()
                    D3R.append(rep)
                else:
                    D3R.append(rep)
for i in range(Xt):
    rep = 0
    if term[i] not in doc4:
        rep1 = 0 
        D4R.append(rep1)
    elif term[i] in doc4:
        for j in range(x4):   
            if term[i] == doc4[j]:
                rep = rep + 1
                if rep >= 2:
                    v = rep - 1
                    for i in range(v):
                        D4R.pop()
                    D4R.append(rep)
                else:
                    D4R.append(rep)

print(term)
print("Q: ", Q1R)
print("D1: ", D1R)
print("D2: ", D2R)
print("D3: ", D3R)
print("D4: ", D4R)
