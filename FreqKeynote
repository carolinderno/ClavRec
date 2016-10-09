#Frequency of the keynote of claves
import numpy as np 

x,t,rate=read(’R1.wav’)

f=np.fft.fft(x,rate) 

ft=np.fft.fftshift(np.fft.fft(x,rate)) #centering fft around zero

faxis=np. arange(−ft . shape [0]/2 , ft . shape [0]/2)∗1./ rate #Vector with points in time (axis of abscissae)

t=faxis[np.where(np.abs(ft)==np.amax(np.abs(ft)))[0]] 
#Time values of the maximum of the absolute value (negative values possible) of the Fourier transform

n=int(round(np.abs(22.05/t)))
