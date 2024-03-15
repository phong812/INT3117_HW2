import pytest
import Main
def test_06():
    assert Main.Calculate_ticket_price(15, 110, 10000) == -1
def test_07():
    assert Main.Calculate_ticket_price(18, 90, 20000) == -1
def test_08():
    assert Main.Calculate_ticket_price(20, 120, 51000) == 35700
def test_09():
    assert Main.Calculate_ticket_price(22, 160, 80000) == 64000
def test_10():
    assert Main.Calculate_ticket_price(25, 210, 300000) == -1
def test_11():
    assert Main.Calculate_ticket_price(30, 120, 120000) == 102000
def test_12():
    assert Main.Calculate_ticket_price(35, 170, 250000) == 250000