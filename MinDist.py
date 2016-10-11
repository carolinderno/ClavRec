#Minimal distance between two rhythms
#function f=|x-a*y-b|, whereas x and y are the correspondant vectors of two rhythms
#look for minimum of its partial derivations

import numpy as np
import itertools

def mindist(t1,m1,t2,m2): 
    if len(t1)==len(t2):
        ysum=t2[0:len(t2)].sum()
        ysumsq=np.power(t2[0:len(t2)],2).sum()
        xsum=t1[0:len(t1)].sum()
        xysum=(t1*t2).sum()
        A=np.array([[ysum,len(t1)],[ysumsq,ysum]]) 
        c=np.array([xsum,xysum])
        a,b=np.linalg.solve(A,c)
        dist2=np.sqrt(np.power(t1-a*t2-b,2).sum())
        t1new=t1; m1new=m1; t2new=t2; m2new=m2
    if len(t1)>len(t2):
        xsum=t1[0:len(t1)].sum()
        diff=len(t1)-len(t2)
        comb=list(itertools.combinations_with_replacement(range(len(t2)),diff))
        dist1=np.zeros(len(comb)); a1=np.zeros(len(comb)); b1=np.zeros(len(comb))
        k=0 
        for i in itertools.combinations_with_replacement(range(len(t2)),diff):
            k=1+k
            for j in range(diff):
                t2new=np.insert(t2,i[j],t2[i[j]])
            ysumsq=np.power(t2new[0:len(t2new)],2).sum()
            ysum=t2new[0:len(t2new)].sum()
            xysum=(t1*t2new).sum()
            A=np.array([[ysum,len(t1)],[ysumsq,ysum]])
            c=np.array([xsum,xysum])
            a1[k-1],b1[k-1]=np.linalg.solve(A,c)
            dist1[k-1]=np.sqrt(np.power(t1-a1[k-1]*t2new-b1[k-1],2).sum())
        dist2=np.amin(dist1)
        pos=np.where(dist1==dist2)[0]
        t1new=t1; m1new=m1; 
        a=a1[pos]; b=b1[pos]
        for j in range(diff):
            t2new=np.insert(t2,comb[pos][j],t2[comb[pos][j]]); 
            m2new=np.insert(m2,comb[pos][j],m2[comb[pos][j]])
        print 'reproduction has less notes than the given rhythm'
    if len(t1)<len(t2):
        ysum=t1[0:len(t2)].sum()
        ysumsq=np.power(t2[0:len(t2)],2).sum()
        diff=len(t2)-len(t1)
        comb=list(itertools.combinations_with_replacement(range(len(t1)),diff))
        dist1=np.zeros(len(comb)); a1=np.zeros(len(comb)); b1=np.zeros(len(comb))
        k=0 
        for i in itertools.combinations_with_replacement(range(len(t1)),diff):
            k=1+k
            for j in range(diff):
                t1new=np.insert(t1,i[j],t1[i[j]])
            xsum=t1new[0:len(t1new)].sum()
            xysum=(t1new*t2).sum()
            A=np.array([[ysum,len(t1)],[ysumsq,ysum]])
            c=np.array([xsum,xysum])
            a1[k-1],b1[k-1]=np.linalg.solve(A,c)
            dist1[k-1]=np.sqrt(np.power(t1new-a1[k-1]*t2-b1[k-1],2).sum())
        dist2=np.amin(dist1)
        pos=np.where(dist1==dist2)[0]
        t2new=t2; m2new=m2; 
        a=a1[pos]; b=b1[pos]
        for j in range(diff):
            t1new=np.insert(t1,comb[pos][j],t1[comb[pos][j]]); 
            m1new=np.insert(m1,comb[pos][j],m1[comb[pos][j]])
        print 'reproduction has more notes than the given rhythm'
    return t1new,m1new,t2new,m2new,a,b,dist2 
