import pandas as pd
from scipy.io import arff

# CSV dosyasını yükleme
df = pd.read_csv('ecommerce_data.csv')

# .arff dosyasına dönüştürme
with open('ecommerce_data.arff', 'w') as f:
    f.write('@RELATION veri_seti\n\n')
    for column in df.columns:
        if df[column].dtype == 'object':
            f.write(f'@ATTRIBUTE {column} STRING\n')
        else:
            f.write(f'@ATTRIBUTE {column} NUMERIC\n')
    f.write('\n@DATA\n')
    for index, row in df.iterrows():
        f.write(','.join(map(str, row)) + '\n')
