import numpy as np

class oil_gas:
    def __init__(self):
        pass
    def kr_oil(self, Sg, Swc):
        kro = (1-Sg/(1-Swc)) ** 4
        return kro
    def kr_gas(self, Sg, Swc):
        krg = Sg/(1-Swc) * (2-Sg/(1-Swc))
        return krg
class oil_water:
    def __init__(self):
        pass
    def kr_oil(self, Sw, Swc, n = 4):
        kro = ((1-Sw)/(1-Swc)) ** n
        return kro
    def kr_water(self, Sw ,Swc , m = 4):
        krw = ((Sw-Swc)/(1-Swc)) ** m
        return krw