def transfer_amount(accounts, sender, recipient, amount):
    '''
    Performs a transaction between two accounts if the transaction is valid.

    Args:
        accounts (dict): A dictionary of account numbers and their respective balances.
        sender (str): The account number of the sender.
        recipient (str): The account number of the recipient.
        amount (int): The amount to be transferred.

    Returns:
        None - this updates the dictionary accordingly.
    '''
    if accounts.keys().__contains__(sender) and accounts.keys().__contains__(recipient):
        a = accounts[sender]
        b = accounts[recipient]
        if a >= amount > 0:
            accounts[sender] = a - amount
            accounts[recipient] = b + amount
