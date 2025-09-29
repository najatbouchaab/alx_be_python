class BankAccount:
    """A simple bank account class that manages deposits, withdrawals, and balance."""
    
    def __init__(self, initial_balance=0):
        """Initialize the bank account with an optional initial balance.
        
        Args:
            initial_balance (float): Starting balance for the account. Defaults to 0.
        """
        self.account_balance = initial_balance
    
    def deposit(self, amount):
        """Add the specified amount to the account balance.
        
        Args:
            amount (float): The amount to deposit.
        """
        self.account_balance += amount
    
    def withdraw(self, amount):
        """Deduct the amount from account balance if funds are sufficient.
        
        Args:
            amount (float): The amount to withdraw.
            
        Returns:
            bool: True if withdrawal was successful, False if insufficient funds.
        """
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False
    
    def display_balance(self):
        """Print the current account balance in a user-friendly format."""
        print(f"Current Balance: ${self.account_balance:.2f}")