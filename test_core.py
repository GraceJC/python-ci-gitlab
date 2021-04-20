import pytest

from cathay.sample.customer import Customer
from cathay.sample.core import CustomerDataProcess
from decimal import Decimal, ROUND_DOWN

INIT_MONEY=100.0

class TestCoreSuites:
##########################################################################################
#
# 假設這位客戶, 名字是 Test User, 帳號為100-1100, 一開始帳戶會先存100元, 要測試下面項目: 
#
# 1. 之後存款 1000 元, 確認帳戶總金額為 1100 元
# 2. 下一步提款 500 元, 確認帳戶總金額為 600 元
# 3. 假設銀行年利率是10%, 經過一年之後確認帳戶餘額為660元
# 4.之後提款 700 元, pytest 預期會接到 RuntimeError
#
##########################################################################################
#    def __init__(self,customer:Customer):       
#       customer.deposit(INIT_MONEY)
#       self.customer = customer
        
    def test_1(self):
        self.customer.deposit(1000)
#        print(self.customer.deposit)
        assert self.customer.balance == 1100

    def test_2(self):
        self.customer.withdraw(500)
        assert self.customer.balance == 600

    def test_3(self):
        CustomerDataProcess.add_interest(customer,0.1)
        assert self.customer.balance == 660
    
    def test_4():
        with pytest.raises(RuntimeError) as ex:
            customer.withdraw(700)
        assert ex is RuntimeError

customer = Customer('Test User','100-1100')
customer.deposit(INIT_MONEY)
c=TestCoreSuites(customer)
c.test_1()
c.test_2()
c.test_3()
c.test_4()
    #test_1()
    #test_2()
    #test_3()
    #test_4()
