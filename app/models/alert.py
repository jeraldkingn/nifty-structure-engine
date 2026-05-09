class Alert:

    def __init__(
        self,
        signal_type,
        price,
        confidence,
        market_bias,
        message
    ):

        self.signal_type = signal_type
        self.price = price
        self.confidence = confidence
        self.market_bias = market_bias
        self.message = message

    def to_dict(self):

        return {
            "signal_type": self.signal_type,
            "price": self.price,
            "confidence": self.confidence,
            "market_bias": self.market_bias,
            "message": self.message
        }