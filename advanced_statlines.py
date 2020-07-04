from collections import namedtuple

import pandas as pd
import numpy as np

ColFunction = namedtuple('StatFunction', 'name func')


PA_lambda = lambda row: row.AB + row.BB + row.HBP + row.SH + row.SF
OBP_lambda = lambda row: (row.H + row.BB + row.HBP) / (row.PA) if row.PA > 0 else np.NaN
AVG_lambda = lambda row: row.H / row.AB if row.AB > 0 else np.NaN

stat_functions = [
    ColFunction(name='PA', func=PA_lambda),
    ColFunction(name='OBP', func=OBP_lambda),
    ColFunction(name='AVG', func=AVG_lambda)
]

def format_df(df):
    formatted_copy = df.copy()
    for func in stat_functions:
        formatted_copy[func.name] = formatted_copy.apply(func.func, axis=1)
    return formatted_copy

def order_by(df, sort_column, ascending):
    df_copy = df.copy()
    df_copy.sort_values(by=sort_column, inplace=True, ascending=ascending)
    df_copy.reset_index(drop=True, inplace=True)
    return df_copy

