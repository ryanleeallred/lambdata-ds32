from lambdata.wallet import Wallet
import pytest

@pytest.fixture
def empty_wallet():
    '''returns a wallet object with balance of 0'''
    return Wallet()

@pytest.fixture
def wallet_20():
    '''returns a wallet object with balance of 20'''
    return Wallet(20)
    
def test_empty_wallet(empty_wallet):
    '''Tests wallet init with no balance to be 0'''
    assert empty_wallet.balance == 0
    
def test_wallet_20_init(wallet_20):
    '''Tests wallet init with balance 20 to be 20'''
    assert wallet_20.balance == 20

def test_wallet_20_spend_10(wallet_20):
    '''Tests wallet with balance 20 then spending 10 to have balance 10'''
    wallet_20.spend_cash(10)
    assert wallet_20.balance == 10
    
    