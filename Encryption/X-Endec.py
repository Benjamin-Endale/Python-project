alpha,sup,cap,encrypt,decrypt = [],[],[],[],[]
alpha_ = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ","1","2","3","4","5","6","7","8","9","0","~","&","#","*",")","^","@","'","|","%",":","=",".","/","-",";","_","`","?",'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alphaX = ["x","y","z","X","Y","Z",".","/","-"]
alphaXD = ["a","b","c","A","B","C","_","`","?"]
betaX = ["d","e","f","D","E","F","_","`","?",]
betaXD = ["a","b","c","A","B","C",".","/","-",]
beta_ =  ["d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c"," ","~","&","#","*",")","^","@","'","|","%","1","2","3","4","5","6","7","8","9","0",";","=","_","`","?",":",".","/","-",'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','A', 'B', 'C']
AlphaD = ['D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','A', 'B', 'C']
Alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
num = ["1","2","3","4","5","6","7","8","9","0","=","~","&","#","*",")","^","@","'","|","%"]
numD = ["~","&","#","*",")","^","@","'","|","%","=","1","2","3","4","5","6","7","8","9","0"]
symb = [":",".","/","-"," ",";","_","`","?"]
symbD = [";","_","`","?"," ",":",".","/","-"]
capD = ['D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','A', 'B', 'C']
print("-------------- CONTROL ---------------\n \"Exit\" or \"t\" or \"exit\" - allows you to terminate the program when choosing operation.\n To do basic operation first use \"e\" + space for encryption and use \"d\" + space for decryption.\n example \"e [anything to encrypt] - dont forget to space before writting any value\"\n\n")
def clean():
    sup.clear()
    alpha.clear()
clone = Alpha.copy()
for i in clone:
    for j in i:
        d = j.upper()
        cap.append(d)
while True:
    ENCL = input("Enter the name: ")
    if ENCL == "Exit" or ENCL == "exit" or ENCL == "t" or ENCL == " t" or ENCL == " exit" or ENCL == " Exit" or ENCL == "t " or ENCL == "exit " or ENCL == "Exit " or ENCL == " t " or ENCL == " exit " or ENCL == " Exit ":
        print("Powered by Onyx Technology")
        break
    elif ENCL == "":
        print("No input!!")
    else:
        alpha.append(ENCL)
        for i in alpha:
            for j in i:
                l = len(j)
                sup.append(j)
        if sup[0] == "E" or sup[0] == "e":
            if len(sup) == 1:
                print("Nothing to encrypt!")
                clean()
                continue
            if sup[1] != " ":
                print("you didnt put a space after e!!")
                clean()
                continue
            if len(sup) == 2:
                print("you didnt right anything to encrypt")
                clean()
                continue
            for b in range(2, len(sup)):
                for n in range(len(alpha_)):
                    if sup[b] == alpha_[n]:
                        if alpha_[n] in num:
                            encrypt.append(beta_[n])
                        elif alpha_[n] in cap:
                            encrypt.append(beta_[n])
                        elif alpha_[n] in symbD:
                            encrypt.append(beta_[n])
                        else:
                            if alpha_[n] in alphaX:
                                encrypt.append(beta_[n])
                            elif alpha_[n] in alphaXD:
                                encrypt.append(beta_[n])
                            else:
                                f = n + 3
                                encrypt.append(alpha_[f])
            p = "".join(encrypt)
            print("encrypted value: ",p)
            encrypt.clear()
            clean()
        elif sup[0] == "d" or sup[0] == "D": 
            if len(sup) == 1:
                print("Nothing to decrypt!")
                clean()
                continue
            if sup[1] != " ":
                print("you didnt put a space after d!!")
                clean()
                continue
            if len(sup) == 2:
                print("you didnt right anything to decrypt")
                clean()
                continue
            for b in range(2,len(sup)):
                for n in range(len(beta_)):
                    if sup[b] == beta_[n]:
                        if beta_[n] in numD:
                            decrypt.append(alpha_[n])
                        elif beta_[n] in symb:
                            decrypt.append(alpha_[n])
                        elif beta_[n] in capD:
                            decrypt.append(alpha_[n])
                        else:
                            if beta_[n] in betaX:
                                decrypt.append(alpha_[n])
                            elif beta_[n] in betaXD:
                                decrypt.append(alpha_[n])
                            else:
                                f = n - 3
                                decrypt.append(beta_[f])
            p = "".join(decrypt) 
            print("Decrypted value: ",p)
            decrypt.clear()
            clean()
        else:
            print("you didnt use \"e\" or \"d\"!! try again!!")
            encrypt.clear()
            decrypt.clear()
            clean()
            continue