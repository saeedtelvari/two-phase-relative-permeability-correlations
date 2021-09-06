import numpy as np

def oil_water(Sw = 0, So = 0, Swc = 0, rock_type = 'UW'):
    if (Sw > 1) or (Sw <= 0):
        print('Invalid input : Sw')
        return
    if (So > 1) or (So <= 0):
        print('Invalid input : So')
        return
    if (Swc > 1) or (Swc <= 0):
        print('Invalid input : Swc')
        return
    eff_sw = (Sw-Swc)/(1-Swc)
    eff_so = So/(1-Swc)
    krw = 0
    kro = 0
    if rock_type.upper() == 'UW':
        krw = np.power(eff_sw, 3)
        kro = 1 - eff_sw
    if rock_type.upper() == 'UP':
        krw = np.power(eff_so, 3.5)
        kro = np.power(1-eff_sw, 2) * (1-np.power(eff_sw, 1.5))
    if rock_type.upper() == 'CO':
        krw = np.power(eff_so, 4)
        kro = np.power(1-eff_so, 2) * (1-np.power(eff_sw, 2))
        
    return krw, kro

def oil_gas(So = 0, Swc = 0, rock_type = 'UW'):
    if (So > 1) or (So <= 0):
        print('Invalid input : So')
        return
    if (Swc > 1) or (Swc <= 0):
        print('Invalid input : Swc')
        return
    eff_so = So/(1-Swc)
    krg = 0
    kro = 0
    if rock_type.upper() == 'UW':
        krg = np.power(1-eff_so, 3)
        kro = np.power(eff_so, 3)
    if rock_type.upper() == 'UP':
        krg = np.power(1-eff_so, 2) * (1-np.power(eff_so, 1.5))
        kro = np.power(eff_so, 3.5)
    if rock_type.upper() == 'CO':
        krg = np.power(1-eff_so, 2) * (1-np.power(eff_so, 2))
        kro = np.power(eff_so, 4)
        
    return krg, kro