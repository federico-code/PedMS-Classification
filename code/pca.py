import pandas as pd
import numpy as np
import sys
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA



def _PCA(df, COMPONENTS=47):
    x, y = df.iloc[:,:-1], df.iloc[:, -1] 
    X = pd.DataFrame(StandardScaler().fit_transform(x))

    pca = PCA(n_components=COMPONENTS)
    principalComponents = pca.fit_transform(X)

    columns = []
    for i in range(COMPONENTS):
        columns.append("PC"+str(i+1))

    principalDf = pd.DataFrame(data = principalComponents, columns=columns)

    principalDf["target"] = y.tolist()
    return principalDf
    


# def main():
#     data = read_data(sys.argv[1])
#     _PCA(data).to_csv(sys.argv[2], sep="\t")

 
# # python pca.py .\data\new_data.txt .\data\pca_data.txt
# if __name__== "__main__":
#   main()
