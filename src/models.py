from dataclasses import dataclass


@dataclass
class TechnicalAlert:
    """
    Models technical indicator alerts - fetched from Taapi.io.
    """

    pair: str
    indicator: str
    interval: str
    params: dict
    output_vals: list
    endpoint: str
    name: str
    type: str = "t"


@dataclass
class CEXAlert:
    """
    Models centralized exchange alerts - currently only Binance pairs.
    """

    pair: str
    indicator: str
    params: dict = None
    type: str = "s"


class BinancePriceResponse:
    def __init__(self, response_data: dict):
        # Extracting data from the response, assuming "data" is a list containing one dictionary
        data = response_data.get("data", [{}])[0]

        self.symbol = str(data.get("symbol", ""))
        self.open = float(data.get("open", 0.0))
        self.high24h = float(data.get("high24h", 0.0))
        self.low24h = float(data.get("low24h", 0.0))
        self.lastPrice = float(data.get("lastPr", 0.0))
        self.quoteVolume = float(data.get("quoteVolume", 0.0))
        self.baseVolume = float(data.get("baseVolume", 0.0))
        self.usdtVolume = float(data.get("usdtVolume", 0.0))
        self.timestamp = int(data.get("ts", 0))
        self.bidPrice = float(data.get("bidPr", 0.0))
        self.askPrice = float(data.get("askPr", 0.0))
        self.bidSize = float(data.get("bidSz", 0.0))
        self.askSize = float(data.get("askSz", 0.0))
        self.openUtc = float(data.get("openUtc", 0.0))
        self.changeUtc24h = float(data.get("changeUtc24h", 0.0))
        self.change24h = float(data.get("change24h", 0.0))

    def to_dict(self):
        return {
            "symbol": self.symbol,
            "open": self.open,
            "high24h": self.high24h,
            "low24h": self.low24h,
            "lastPrice": self.lastPrice,
            "quoteVolume": self.quoteVolume,
            "baseVolume": self.baseVolume,
            "usdtVolume": self.usdtVolume,
            "timestamp": self.timestamp,
            "bidPrice": self.bidPrice,
            "askPrice": self.askPrice,
            "bidSize": self.bidSize,
            "askSize": self.askSize,
            "openUtc": self.openUtc,
            "changeUtc24h": self.changeUtc24h,
            "change24h": self.change24h,
        }
