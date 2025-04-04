# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 11:52:37 2025

@author: 91766
"""

class InsufficientFundsError(Exception):
    """Custom exception for insufficient balance """
    
    
   
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        """
        Withdraws money from the account.
        
        :param amount: Amount to withdraw
        :return: Remaining balance or error message
        """
        try:
            # TODO: 
            if amount < 0:
                raise ValueError("Withdrawal amount cannot be negative.")
            if amount > self.balance:
                raise InsufficientFundsError("Insufficient funds in the account.")
            self.balance -= amount
            return self.balance
            print(self.balance-self.amount)
        except ValueError as e:
            print(e)
            pass  # TODO: Handle negative withdrawal amounts
        except InsufficientFundsError as e:
            print(e)
            pass  # TODO: Handle insufficient funds
        except Exception as e:
            print(e)
            pass  # TODO: Handle unexpected errors
        finally:
            print(self.balance )

# Example Usage:
account = BankAccount(100)
print(account.withdraw(150))  # Should raise InsufficientFundsError
print(account.withdraw(-10))  # Should raise ValueError