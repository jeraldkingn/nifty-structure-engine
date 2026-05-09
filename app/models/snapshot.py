class Snapshot:

    def __init__(
        self,
        symbol,
        price,
        today_high,
        today_low,
        vwma,
        trend,
        volume_state
    ):

        self.symbol = symbol
        self.price = price
        self.today_high = today_high
        self.today_low = today_low
        self.vwma = vwma
        self.trend = trend
        self.volume_state = volume_state

    def to_dict(self):

        return {
            "symbol": self.symbol,
            "price": self.price,
            "today_high": self.today_high,
            "today_low": self.today_low,
            "vwma": self.vwma,
            "trend": self.trend,
            "volume_state": self.volume_state
        }