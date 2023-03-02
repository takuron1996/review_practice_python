#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""例題プログラム
"""

from template.example import calc


def test_calc():
    """正常系のテスト"""
    assert calc(10, 0.5) == 5


def test_calc2():
    """割引率が整数のテスト"""
    assert calc(10, 5) == -40


def test_calc3():
    """割引率が1より大きい場合のテスト"""
    assert calc(10, 1.5) == -5


def test_calc4():
    """価格が小数のテスト"""
    assert calc(10.5, 0.2) == 8.5


def test_calc5():
    """割引率が0の場合のテスト"""
    assert calc(10, 0) == 10


def test_calc6():
    """割引率が1の場合のテスト"""
    assert calc(10, 1) == 0


def test_calc7():
    """価格がマイナスのテスト"""
    assert calc(-5, 0.5) == -3


def test_calc8():
    """割引率がマイナスのテスト"""
    assert calc(10, -1) == 20
