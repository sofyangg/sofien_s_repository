row=["a","b","c","d","e","f","g","h"]
board=[]
for i in row:
  column=[]
  for j in range(8):
   column.append(i+str(j))
  board.append(column)

for i in range (3):
 pnp=input("place a piece in a specific place separated by a ,") 
 k=0
 while pnp[k]!="," and k<len(pnp):
   k+=1
 piece= pnp[:k]
 positionn= pnp[k+1:]
 
 
   
 if positionn[0]=="a":

    p=0
 elif positionn[0]=="b":
    p=1
 elif positionn[0]=="c":
    p=2
 elif positionn[0]=="d":
    p=3
 elif positionn[0]=="e" :
    p=4
 elif positionn[0]=="f":
    p=5
 elif positionn[0]=="g":
    p=6
 elif positionn[0]=="h":
    p=7
   
 p2=int( positionn[1])-1
 board[p][p2]=piece






k=3
while k>0 :
   position=input( "give me a position and i'll tell you it's place")
   while  len(position)!= 2 or position[0] not in ["a","b","c","d","e","f","g","h"] and position[1] not in["1","2","3","4","5","6","7","8"]:
     posittion=input("give me a real position")
   if position[0]=="a":

    p=0
   elif position[0]=="b":
    p=1
   elif position[0]=="c":
    p=2
   elif position[0]=="d":
    p=3
   elif position[0]=="e" :
    p=4
   elif position[0]=="f":
    p=5
   elif position[0]=="g":
    p=6
   elif position[0]=="h":
    p=7
   
   p2=int( position[1])-1
   print(board[p][p2])
   k-=1