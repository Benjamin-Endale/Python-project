import math
Q,D1,D2,D3,D4,QW1,DW1,DW2,DW3,DW4,D1M,D2M,D3M,D4M,QM,Df,Dfr,IDf,IDfr,NDr,Q1R,D1R,D2R,D3R,D4R= [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
ALLD,term,rank = [],[],[]
Stop_Word = ["a", "an", "the","i", "he", "she", "it", "their", "his","on", "of", "in", "about", "besides", "against", "over","and", "but", "for", "nor", "or", "so", "yet","is", "are", "was", "were","here", "there", "out", "because", "soon", "after","all", "any", 
             "each", "every", "few", "many", "some",'as','by','down','had','into','its','on','one','the','these','this','through','to','toward','what','who']
Inc = 1
z = 0
print("\n")
print("VSM calculator (version 3.1).")
print("\n")
def QMag():
    mag = 0
    Ql = len(QW1)
    for t in range(Ql):
        a = QW1[t] ** 2
        mag = mag + a
    global magQ 
    magQ = mag ** 0.5
    magQ = round(magQ,3)
    print("|Q|: ",magQ)
def Qcalc():
    for i in range(Xt):
        rep = 0
        if term[i] not in Query:
            rep1 = 0 
            Q1R.append(rep1)
        elif term[i] in Query:
            rep = Query.count(term[i])
            Q1R.append(rep)
def D1Mag():
    mag = 0
    D1l = len(DW1)
    for t in range(D1l):
        a = DW1[t] ** 2
        mag = mag + a
    magD1 = mag ** 0.5
    magD1 = round(magD1,3)
    print("|D1|: ",magD1)
    resDot = 0
    for g in range(Xt):
        Dot = QW1[g] * DW1[g] 
        resDot = resDot + Dot
    resDot = round(resDot,4)
    print("Q*d1: ",resDot)
    Prod = magD1 * magQ
    global simD1
    simD1 =   resDot/Prod
    simD1 = round(simD1,4)
    print("Sim(Q,D1): ",simD1)
def D1calc():
    for i in range(Xt):
        rep = 0
        if term[i] not in doc1:
            rep1 = 0 
            D1R.append(rep1)
        elif term[i] in doc1:
            rep = doc1.count(term[i])
            D1R.append(rep)
def D2Mag():
    mag = 0
    D2l = len(DW2)
    for t in range(D2l):
        a = DW2[t] ** 2
        mag = mag + a
    magD2 = mag ** 0.5
    magD2 = round(magD2,3)
    print("|D2|: ",magD2)
    resDot = 0
    for g in range(Xt):
        Dot = QW1[g] * DW2[g] 
        resDot = resDot + Dot
    resDot = round(resDot,4)
    print("Q*d2: ",resDot)
    Prod = magD2 * magQ
    global simD2
    simD2 =   resDot/Prod
    simD2 = round(simD2,4)
    print("Sim(Q,D2): ",simD2)
def D2calc():
    mag = 0
    for i in range(Xt):
        rep = 0
        if term[i] not in doc2:
            rep1 = 0 
            D2R.append(rep1)
        elif term[i] in doc2:
            rep = doc2.count(term[i])
            D2R.append(rep)
def D3Mag():
    mag = 0 
    D3l = len(DW3)
    for t in range(D3l):
        a = DW3[t] ** 2
        mag = mag + a
    magD3 = mag ** 0.5
    magD3 = round(magD3,3)
    print("|D3|: ",magD3)
    resDot = 0
    for g in range(Xt):
        Dot = QW1[g] * DW3[g] 
        resDot = resDot + Dot
    resDot = round(resDot,4)
    print("Q*d3: ",resDot)
    Prod = magD3 * magQ
    global simD3
    simD3 =   resDot/Prod
    simD3 = round(simD3,4)
    print("Sim(Q,D3): ",simD3)
def D3calc():
    for i in range(Xt):
        rep = 0
        if term[i] not in doc3:
            rep1 = 0 
            D3R.append(rep1)
        elif term[i] in doc3:
            rep = doc3.count(term[i])
            D3R.append(rep)
def D4Mag():
    mag = 0
    D4l = len(DW4)
    for t in range(D4l):
        a = DW4[t] ** 2
        mag = mag + a
    magD4 = mag ** 0.5
    magD4 = round(magD4,3)
    print("|D4|: ",magD4)
    resDot = 0
    for g in range(Xt):
        Dot = QW1[g] * DW4[g] 
        resDot = resDot + Dot
    resDot = round(resDot,4)
    print("Q*d4: ",resDot)
    Prod = magD4 * magQ
    global simD4
    simD4 =   resDot/Prod
    simD4 = round(simD4,4)
    print("Sim(Q,D4): ",simD4)
def D4calc():
    for i in range(Xt):
        if term[i] not in doc4:
            rep1 = 0 
            D4R.append(rep1)
        elif term[i] in doc4:
            rep = doc4.count(term[i])
            D4R.append(rep)
while True:
    e = 0
    Entry = input("Enter \"S\" to start or \"E\" to exit:  ")
    if Entry == "S" or Entry == "s":
        while True:
            Number_of_doc = int(input("Enter the number of doc: "))
            if Number_of_doc > 4:
                print("only 4 documents allowed!!")
                continue 
            Query = list(map(str,input("Enter Query: ").lower().split()))
            x = len(Query)
            if Number_of_doc == 1:
                doc1 = list(map(str,input("Enter doc 1: ").lower().split()))
                x1 = len(doc1)
                for i in range(x1):
                    if doc1[i] not in Stop_Word:
                        ALLD.append(doc1[i])
            elif Number_of_doc == 2:
                doc1 = list(map(str,input("Enter doc 1: ").lower().split()))
                doc2 = list(map(str,input("Enter doc 2: ").lower().split()))
                x1 = len(doc1)
                x2 = len(doc2)
                for i in range(x1):
                    if doc1[i] not in Stop_Word:
                        ALLD.append(doc1[i])
                for i in range(x2):
                    if doc2[i] not in Stop_Word:
                        ALLD.append(doc2[i])
            elif Number_of_doc == 3:
                doc1 = list(map(str,input("Enter doc 1: ").lower().split()))
                doc2 = list(map(str,input("Enter doc 2: ").lower().split()))
                doc3 = list(map(str,input("Enter doc 3: ").lower().split()))
                x1 = len(doc1)
                x2 = len(doc2)
                x3 = len(doc3)
                for i in range(x1):
                    if doc1[i] not in Stop_Word:
                        ALLD.append(doc1[i])
                for i in range(x2):
                    if doc2[i] not in Stop_Word:
                        ALLD.append(doc2[i])
                for i in range(x3):
                    if doc3[i] not in Stop_Word:
                        ALLD.append(doc3[i])
            elif Number_of_doc == 4:
                doc1 = list(map(str,input("Enter doc 1: ").lower().split()))
                doc2 = list(map(str,input("Enter doc 2: ").lower().split()))
                doc3 = list(map(str,input("Enter doc 3: ").lower().split()))
                doc4 = list(map(str,input("Enter doc 4: ").lower().split()))
                x1 = len(doc1)
                x2 = len(doc2)
                x3 = len(doc3)
                x4 = len(doc4)
                for i in range(x1):
                    if doc1[i] not in Stop_Word:
                        ALLD.append(doc1[i])
                for i in range(x2):
                    if doc2[i] not in Stop_Word:
                        ALLD.append(doc2[i])
                for i in range(x3):
                    if doc3[i] not in Stop_Word:
                        ALLD.append(doc3[i])
                for i in range(x4):
                    if doc4[i] not in Stop_Word:
                        ALLD.append(doc4[i])
            for i in ALLD:
                if i not in term:
                    term.append(i)
            term = sorted(term)
            Xt = len(term)
            Xq = len(Query)
            y = Number_of_doc + 1
            for i in range(Xt):
                df = 0 
                IDf = 0
                if Number_of_doc == 1:
                    Qcalc()
                    D1calc()
                    if e == 0:
                        print("\n")
                        print("Term ", term)
                        print("Q: ", Q1R)
                        print("D1: ", D1R)
                        e = e + 1
                    Df.append(Q1R[i])
                    Df.append(D1R[i])
                elif Number_of_doc == 2:
                    Qcalc()
                    D1calc()
                    D2calc()
                    if e == 0:
                        print("\n")
                        print("Term ", term)
                        print("Q: ", Q1R)
                        print("D1: ", D1R)
                        print("D2: ", D2R)
                        e = e + 1
                    Df.append(Q1R[i])
                    Df.append(D1R[i])                       
                    Df.append(D2R[i])
                elif Number_of_doc == 3:
                    Qcalc()
                    D1calc()
                    D2calc()
                    D3calc()
                    if e == 0:
                        print("\n")
                        print("Term ", term)
                        print("Q: ", Q1R)
                        print("D1: ", D1R)
                        print("D2: ", D2R)
                        print("D3: ", D3R)
                        e = e + 1    
                    R = [Q1R,D1R,D2R,D3R]
                    for j in R:          
                        Df.append(j[i])
                elif Number_of_doc == 4:
                    Qcalc()
                    D1calc()
                    D2calc()
                    D3calc()
                    D4calc()
                    if e == 0:
                        print("\n")
                        print("Term ", term)
                        print("Q: ", Q1R)
                        print("D1: ", D1R)
                        print("D2: ", D2R)
                        print("D3: ", D3R)
                        print("D4: ", D4R)
                        e = e + 1
                    R = [Q1R,D1R,D2R,D3R,D4R]
                    for j in R:
                        Df.append(j[i])
                print("\n")    
                for j in range(1,y):
                    if Df[j] >= 1:
                        df = df + 1
                        IDf= math.log(Number_of_doc/df,10)
                        IDf = round(IDf,3)  
                IDfr.append(IDf)
                Dfr.append(df)
                for u in range(y):
                    l = IDfr[z] * Df[u]
                    l = round(l,3)
                    NDr.append(l)
                if Number_of_doc == 1:
                    QW1.append(NDr[0])
                    DW1.append(NDr[1])
                elif Number_of_doc == 2:
                    QW1.append(NDr[0])
                    DW1.append(NDr[1])
                    DW2.append(NDr[2])
                elif Number_of_doc == 3:
                    QW1.append(NDr[0])
                    DW1.append(NDr[1])
                    DW2.append(NDr[2])
                    DW3.append(NDr[3])
                elif Number_of_doc == 4:
                    QW1.append(NDr[0])
                    DW1.append(NDr[1])
                    DW2.append(NDr[2])
                    DW3.append(NDr[3])
                    DW4.append(NDr[4])
                print("Weight value of term ",Inc ,"from Q to Dn: ",NDr)
                Inc = Inc + 1
                z = z + 1
                silent = [NDr,Df,Q1R,D1R,D2R,D3R,D4R,rank]
                for l in silent:
                    l.clear()
            print("\n\nValue of DF and IDF\n\n")
            print("Df value from top to bottom: ",Dfr)
            print("IDF value from top to bottom: ",IDfr)
            print("\n")
            Inc1 = Xt + 1
            if Inc == Inc1:
                if Number_of_doc == 1:
                    QMag()
                    D1Mag()
                    print("Rank 1: D1", simD1)                
                elif Number_of_doc == 2:
                    QMag()
                    D1Mag()
                    D2Mag()
                    rank.append(simD1)
                    rank.append(simD2)
                    rank.sort(reverse=True)
                    rankL = len(rank)
                    for i in range(rankL):
                        if rank[i] == simD1:
                            if i == 0:
                                print("Rank 1: D1", simD1)
                            elif i == 1:
                                print("Rank 2: D1", simD1)
                        elif rank[i] == simD2:
                            if i == 0:
                                print("Rank 1: D2", simD2)
                            elif i == 1:
                                print("Rank 2: D2", simD2)
                elif Number_of_doc == 3:
                    QMag()
                    D1Mag()
                    D2Mag()
                    D3Mag()
                    sim = [simD1,simD2,simD3]
                    for j in sim:
                        rank.append(j)
                    rank.sort(reverse=True)
                    rankL = len(rank)
                    for a in range(rankL):
                        if rank[a] == simD1:
                            if a == 0:
                                print("Rank 1: D1", simD1)
                            elif a == 1:
                                print("Rank 2: D1", simD1)
                            elif a == 2:
                                print("Rank 3: D1", simD1)
                        elif rank[a] == simD2:
                            if a == 0:
                                print("Rank 1: D2", simD2)
                            elif a == 1:
                                print("Rank 2: D2", simD2)
                            elif a == 2:
                                print("Rank 3: D2", simD2)
                        elif rank[a] == simD3:
                            if a == 0:
                                print("Rank 1: D3", simD3)
                            elif a == 1:
                                print("Rank 2: D3", simD3)
                            elif a == 2:
                                print("Rank 3: D3", simD3)  
                elif Number_of_doc == 4:
                    QMag()
                    D1Mag()
                    D2Mag()
                    D3Mag()
                    D4Mag()
                    sim = [simD1,simD2,simD3,simD4]
                    for j in sim:
                        rank.append(j)
                    rank.sort(reverse=True)
                    rankL = len(rank)
                    for i in range(rankL):
                        if rank[i] == simD1:
                            if i == 0:
                                print("Rank 1: D1", simD1)
                            elif i == 1:
                                print("Rank 2: D1", simD1)
                            elif i == 2:
                                print("Rank 3: D1", simD1)
                            elif i == 3:
                                print("Rank 4: D1", simD1)
                        elif rank[i] == simD2:
                            if i == 0:
                                print("Rank 1: D2", simD2)
                            elif i == 1:
                                print("Rank 2: D2", simD2)
                            elif i == 2:
                                print("Rank 3: D2", simD2)
                            elif i == 3:
                                print("Rank 4: D2", simD2)
                        elif rank[i] == simD3:
                            if i == 0:
                                print("Rank 1: D3", simD3)
                            elif i == 1:
                                print("Rank 2: D3", simD3)
                            elif i == 2:
                                print("Rank 3: D3", simD3)
                            elif i == 3:
                                print("Rank 4: D3", simD3)
                        elif rank[i] == simD4:
                            if i == 0:
                                print("Rank 1: D1", simD4)
                            elif i == 1:
                                print("Rank 2: D1", simD4)
                            elif i == 2:
                                print("Rank 3: D1", simD4)
                            elif i == 3:
                                print("Rank 4: D1", simD4)
                break
    elif Entry == "E" or Entry == "e":
        print("Powered By Onyx Technology")
        break