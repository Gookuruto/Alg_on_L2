import numpy as np
import rozklady
import freq_cls as fc
import rma_cls as rc
import lru_cls as lru
import datetime
import math
import matplotlib.pyplot as plt

def FIFO(k,n,rozklad):
    cache=[None]*k
    pages=[None]*n
    distrib=rozklad(n)
    print(distrib)
    cost=0
    for i in range(n):
        pages[i]=i+1
    for i in range(n):
        z=np.random.choice(pages,p=distrib)
        if (i<k and not z in cache) or (None in cache and not z in cache):
            if None in cache:
                for j in range(k):
                    if cache[j]==None and z not in cache:
                        cache[i%k]=z
                        cost+=1
        else:
            if z in cache:
                pass
            else:
                cache.pop(0)
                cache.append(z)
                cost+=1
                print(cache)
    return cost

def RAND(k,n,rozklad):
    cache=[None]*k
    pages=[None]*n
    distrib=rozklad(n)
    print(distrib)
    cost=0
    for i in range(n):
        pages[i]=i+1
    for i in range(n):
        z=np.random.choice(pages,p=distrib)
        if (i<k and not z in cache) or (None in cache and not z in cache):
            if None in cache:
                for j in range(k):
                    if cache[j]==None and z not in cache:
                        cache[i%k]=z
                        cost+=1
        else:
            if z in cache:
                cost=cost
            else:
                x=np.random.random_integers(0,k-1)
                print("x=  "+str(x))
                cache[x]=z
                cost+=1
                print(cache)
    return cost
def LFU(k,n,rozklad):
    cache=[None]*k
    pages=[None]*n
    distrib = rozklad(n)
    cost=0
    for i in range(n):
        pages[i]=fc.freq_obj(i+1,0)
    for i in range(n):
        #print(pages)
        z=np.random.choice(pages,p=distrib)
        if (i<k and not z in cache) or (None in cache and not z in cache):
            if None in cache:
                for j in range(k):
                    if cache[j]==None and z not in cache:
                        cache[j] = z
                        cache[j].freq+=1
                        cost += 1
        else:
            if z in cache:
                cost=cost
            else:
                cache.sort(key=lambda x: x.freq)
                cache[0]=z
                z.freq+=1
                cost+=1
                #print(cache)
    return cost

def FWF(k,n,rozklad):
    cache=[None]*k
    pages=[None]*n
    distrib=rozklad(n)
    #print(distrib)
    cost=0
    for i in range(n):
        pages[i]=i+1
    for i in range(n):
        z=np.random.choice(pages,p=distrib)
        if (i<k and not z in cache) or (None in cache and not z in cache):
            if None in cache:
                for j in range(k):
                    if cache[j]==None and z not in cache:
                        cache[j] = z
                        cost += 1
        else:
            cache=[None]*k
    return cost
def RMA(k,n,rozklad):
    cache = [None] * k
    pages = [None] * n
    distrib = rozklad(n)
    cost = 0
    for i in range(n):
        pages[i] = rc.rma_obj(i + 1, False)
    for i in range(n):
        # print(pages)
        z = np.random.choice(pages, p=distrib)
        if (i < k and z not in cache) or (None in cache and z not in cache):
            if None in cache:
                for j in range(k):
                    if cache[j]==None and z not in cache:
                        cache[j] = z
                        cache[j].mark = True
                        cost += 1

            #else:
                #cache[i%k] = z
                #cache[i%k].mark = True
                #cost += 1
        else:
            if z in cache:
                z.mark=True
                cost = cost
            else:
                x=np.random.random_integers(0,k-1)
                ksz = 0
                for j in cache:
                    if j.mark:
                        ksz += 1
                if ksz >= k:
                    for l in cache:
                        l.mark = False
                while cache[x].mark :

                    x=np.random.random_integers(0,k-1)
                cache[x]=z
                cost += 1
                #print(cache)
    return cost

#TODO Least Frequency Used algorithm and test with plots
def LRU(k,n,rozklad):
    cache=[None]*k
    pages=[None]*n
    distrib = rozklad(n)
    cost=0
    for i in range(n):
        pages[i]=lru.lru_obj(i+1,datetime.datetime.now())
    for i in range(n):
        #print(pages)
        z=np.random.choice(pages,p=distrib)
        if (i<k and not z in cache) or (None in cache and not z in cache):
            if None in cache:
                for j in range(k):
                    if cache[j]==None and z not in cache:
                        cache[j] = z
                        cache[j].datetim=datetime.datetime.now()
                        cost += 1
        else:
            if z in cache:
                z.datetim=datetime.datetime.now()
            else:
                cache.sort(key=lambda x: x.datetim)
                cache[0]=z
                z.datetim=datetime.datetime.now()
                cost+=1
                #print(cache)
    return cost



print(LRU(10,100,rozklady.geometryczny))


n=[20,30,40,50,60,70,80,90,100]
tempx=[None]*100
x=[None]*54
xk=[None]*54
ind=0
for i in n:
    k=[math.ceil((i/5)),math.ceil(i/6),math.ceil(i/7),math.ceil(i/8),math.ceil(i/9),math.ceil(i/10)]
    for j in k:
        for l in range(100):
            tempx[l]=RMA(j,i,rozklady.dwuharmoniczny)
        x[ind]=sum(tempx)/len(tempx)
        xk[ind]=k[ind%6]
        ind+=1
'''
print(x[0:6])
print(xk[0:6])
'''
rangmin=0
rangup=6
colors=['b','g','r','c','m','y','k','gold','salmon']
for i in range(9):
    plt.plot(xk[rangmin:rangup],x[rangmin:rangup],color=colors[i],label="n = "+str(n[i]))
    plt.xlabel("k")
    plt.ylabel("cost")
    rangmin+=6
    rangup+=6
plt.legend(loc="lower right",shadow=True)
plt.show()