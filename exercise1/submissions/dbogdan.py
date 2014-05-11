#!/usr/bin/env python

#
# Author: Bogdan Vasile Dumtirica
# Elance: http://dbogdan.elance.com
#

import pandas as pd
import os

in_file = os.path.join(os.path.dirname(__file__), "../input/xl.csv")
mean_file = "mean.csv"
stats_file = "stats.csv"

def main():
    data = pd.read_csv(in_file,
                       na_values = (77, 88),
                       usecols = ('fdntext', 
                                  'fldimp', 
                                  'undrfld', 
                                  'advknow', 
                                  'pubpol', 
                                  'comimp', 
                                  'undrwr', 
                                  'undrsoc', 
                                  'orgimp', 
                                  'impsust'))
    
    mean = data.groupby('fdntext').mean()
    mean.to_csv(mean_file)
    
    stats = mean.describe()
    stats.to_csv(stats_file)

if __name__ == "__main__":
    main()

