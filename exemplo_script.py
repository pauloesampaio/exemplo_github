import pandas as pd
import os
import numpy

teste = pd.read_csv("exemplo_arquivo.csv")
teste.to_parquet("exemplo_parquet.parquet")

grouped = teste.groupby().sum()
