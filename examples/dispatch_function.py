# example of dispatch 这个方法令我耳目一新！
# 下面这是function 和 class 不同，class可以用exp.method，这里用的是不同frame
def account(initial_balance):
    """Account constructor"""
    def deposit(amount):
        dispatch['balance'] += amount
        return dispatch['balance']
    def withdraw(amount):
        if amount > dispatch['balance']:
            return 'Insufficient funds'
        dispatch['balance'] -= amount
        return dispatch['balance']
    dispatch = {'deposit':   deposit,
                'withdraw':  withdraw,
                'balance':   initial_balance}
    return dispatch

# Two different operations on account
def withdraw(account, amount):
    return account['withdraw'](amount)
def deposit(account, amount):
    return account['deposit'](amount)

# Selector.Check the balance
def check_balance(amount):
    return account['balance']
