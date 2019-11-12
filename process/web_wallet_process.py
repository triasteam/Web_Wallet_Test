#coding=utf-8
import unittest
from case.creat_wallet import CreatWallet
from case.get_coin import GetCoin
from case.get_hidden_coin import GetHiddenCoin
from case.send_public_address_amount import SendPublicAddressAmount
from case.send_public_address_hidden_amount import SendPublicAddressHiddenAmount
from case.send_private_address_amount import SendPrivateAddressAmount
from case.send_private_address_hidden_account import SendPrivateAddressHiddenAmount
from case.check_view_account_info import CheckViewAccountInfo
from common.writeexcel import WriteExcel
import time,os,HTMLTestReportCN
class WebWalletProcess(unittest.TestCase):
    '''
    Go through the trading process
    '''
    def setUp(self):
        pass
    def test_0creat_wallet(self):
        CreatWallet().creat_wallet()
        CreatWallet().creat_wallet()

    def test_1getcoin(self):
        GetCoin().getcoin()
        GetHiddenCoin().get_hidden_coin()

    def test_2check_view_account_info(self):
        CheckViewAccountInfo().check_view_account_info()

    def test_3creat_excel_write_header(self):
        WriteExcel().creat_excel()
        WriteExcel().write_excel(0,['Public Address',
                                    'Public Address Hidden Amount)',
                                    'Private Address',
                                    'Private Address Hidden Amount) ',
                                    'Transfer details',
                                    'Public Address  After',
                                    'Public Address Hidden Amount After',
                                    'Private Address After',
                                    'Private Address Hidden Amount After',])

    def test_4send_public_address_amount(self):
        SendPublicAddressAmount().send_public_address_amount()

    def test_5send_public_adddress_hidden_amount(self):
        SendPublicAddressHiddenAmount().send_public_address_hidden_amount()

    def test_6send_private_address_amount(self):
        SendPrivateAddressAmount().send_private_address_amount()

    def test_7send_private_address_hidden_amount(self):
        SendPrivateAddressHiddenAmount().send_private_address_hidden_amount()

    def tearDown(self):
        pass

if __name__ == '__main__':
    now_time = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
    qian = os.path.abspath('.').split('process')[0]
    # Define a report store path
    filename = qian + 'report' + '\\' + now_time + 'result.html'
    fp = open(filename, 'wb')

    testsuite=unittest.TestSuite()
    testsuite.addTest(WebWalletProcess('test_0creat_wallet'))
    testsuite.addTest(WebWalletProcess('test_1getcoin'))
    testsuite.addTest(WebWalletProcess('test_2check_view_account_info'))
    testsuite.addTest(WebWalletProcess('test_3creat_excel_write_header'))
    testsuite.addTest(WebWalletProcess('test_4send_public_address_amount'))
    testsuite.addTest(WebWalletProcess('test_5send_public_adddress_hidden_amount'))
    testsuite.addTest(WebWalletProcess('test_6send_private_address_amount'))
    testsuite.addTest(WebWalletProcess('test_7send_private_address_hidden_amount'))
    runner=HTMLTestReportCN.HTMLTestRunner(

        stream=fp,
        title=u'web wallet process,',
        description=u'case execution'
    )
        # Run the test case
    runner.run(testsuite)

    fp.close()