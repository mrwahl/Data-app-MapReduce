REM Locally test topN houses mapper and reducer

REM Run mapper on 1st data split, output to file
type data_sample1.txt | topNHouseMapper.py > top20HousesMapper_output.txt

REM Run mapper on 2nd data split, append to the same file
type data_sample2.txt | topNHouseMapper.py >> top20HousesMapper_output.txt


REM Run the reducer, output to file
type top20HousesMapper_output.txt | sort | topNHouseReducer.py > top20HouseReducer_output.txt

