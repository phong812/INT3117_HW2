import pytest
import Main
def test_01():
    assert Main.Calculate_ticket_price(16, 100, 1000) == 700
def test_02():
    assert Main.Calculate_ticket_price(17, 101, 500000) == 350000
def test_03():
    assert Main.Calculate_ticket_price(46, 120, 1000000) == 850000
def test_04():
    assert Main.Calculate_ticket_price(30, 160, 200000) == 200000
def test_05():
    assert Main.Calculate_ticket_price(81, 201, 1000000) == -1
