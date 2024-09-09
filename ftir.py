import typing
import numpy as np
import pandas as pd
import scipy as sp
from scipy import signal
import torch 
import torch.nn as nn
import matplotlib.pyplot as pl
import pyspectra as ps
import spectrochempy as scp

# Process FTIR Data
def readNicoletScp(filepath: str, res: int, rang: int = (450, 4400)):
    data = scp.read_omnic(filepath)
    print(data.name, data.author, data.description, data.created)
    print(data.data, data.values, data.units, data.shape)
    print(data.x, data.y, data.dims)

    subplot = X[:, 2300.0:1900.0:].plot()

    return data

def readNicoletCsv(filepath: str, res: int, rang = (450, 4400)):
    spec = pd.read_csv(filepath, sep = ";")
    spec = spec[['Wavenumbers [1/cm]', 'Absorbance']]
    spec['Wavenumbers [1/cm]'] = [float(x.replace(',','.')) for x in spec['Wavenumbers [1/cm]']]
    spec['Absorbance'] = [float(x.replace(',','.')) for x in spec['Absorbance']] 
    return spec

def readOld():
    # Loading
    spec = pd.read_csv("C:/Users/guilh/OneDrive/Documents/Pesquisa/ML MIT/FTIR NN/polyethylene_ref.csv",
                   sep = ";" 
                   )
    spec = spec[['Wavenumbers [1/cm]', 'Absorbance']];

    # Cleansing
    spec['Wavenumbers [1/cm]'] = [float(x.replace(',','.')) for x in spec['Wavenumbers [1/cm]']]
    spec['Absorbance'] = [float(x.replace(',','.')) for x in spec['Absorbance']]

    # Range and Resolution
    #spec = signal.resample_poly(spec, 2, 4)
    spec = spec.iloc[rang[0]:rang[1], :]
    # i = 0
    # while len(spec) < 2000 + 3:
    #     spec.append([0,spec[i]-spec[i+1]])
    #     i += 1



    # spec = pd.to_numeric(spec)
    pl.plot(spec['Wavenumbers [1/cm]'], spec['Absorbance'], linewidth = 0.2, color = 'r')
    pl.show()
    return spec






