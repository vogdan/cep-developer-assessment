#!/usr/bin/env python

#
# Author: Bogdan Vasile Dumtirica
# Elance: http://dbogdan.elance.com
#

from scipy.stats import percentileofscore
import pandas as pd
import os

in_file = os.path.join(os.path.dirname(__file__),"../input/mean.csv")
out_file = "pct.csv"

def get_percentile_from_rating(rating_list):
    percentile_list = []
    for r in rating_list:
        percentile = percentileofscore(rating_list, r, kind='mean')
        percentile_list.append(percentile)
    return percentile_list

def main():
    mean = pd.read_csv(in_file)
    percentile_cols = []
    for col_name in mean:
        if col_name == 'fdntext':
            percentile_list = list(mean[col_name])
        else:
            percentile_list = get_percentile_from_rating(mean[col_name])
        percentile_cols.append((col_name,percentile_list))

        data = pd.DataFrame.from_items(percentile_cols)
        data.to_csv(out_file, index=False)

if __name__ == "__main__":
    main()
