#Dimension reduction 
#Returning a vector with the points in time of the local maxima of all amplitude envelopes (= onsets)
#bounds s1 (y-axis) and s2 (x-axis) were adapted to the specific claves' recordings
#in order to get all maxima of all rhythms

import numpy as np

def maxi(y,ty,s1,s2): 
    w=np.where(y>s1)[0]
    dt=np.diff(w)
    pos=np.where(dt>s2)[0]+1 
    neu=np.split(w,pos)
    m=np.zeros(len(neu))
    t=np.zeros(len(neu))
    for i in range(len(neu)):
        yneu=np.zeros(len(neu[i]))
        for j in range(len(neu[i])):
            yneu[j]=y[neu[i][j]]
        m[i]=np.max(yneu)
        t[i]=ty[np.where(y==m[i])][0]
    return m,t
