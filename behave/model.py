from datetime import datetime


class Candle:
    """
    Example Data: [1718582400000,"66653.50","66915.40","66116.00","66200.00","26541.924",1718596799999,"1762908795.38740",334631,"12831.628","852351951.24160","0"]
        data[0]: 开始时间戳
        data[1]: 开盘价
        data[2]: 最高价
        data[3]: 最低价
        data[4]: 收盘价
        data[5] 结束时间戳
    """

    def __init__(self, data):
        self.data = data
        self.start_at = data[0] / 1000.0
        self.start_price = data[1]
        self.high_price = data[2]
        self.low_price = data[3]
        self.end_price = data[4]
        self.end_at = data[6]/ 1000.0

    def __getitem__(self, item):
        return self.data[item]

    def __str__(self):
        return "{} - {}, 开盘:{}, 收盘:{}, 最高:{}, 最低:{}".format(datetime.fromtimestamp(self.start_at).strftime('%Y-%m-%d %H:%M:%S'),
                                                                       datetime.fromtimestamp(self.end_at).strftime('%Y-%m-%d %H:%M:%S'),
                                                                       self.start_price, self.end_price, self.high_price, self.low_price)

    def upper_shadow(self):
        # 上影线 = 最高价 - 收盘价（如果收盘价高于开盘价）或者 最高价 - 开盘价（如果收盘价低于开盘价）
        return max(self.high_price - self.end_price, self.high_price - self.start_price)

    def lower_shadow(self):
        # 下影线 = 开盘价 - 最低价（如果收盘价高于开盘价）或者 收盘价 - 最低价（如果收盘价低于开盘价）
        return max(self.start_price - self.low_price, self.end_price - self.low_price)

    def price_change(self):
        # 涨跌价 = 收盘价 - 开盘价
        return self.end_price - self.start_price

    def amplitude(self):
        # 振幅 = (最高价 - 最低价) / 开盘价 * 100
        return (self.end_price - self.start_price) / self.start_price * 100

    def amplitude_large(self):
        # 振幅 = (最高价 - 最低价) / 开盘价 * 100
        return (self.high_price - self.start_price) / self.start_price * 100

    def is_contained(self, candle) -> bool:
        """
        当前candle是否被包含：通过开盘，收盘计算是否包含
        :param candle:
        :return: boolean
        """
        if self.start_price < candle.end_price < self.end_price:
            return True
        elif self.start_price > candle.end_price > self.end_price:
            return True
        else:
            return False


class Candles:
    """
     传入参数，不带最后一个，因为他没有跑完
    """

    def __init__(self, datas):
        self.datas = datas[:-1]
        self.candles = [Candle(candle) for candle in self.datas]


    def __getitem__(self, item):
        return self.candles[item]

    def __len__(self):
        return len(self.candles)

    def __str__(self):
        res = []
        for can in self.candles:
            res.append(str(can))
        return '\n'.join(res)

    def convert_to_3_line(self):
        res = []
        for i in range(len(self) - 1, 0, -1):
            if self[i].is_contained(self.candles[i - 1]):
                continue
            else:
                res.append(self.datas[i])
            if len(res) == 3:
                break
        return Candles(res)

