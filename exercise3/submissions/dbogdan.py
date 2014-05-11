#!/usr/bin/env python

#
# Author: Bogdan Vasile Dumtirica
# Elance: http://dbogdan.elance.com
#


from os.path import join, dirname, normpath
import pandas as pd
from collections import OrderedDict
import json

in_path = normpath(join(dirname(__file__),"../input"))
in_mean = join(in_path, "mean.csv")
in_pct = join(in_path, "pct.csv")
in_stats = join(in_path, "stats.csv")
out_file = "output.json"
q_list = ('fldimp', 'undrfld', 'advknow','pubpol',  
          'comimp', 'undrwr', 'undrsoc', 'orgimp', 'impsust')
client = "Tremont 14S"


def main():

    mean = pd.read_csv(in_mean)
    stats = pd.read_csv(in_stats)
    pct = pd.read_csv(in_pct)

    client_index = mean[(mean.fdntext == client)].index[0]

    elements_dict = OrderedDict()
    for q in q_list:
        q_dict = {} 
        q_dict['type'] = 'percentileChart'
        # absolutes
        abs_list = [stats[q].iloc[idx] for idx in range(3,8)]
        q_dict['absolutes'] = abs_list
        # current
        cur_dict = OrderedDict()
        cur_dict['name'] = '2014'
        cur_dict['value'] = mean[q].iloc[client_index]
        cur_dict['percentage'] = pct[q].iloc[client_index]
        q_dict['current'] = cur_dict
        # others
        q_dict['cohorts'] = []
        q_dict['past_results'] = []
        q_dict['segmentations'] = []
        
        elements_dict[q] = q_dict

    reports_array = OrderedDict([
        ('name', client+' Report'),
        ('title', client+' Report'),
        ('cohorts', []),
        ('segmentations', []),
        ('elements', elements_dict)
        ])
    json_dict = OrderedDict([
        ('version', '1.0'), 
        ('reports', reports_array)
        ])
    
    with open(out_file, 'wb') as of:
        json.dump(json_dict, of)
    

if __name__ == '__main__':
    main()


