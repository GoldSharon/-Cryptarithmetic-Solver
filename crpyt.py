# send+
# more
# _____
# money
# _____



def solution():
    
    # letters s,e,n,d,m,o,r,y
    for s in range(9,-1,-1):
        for e in range(9,-1,-1):
            for n in range(9,-1,-1):
                for d in range(9,-1,-1):
                    for m in range(9,0,-1):
                        for o in range(9,-1,-1):
                            for r in range(9,-1,-1):
                                for y in range(9,-1,-1):
                                    if len(set([s,e,n,d,m,o,r,y]))==8:
                                        send=s*1000+e*100+n*10+d
                                        more=m*1000+o*100+r*10+e
                                        money=m*10000+o*1000+n*100+e*10+y
                                        if money==send+more:
                                            print("send = "+str(send))
                                            print("more = "+str(more))
                                            print("money = "+str(money))
                                            

solution()                                           