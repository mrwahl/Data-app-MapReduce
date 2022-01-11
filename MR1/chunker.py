import pandas as pd

chunk_size = 15000
batch_no = 1

for chunk in pd.read_csv('dataset.csv', chunksize=chunk_size):
    chunk.to_csv('data_sample' + str(batch_no) + '.csv', index=False)
    batch_no +=1