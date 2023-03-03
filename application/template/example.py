#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""例題プログラム変える
"""


def calc(price, discount_rate):
    """与えられた価格と割引率から割引後の価格を計算する関数。

    Args:
        price (int): 価格
        discount_rate (float): 割引率 (0.0~1.0)

    Returns:
        int: 割引後の価格
    """
    price2 = int(price * discount_rate)
    d = price - price2
    return d
