class MarketState:

    def __init__(
        self,
        symbol,
        trend,
        volatility,
        bias,
        active_resistance,
        active_support
    ):

        self.symbol = symbol
        self.trend = trend
        self.volatility = volatility
        self.bias = bias
        self.active_resistance = active_resistance
        self.active_support = active_support

    def to_dict(self):

        return {
            "symbol": self.symbol,
            "trend": self.trend,
            "volatility": self.volatility,
            "bias": self.bias,
            "active_resistance": self.active_resistance,
            "active_support": self.active_support
        }