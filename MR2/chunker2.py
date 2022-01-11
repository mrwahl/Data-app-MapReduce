import pandas as pd

chunk_size = 4939
batch_no = 1

for chunk in pd.read_csv('DublinData.csv', chunksize=chunk_size , encoding='ISO-8859-1'):
    chunk.to_csv('data_sample' + str(batch_no) + '.csv', index=False)
    batch_no +=1