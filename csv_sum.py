import tarfile
import pandas as pd
import time
def check_sum():
    with tarfile.open("data.tgz", "r:gz") as tar:
        tar.extractall()
    df = pd.read_csv("data.csv", sep=",", header=None)
    return df.values.sum() == 10

if __name__ == "__main__":
    result = check_sum()
    print(result)
