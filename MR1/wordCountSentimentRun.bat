REM This batch script runs a word count sentiment analyis mapreduce implemenation on a Steam review dataset

REM data_sample1.txt


type dataset.txt | wordCountSentMapper.py | sort | wordCountSentReducer.py > wordCountSentReducer_output.txt

