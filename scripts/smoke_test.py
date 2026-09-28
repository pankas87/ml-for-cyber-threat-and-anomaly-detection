"""Smoke test del entorno: importa librerias clave, imprime versiones,
y entrena KNeighborsClassifier + OneClassSVM sobre datos sinteticos."""

import sys

import matplotlib
import numpy as np
import pandas as pd
import seaborn as sns
import sklearn
from sklearn.datasets import make_blobs
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import OneClassSVM

print(f"python      {sys.version.split()[0]}")
print(f"numpy       {np.__version__}")
print(f"pandas      {pd.__version__}")
print(f"matplotlib  {matplotlib.__version__}")
print(f"seaborn     {sns.__version__}")
print(f"scikit-learn {sklearn.__version__}")

X, y = make_blobs(n_samples=200, centers=3, n_features=4, random_state=42)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X, y)
print(f"\nKNeighborsClassifier entrenado. accuracy en train: {knn.score(X, y):.3f}")

ocsvm = OneClassSVM(gamma="auto")
ocsvm.fit(X)
preds = ocsvm.predict(X)
inliers = (preds == 1).sum()
print(f"OneClassSVM entrenado. inliers detectados: {inliers}/{len(X)}")

print("\nSmoke test OK.")
