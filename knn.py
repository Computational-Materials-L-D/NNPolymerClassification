### K Nearest Neighbor for FTIR Spectra
import torch as t
import numpy as np
import typing

def init(spec, batchSize):
    model = nn.Sequential(
        nn.Conv1D(1, len(spec), 5),
        nn.ReLU(),
        nn.MaxPool1D((2, 2)),
        nn.Conv1D(..., ..., 10),
        nn.ReLU(),
        nn.MaxPool1D(4),
        nn.Conv1D(..., ..., 15),
        nn.ReLU(),
        nn.MaxPool1D(4),
        nn.Flatten(),
        nn.Linear(... ,...),
        nn.Dropout(),
        nn.Linear(... ,...)
    )
    return None
