class Alert:

    def __init__(
        self,
        signal,
        price,
        confidence,
        market_bias,
        message
    ):

        self.signal = signal
        self.price = price
        self.confidence = confidence
        self.market_bias = market_bias
        self.message = message

    def to_dict(self):

        return {
            "signal": self.signal,
            "price": self.price,
            "confidence": self.confidence,
            "market_bias": self.market_bias,
            "message": self.message
        }