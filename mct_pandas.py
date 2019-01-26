import pandas as pd
import csv
mct_data_frame = pd.read_csv('mct1_data0.csv')
print mct_data_frame.head(10)
#print (mct_data_frame.info())

#selecting a column from the mct_data_frame
#height is a column name
height = mct_data_frame.height
height_weight_pre = mct_data_frame[['height', 'weight', 'pre']]
#print height_weight_pre

#Selecting a row from data mct_data_frame
#Zero indexed
subject_two = mct_data_frame.iloc[1]
subjects_two_three_five_seven = mct_data_frame.iloc[[2, 3, 5, 7]]
subjects_two_three_five_seven.reset_index(inplace = True, drop = True) #This drops the indexing scheme from the old column
#print subjects_two_three_five_seven

# Querying from csv samples
# mct_data_frame[(mct_data_frame.subject_id = 1)
#Querying from data frame
short_heavy = mct_data_frame[(mct_data_frame.weight > 65) & (mct_data_frame.height < 170)]
#print short_heavy

#Creating New Columns
mct_data_frame['Fold Increase'] = mct_data_frame['post'] / mct_data_frame['pre']

#mct_data_frame['area_code'] = mct_data_frame.phone_number.apply(
#lambda x: x.split('-')[0]

#writing to csv in pandas
#df.to_csv('new-csv-file.csv')
#height_weight_pre.to_csv('height_weight_pre.csv')
