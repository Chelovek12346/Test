def request():
    while True:
        n = int(input())
        if n > 0:
            return n
        else:
            print("Stupid ahh bro enter a number greater than 0")

def requer():
    while True:
        n = int(input())
        if 3<=n<=9:
            return n
        else:
            print("Stupid ahh bro enter a number between 3 and 9")

class ATM:
    def __init__(self):
        self.balance = 20000
        self.withdrawals = [0,0]

    def update(self, n):
        if n == 0:
            print('Successful withdrawals:', self.withdrawals[1])
            print('Total withdrawals:', self.withdrawals[0])
            print('Final balance:', self.balance)
            exit()
        elif n < 0:
            print('Invalid amount')
            self.withdrawals[0]+=1
        elif n%1000:
            print('Use multiples of 1000')
            self.withdrawals[0] += 1
        elif n > self.balance:
            print('Insufficient funds')
            self.withdrawals[0] += 1
        else:
            self.balance -= n
            self.withdrawals[0] += 1
            self.withdrawals[1] += 1
            print('Successful withdrawal, remaining balance: ', self.balance)