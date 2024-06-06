t=["0.movies","1.web series","2.anime"] 
t2=[["0.bollywood","1.hollywood","2.tollywood"],["0.bollywood","1.hollywood"],["0.japanese anime"]]
t3=[["0.tanhaji","1.pawankhind","2.farjad"],["0.avengers","1.logan","2.ghost rider"],["0.KGF","1.RRR","2.Pushpa"],["0.family man","1.tandav","2.special ops"],["0.game of thrones","1.money hiest","2.wednesday"],["0.One piece","1.Dragon ball super","2.Demon slayer"]]
t4=["gadh ala pn sivha gela !!","gadawar pohochlyawar tofanche tin aavaj dya tovar ganim pudhe sarku denar nahi raje","fakta 40 mavle dya raje gadh jinkun yeto!!!","or hulk: phod dena !!","Go... Don't be what they made you","I'm the king of hell"]
t5=["violence.. violence.. violence","Natto natto","jhukega nahi salla"]
t6=["Mere liye mera desh, Tere liye Jehad, Sab zaruri hai","सही और गलत के बीच में जो चीज इतनी खड़ी हो जाती है ना","The Less Competent Should Not Judge The More Competent"]
t7=["Never forget what you are, the rest of the world will not. Wear it like armor and it can never be used to hurt you","The plan is designed to survive any setbacks, including my death.","Wednesday's child is full of woe.",]
t8=["Inherited Will, The Destiny Of Age, The Dreams Of Its People","Yo, I'm Goku” — Goku","No matter how many people you may lose, you have no choice but to go on living -- no matter how devastating the blows, maybe."]
print(t)
a=int(input("Enter your choise:"))
if a>0<1:
    if a<2>1:
        print(t2[1])
        d=int(input("Enter your choise:"))
        if d>0<1:
                print(t3[4])
                f=int(input("Enter your choise:"))
                if f>0<1:
                    if f<2>1:
                       print(t7[1])
                    else:
                        print(t7[2])
                else:
                    print(t7[0])
        else:
            print(t3[3])
            e=int(input("enter your choise:"))
            if e>0<1:
                if e<2>1:
                    print(t6[1])
                else:
                    print(t6[2])
            else:
                print(t6[0])
    
    
    
    else:
                                                    print(t3[-1])
                                                    i=int(input("Enter your choise:"))
                                                    if i>0<1:
                                                        if i<2>1:
                                                            print(t8[1])
                                                        else:
                                                            print(t8[2])
                                                    else:
                                                        print(t8[0])

       

else:
    print(t2[0])
    b=int(input("Enter your choise:"))
    if b>0<1:
         if b<2>1:
            print(t3[1])
            g=int(input("Enter your choise:"))
            if g>0<1:
                if g<2>1:
                    print(t4[4])  
                else:
                    print(t4[5])
            else:
                print(t4[3])
                       
         
         
         
         else:
            print(t3[2])
            h=int(input("Enter your choise:"))
            if h>0<1:
                if h<2>1:
                    print(t5[1])
                else:
                    print(t5[2])
            else:
                print(t5[0])
    
    else:
        print(t3[0])

        c=int(input("Enter your choise:"))
        if c>0<1:
            if c<2>1:
                print(t4[1])
            else:
                print(t4[2])
        else:
            print(t4[0])