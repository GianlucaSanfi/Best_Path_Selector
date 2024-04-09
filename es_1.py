##################### DEF FUNZIONI ######################
def checkSilver(point, direz):
     #se (dire_x > 0) => vado a sinistra  
     #se (dire_y > 0) => vado sopra
    """  if point[0] > 0:
        #ho spazio per andare a sinistra

     if point[0] < W-2:
        #ho spazio per andare a destra
        
     if point [1] > 0:
        #ho spazio per andare sopra


     if point [1] < H-2:
        #ho spazio per andare sotto """


    point1 = (point[0]+1, point[1]+1)
    if point1 in silvers_onlyCoord:
        return "UL"

    point1 = (point[0]+1, point[1]+1)
    if point1 in silvers_onlyCoord:
        return "UR"
    point1 = (point[0]+1, point[1]+1)
    if point1 in silvers_onlyCoord:
        return "UR"
    point1 = (point[0]+1, point[1]+1)
    if point1 in silvers_onlyCoord:
        return "UR"

    return 0

############################
def chooseTile(conn):
    lung = 20
    costo = 100000
    k = 'h'
    for key in direzioni:
        if (conn in direzioni[key]) and (direzioni[key][0] > 0) and ((direzioni[key][1] <= costo) or (len(direzioni[key]) < lung)):
            k = key
            lung = len(direzioni[key])
            costo = direzioni[key][1]

    return k

def chooseMTile(conns):
    lung = 20
    costo = 100000
    k = 'h'
    for key in direzioni:
        for di in conns:
            if (di in direzioni[key]) and (direzioni[key][0] > 0) and ((direzioni[key][1] <= costo) or (len(direzioni[key]) < lung)):
                k = key
                lung = len(direzioni[key])
                costo = direzioni[key][1]
    return k

###########################
def findComplementare(pos, newNeed):
    k = 'h'

    return k

#####################################################
##################### START #########################

nome_file = "00-trailer.txt"


direzioni = {} #tot, cost, dir's
direzioni['3'] = [0,0,"HOR"]
direzioni['5'] = [0,0,"UR", "LD"]
direzioni['6'] = [0,0,"UL", "RD"]
direzioni['7'] = [0,0,"HOR", "LD", "RD", "UL", "UR"]
direzioni['9'] = [0,0,"LU", "DR"]
direzioni['A'] = [0,0,"RU", "DL"]
direzioni['B'] = [0,0,"HOE", "LU", "RU", "DR", "DL"]
direzioni['C'] = [0,0,"VER"]
direzioni['D'] = [0,0,"VER","UR", "DR", "LU", "LD"]
direzioni['E'] = [0,0,"VER","UL", "DL", "RD", "RU"]
direzioni['F'] = [0,0,"VER", "HOR", "UL", "UR", "LU", "RU", "DL", "DR", "LD", "RD"]

#effettivi
total_score = 0
total_cost = 0
########
totale_possibili_score = 0
total_tiles = 0
goldens = []
silvers = []
silvers_onlyCoord = []

#apro file lettura
file_in = open(nome_file, "r", encoding="utf-8-sig")
line = file_in.readline()
l = line.split()

W = int(l[0])
H = int(l[1])
N = int(l[2])
M = int(l[3])
L = int(l[4])

matriceTiles = [[0 for i in range(W)] for j in range(H)]

for i in range(N):
    line = file_in.readline()
    l = line.split()
    goldens.append((int(l[0]), int(l[1])))

for i in range(M):
    line = file_in.readline()
    l = line.split()
    silvers.append((int(l[0]), int(l[1]), int(l[2])))
    silvers_onlyCoord.append((int(l[0]), int(l[1])))
    totale_possibili_score += int(l[2])

for i in range(L):
    line = file_in.readline()
    l = line.split()

    #aggiorno num disponibili
    direzioni[l[0]][0] = int(l[2])
    total_tiles += int(l[2])
    
    #aggiorno costo
    direzioni[l[0]][1] = int(l[1])
