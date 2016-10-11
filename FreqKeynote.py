#Frequency of the keynote of claves
import numpy as np 

def freqk(x,t,rate):
    ft=np.fft.fftshift(np.fft.fft(x,rate)) 
    faxis=np.arange(-ft.shape[0]/2,ft.shape[0]/2)*1./rate 
    t=faxis[np.where(np.abs(ft)==np.amax(np.abs(ft)))[0]] 
    n=int(round(np.abs(22.05/t)))
    return n

