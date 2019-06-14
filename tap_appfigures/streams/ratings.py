from tap_appfigures.streams.base import AppFiguresBase, Record


class RatingsRecord(Record):
    INT_FIELDS = ['total', 'new_total', 'positive', 'negative', 'neutral', 'new_positive', 'new_negative', 'new_neutral', 'product_id']
    FLOAT_FIELDS = ['average', 'new_average']


class RatingsStream(AppFiguresBase):
    STREAM_NAME = 'ratings'
    URI = '/reports/ratings?group_by=products,dates&start_date={}&granularity=daily'
    KEY_PROPERTIES = ['product_id', 'date']
