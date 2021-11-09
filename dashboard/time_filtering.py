from datetime import datetime
from dateutil.relativedelta import relativedelta

def filter_time(df, days = 0):
    """Return dataframe with a range of days which is input"""

    # .date() removes clock, retains date
    last_day = df.index[0].date()

    start_day = last_day - relativedelta(days = days)

    # Possible to run withour sorting, but then we get a warning, unknown why
    df = df.sort_index().loc[start_day:last_day]

    return df
