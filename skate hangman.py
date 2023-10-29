import random

class game():
    tries=1
    def __init__(self):
        k=int(input("how many years did you spend skating?: "))
        if k==0:
            self.word="wheels"
            self.NBlanks=3
            b=random.randint(1,3)
            if b==1:
                self.blank="w123ls"
                self.Blankies=["h","e","e"]
            elif b==2:
                self.blank="1hee23"
                self.Blankies=["w","l","s"]
            elif b==3:
                self.blank="1he2l3"
                self.Blankies=["w","e","s"]
        elif k==1:
            self.word="kickflip"
            self.NBlanks=3
            b=random.randint(1,3)
            if b==1:
                self.blank="ki1k2li3"
                self.Blankies=["c","f","p"]
            elif b==2:
                self.blank="k1c2fl3p"
                self.Blankies=["i","k","i"]
            elif b==3:
                self.blank="kick123p"
                self.Blankies=["f","l","i"]
        elif k==2:
            self.word="backside"
            self.NBlanks=3
            b=random.randint(1,3)
            if b==1:
                self.blank="b1c2si3e"
                self.Blankies=["a","k","d"]
            elif b==2:
                self.blank="123kside"
                self.Blankies=["b","a","c"]
            elif b==3:
                self.blank="ba123ide"
                self.Blankies=["c","k","s"]
        elif k==3:
            self.word="treflip"
            self.NBlanks=3
            b=random.randint(1,3)
            if b==1:
                self.blank="tre12i3"
                self.Blankies=["f","l","p"]
            elif b==2:
                self.blank="t12f3ip"
                self.Blankies=["r","e","l"]
            elif b==3:
                self.blank="1refl23"
                self.Blankies=["t","i","p"]
        elif k==4:
            self.word="grind"
            self.NBlanks=3
            b=random.randint(1,3)
            if b==1:
                self.blank="12i3d"
                self.Blankies=["g","r","n"]
            elif b==2:
                self.blank="g123d"
                self.Blankies=["r","i","n"]
            elif b==3:
                self.blank="g12n3"
                self.Blankies=["r","i","d"]
        elif k==5:
            self.word="pop"
            b=random.randint(1,3)
            if b==1:
                self.blank="1op"
                self.Blankies=["p"]
                self.NBlanks=1
            elif b==2:
                self.blank="p2p"
                self.Blankies=["o"]
                self.NBlanks=1
            elif b==3:
                self.blank="p23"
                self.Blankies=["o","p"]
                self.NBlanks=1
        elif k>5:
            self.word="batb"
            self.NBlanks=3
            b=random.randint(1,3)
            if b==1:
                self.blank="123b"
                self.Blankies=["b","a","t"]
                self.NBlanks=3
            elif b==2:
                self.blank="b12b"
                self.Blankies=["a","t"]
                self.NBlanks=2
            elif b==3:
                self.blank="bat3"
                self.Blankies=["b"]  
                self.NBlanks=1
    def Try(self):
            print(self.blank)
            print("this is your",self.tries,"'th try")
            k=str(input("give me a letter and it's place separated by a ,"))
        
            return k
    
    def Test2(self):
        k=None
        if self.NBlanks==0:
            k=True
            print("you won!")
        if self.tries==8:
            k=False
            print("you lost!")
        return k
        
    def Test(self,k):
        m=True
        if len(k)>3:
            print("dafuq")
            m=False
        if  m==True and k[0] not in self.Blankies:
            print("letter not in word")
            m=False
        if  m==True and k[2]not  in ["1","2","3"]:
            print("that letter is not missing")
            m=False
        if m==True and  self.word[self.blank.index(k[2])]!=k[0]:
            print("letter and position not matching")
            m=False
        if m==True:
            print("nice")
        return m
        
    def allGood(self,k):
        st=""
        for i in range(0,len(self.blank)):
            if self.blank[i]==k[2]:
                st+=k[0]
            else:
                st+=self.blank[i]
        self.blank=st
        self.NBlanks=self.NBlanks-1
    def NotGood(self):
        self.tries=self.tries+1

j="OK"
while j=="OK":
    game1=game()
    k=game1.Try()
    l=game1.Test(k)
    if l==True:
        game1.allGood(k)
    else:
        game1.NotGood()
        while l==False and game1.tries!=8:
            k=game1.Try()
            l=game1.Test(k)
            if l==True:
                game1.allGood(k)
            else:
                game1.NotGood()

    m=game1.Test2()
    while m==None:
        k=game1.Try()
        l=game1.Test(k)
        if l==True:
            game1.allGood(k)
        else:
            game1.NotGood()
            while l==False and game1.tries!=8:
                k=game1.Try()
                l=game1.Test(k)
                if l==True:
                    game1.allGood(k)
                else:
                    game1.NotGood()
        m=game1.Test2()
    if m==False:
        j=input("i'm sorry you lost press OK if you wanna try again or NO if you don't")
    if m==True:
        j=input("good job press OK if you wanna try again or NO if you don't ")
    if j=="OK":
        print("HERE WE GOOOOOOOOOOOOOO")
    else: 
        print("GOODBYEeeeeeeeeeee")

