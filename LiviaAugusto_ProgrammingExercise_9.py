# This program creates a BankAcct Class with attributes for name, account
# number, amount, and interest rate. -Livia Augusto Razera, Assignment 9.

# BankAcctt Class that has state info about the user.
class BankAcct:
    def __init__(self, name, account_number, amount, interest_rate):
        self.name = name
        self.account_number = account_number
        self.amount = amount  
        self.interest_rate = interest_rate  

    # Function to adjust the interest rate for withdraws and deposits,
    # and for giving balance.
    def adjust_interest_rate(self, new_rate):
        if new_rate >= 0:
            self.interest_rate = new_rate
        else:
            print('Interest rate cannot be negative.')

    # Function that withdraws from the account.
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.amount:
                self.amount -= amount
            else:
                print('Insufficient funds.')
        else:
            print('Withdrawal amount must be positive.')

    # Function that deposits into account.
    def deposit(self, amount):
        if amount > 0:
            self.amount += amount
        else:
            print('Deposit amount must be positive.')

    # Function that gets balance from account.
    def get_balance(self):
        return self.amount

    # Function that calculates the interest.
    def calculate_interest(self, days):
        interest = self.amount * self.interest_rate * (days / 365)
        return interest

    # Function to use __str__ method to display balances and interest amounts.
    def __str__(self):
        return (f'Account Holder: {self.name}\n'
                f'Account Number: {self.account_number}\n'
                f'Balance: ${self.amount:.2f}\n'
                f'Interest Rate: {self.interest_rate * 100:.2f}%')

# Test function.
def test_bank_acct():
    acct = BankAcct('Livia Razera', '326712239',
                    2769.0, 0.04)

    # Display results.
    print('Initial Account Info:')
    print(acct)
    print()
    print('Depositing $250')
    acct.deposit(550)
    print()
    print('Withdrawing $400')
    acct.withdraw(270)
    print()
    print('Adjusting interest rate to 7%')
    acct.adjust_interest_rate(0.07)
    print()
    print('Calculating interest for 60 days')
    interest = acct.calculate_interest(60)
    print(f'Interest earned in 60 days: ${interest:.2f}')
    print()
    print('Final Balance:')
    print(f'${acct.get_balance():.2f}')

# Run the test
if __name__ == '__main__':
    test_bank_acct()