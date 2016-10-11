#Read a wav-file
from scipy.io import wavfile

def read(filename):
    rate,x=wavfile.read(filename) 
    x = x.astype(np.float) 
    t = np.arange(x.shape[0])*1./rate*100
    return x,t,rate
