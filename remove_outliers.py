import pandas as pd
import numpy as np
import sys
import matplotlib.pyplot as plt

# Outlier Moving Window Filter
#
# Expects a csv file with multiple columns as the second input argument.
# Specify the column to be filtered as the column variable.
# Column variable can be either column number, or header as a string.
#
# User controlled threshold of filter with the scale variable
# Reccomended 10 - 20
#
# Will generate plots of raw data and filtered data.
# Does not save data to anything, if you want to write the data use df_filtered
#
# Can save to csv with:
# df_filtered.to_csv("csvName.csv") #(put this line at the end of the code)
#
# Examples are Wind Files with U, V , W and Magnitude columns. Will filter the
# magnitude column
#
# Created by:
#            Avinash Muthu Krishnan, muthukra@erau.edu
#
# Created :
#           16 Oct 2024



if len(sys.argv) < 2:
    print("one argument missing")
    print("usage:")
    print('\t{0} [csv file]'.format(sys.argv[0]))
    print(" ")
    print('examples:\n\t{0} 2024_05_10_10_05_00.csv, sphere_log_00.csv'.format(sys.argv[0]))
    sys.exit()
else:
    csv_file=sys.argv[1]
    print('using:\tcsv=[{0}]'.format(csv_file))



df = pd.read_csv(csv_file)

# Put desired column here
column = "Mag"


# Choose the threshold scale here.
scale = 10


Meaner = (abs(df[column].diff()) ).mean()

thres = Meaner*scale

outlier_indices = []

for i in range(len(df[column])):
    if i < 2:
        j = 2 # Do Nothing for first 3 points
    else:
        # Select the previous and next points
        previous = df[column].iloc[i-1]
        try:
            next = df[column].iloc[i+1]
        except:
            next = df[column].iloc[i]
        now = df[column].iloc[i]

        # Filter Logic. "&" is imporntat in making this work
        if ( ( abs(now - previous) > thres ) & (abs(now - next) > thres )  ):
            outlier_indices.append(i)

df_filtered = df.drop(outlier_indices)

print('******** moving window filter **************')
if (len(outlier_indices) == 0):
    print('NO OUTLIERS! :)')
    plt.figure(10)
    ax = plt.subplot()
    ax.plot( df[column])
    ax.set(xlabel='Sample #', ylabel='Wind Mag (m/s)',
           title='Raw Data')
else:
    plt.figure(10)
    ax = plt.subplot()
    ax.plot( df[column])
    ax.set(xlabel='Sample #', ylabel='Wind Mag (m/s)',
           title='Raw Data, Pre-filtered')


    plt.figure(20)
    ax = plt.subplot()
    ax.plot( df_filtered[column])
    ax.set(xlabel='Sample #', ylabel='Wind Mag (m/s)',
           title='Outliers Filtered Data')


for i in range(len(outlier_indices)):
    print('Outlier at Index ', outlier_indices[i] , ' = ', df[column][outlier_indices[i]],' (m/s)')
print('*******************************')

Meanest = (abs(df_filtered[column].diff()) ).mean()

print("MEAN of Diff = ",Meaner)
print("MEAN of Filtered Diff = ",Meanest)

plt.show()
