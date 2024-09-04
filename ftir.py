import typing
import numpy as np
import pandas as pd
import scipy as sp
from scipy import signal
import torch 
import torch.nn as nn
import matplotlib.pyplot as pl
import pyspectra

# Process FTIR Data

def readOld():
    # Loading
    spec = pd.read_csv("C:/Users/guilh/OneDrive/Documents/Pesquisa/ML MIT/FTIR NN/polyethylene_ref.csv",
                   sep = ";" 
                   )
    spec = spec[['Wavenumbers [1/cm]', 'Absorbance']]

    # Cleansing
    spec['Wavenumbers [1/cm]'] = [float(x.replace(',','.')) for x in spec['Wavenumbers [1/cm]']]
    spec['Absorbance'] = [float(x.replace(',','.')) for x in spec['Absorbance']]

    # Range and Resolution
    #spec = signal.resample_poly(spec, 2, 4)
    spec = spec.iloc[rang[0]:rang[1], :]
    return spec

def readNicolet(filepath: str, res: int, rang = (450, 4400): typing.Tuple(int, int)) -> pd.DataFrame:
    spec = pd.read_csv(filepath,
                   sep = ";" 
                   )
    spec = spec[['Wavenumbers [1/cm]', 'Absorbance']]
    spec['Wavenumbers [1/cm]'] = [float(x.replace(',','.')) for x in spec['Wavenumbers [1/cm]']]
    spec['Absorbance'] = [float(x.replace(',','.')) for x in spec['Absorbance']] 
    return spec
# i = 0
# while len(spec) < 2000 + 3:
#     spec.append([0,spec[i]-spec[i+1]])
#     i += 1



# spec = pd.to_numeric(spec)
pl.plot(spec['Wavenumbers [1/cm]'], spec['Absorbance'], linewidth = 0.2, color = 'r')
pl.show()