print("tot tiles: ", total_tiles)
file_in.close()

for i in range(N):
   
    pos = (goldens[i][0], goldens[i][1])

    for j in range(i+1, N):
        jx = goldens[j][0]
        jy = goldens[j][1]

        print("indice j: ", j)
        dire = ((pos[0] - jx), (pos[1] - jy))  
            #se (dire_x > 0) => vado a sinistra  
            #se (dire_y > 0) => vado sopra
        #res = checkSilver(pos, dire) 
        res = 0
        
        if res == 0:
            #no silver vicini, seguo path

            if dire[0] > 0 and dire[1] == 0 :
                #sinistra
                d = "HOR"
                pos = (pos[0]-1, pos[1])
                k = chooseTile(d)
                print(k, " ", pos)
                if k == 'h':
                    continue
                if matriceTiles[pos[0]][pos[1]] == 0 :
                    matriceTiles[pos[0]][pos[1]] = (k, pos[0], pos[1])
                    direzioni[k][0] = direzioni.get(k)[0] -1 #aggiorno count
                else:
                    k = findComplementare(pos, d)
                    if k == 'h':
                        continue
                    #per ora non cambio mai...

            elif dire[0] < 0 and dire[1] == 0 :
                #destra
                d = "HOR"
                pos = (pos[0]+1, pos[1])
                k = chooseTile(d)
                print(k, " ", pos)
                if k == 'h':
                    continue
                if matriceTiles[pos[0]][pos[1]] == 0 :
                    matriceTiles[pos[0]][pos[1]] = (k, pos[0], pos[1])
                    direzioni[k][0] = direzioni.get(k)[0] -1 #aggiorno count
                else:
                    k = findComplementare(pos, d)
                    if k == 'h':
                        continue
                    #per ora non cambio mai...
            elif dire[0] == 0 and dire[1] > 0 :
                #sopra
                d = "VER"
                pos = (pos[0], pos[1]-1)
                k = chooseTile(d)
                print(k, " ", pos)
                if k == 'h':
                    continue
                if matriceTiles[pos[0]][pos[1]] == 0 :
                    matriceTiles[pos[0]][pos[1]] = (k, pos[0], pos[1])
                    direzioni[k][0] = direzioni.get(k)[0] -1 #aggiorno count
                else:
                    k = findComplementare(pos, d)
                    if k == 'h':
                        continue
                    #per ora non cambio mai...
            elif dire[0] == 0 and dire[1] < 0 :
                #sotto
                d = "VER"
                pos = (pos[0], pos[1]+1)
                k = chooseTile(d)
                print(k, " ", pos)
                if k == 'h':
                    continue
                if matriceTiles[pos[0]][pos[1]] == 0 :
                    matriceTiles[pos[0]][pos[1]] = (k, pos[0], pos[1])
                    direzioni[k][0] = direzioni.get(k)[0] -1 #aggiorno count
                else:
                    k = findComplementare(pos, d)
                    if k == 'h':
                        continue
                    #per ora non cambio mai...

            #TODO dir diagonali
            elif dire[0] > 0 and dire[1] > 0 :
                #sopra sinistra // sinistra sopra
                d = ["UL", "LU"]
                k = chooseMTile(d)
                pos = (pos[0]-1, pos[1]-1)
                print(k, " ", pos)

            elif dire[0] < 0 and dire[1] > 0 :
                #sopra destra // destra sopra
                d = ["UR", "RU"]
                k = chooseMTile(d)
                pos = (pos[0]+1, pos[1]-1)
                print(k, " ", pos)

    if total_tiles <= 0:
        break    

#apro file scrittura
file_out = open("soluzioni/output0.txt", "w", encoding="UTF-8")
#file_out.write(l[0]+l[1])
#for s in lista:
#    f_out.write(str(s) + "\n");
for elem in matriceTiles:
    if elem != 0:
        file_out.write(str(elem[0]) +" "+ str(elem[1]) +" "+ str(elem[2]) +"\n")
file_out.close()
