import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def get_path(filename):
    directory = os.path.join(os.path.dirname(__file__))
    filepath = os.path.join(directory, filename)
    return os.path.normpath(filepath)

predictions = pd.read_csv(get_path('test.txt'), sep=';')
predictions['Prediction'] = pd.to_datetime(predictions['Prediction'], errors='coerce')
predictions['decimal time'] =predictions['Prediction'].dt.hour +predictions['Prediction'].dt.minute / 60
predictions.info()

plt.scatter(predictions['decimal time'],
            predictions['Prediction'])
plt.xlabel('decimal time')
plt.ylabel('predictions')
plt.savefig(get_path('test.svg'))