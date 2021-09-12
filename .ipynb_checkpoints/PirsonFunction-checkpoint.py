import numpy as np

def wet_phase(Sw, Swc):
    krw = np.sqrt(abs(Sw-Swc)/(1-Swc)) * (Sw ** 3)
    return krw

def imbibition_nw(Snw, Sw, Swc):
    krnw = (1-(Sw-Swc)/(1-Swc-Snw)) ** 2
    return krnw

def drainage_nw(Sw, Swc):
    Sws = (Sw-Swc)/(1-Swc)
    krnw = (1-Sws) * ((1 - np.power(Sws, 0.25) * np.sqrt(Sw)) ** 0.5)
    return krnw