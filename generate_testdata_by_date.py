# Takes test data, splits by date and creates .csv file for each

from datetime import datetime, timedelta
import pandas as pd
import os
MODEL_DIR = './test_data/'
if not os.path.exists(MODEL_DIR):
    os.mkdir(MODEL_DIR)


def split_by_date(df22):
    fd = datetime.strptime(df22['Date'].iloc[0],'%m/%d/%Y %H:%M').date()
    ld = datetime.strptime(df22['Date'].iloc[-1],'%m/%d/%Y %H:%M').date()
    print('First date: ', fd)
    print('Last date: ', ld)
    print('Difference: ', (ld - fd).days, 'days')     # difference + 1 = number of test sets
    print((ld - fd).days + 1, 'files will be generated.')
    for i in range((ld - fd).days + 1 ):     # from 0 to difference
        df = df22.loc[df22.Date.apply(lambda x: datetime.strptime(x,'%m/%d/%Y %H:%M').date() ==
            (fd + timedelta(days=i)))]
        df.to_csv(f'./test_data/test_{(fd + timedelta(days=i)).month:02d}{(fd + timedelta(days=i)).day:02d}.csv')
    

split_by_date(df3)

