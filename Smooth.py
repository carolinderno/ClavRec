#Smoothing the data x 
#n is the main frequence of the keynote of claves
import numpy as np

def gleitmit(x,rate,n):
    if (n % 2) ==0:    
        y=np.zeros(len(x)-n)
        for i in range(n/2,len(x)-n/2):
            a=1/2.*x[i-n/2]
            b=1/2.*x[i+n/2]
            sum=a+b+x[-n/2+1+i:n/2-1+i].sum()
            y[i-n/2]=sum/n
    else: 
        y=np.zeros(len(x)-(n-1)) 
        for i in range((n-1)/2,len(x)-(n-1)/2):
            sum=x[-(n-1)/2+i:(n-1)/2+i].sum() 
            y[i-(n-1)/2.]=sum/n
    ty = np.arange(y.shape[0])*1000./rate
    return y,ty

