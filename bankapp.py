import pandas as pd

class BankingApp():
    def __init__(self):
        self.BankingQuestions()
        self.BankingTable()
        
    def BankingQuestions(self):
        self.q_name = "What's your name? "
        self.q_deposit = "How much do you want to deposit? "
        self.q_withdrawal = "How much do you want to withdrawal? "
        self.anotherone = "Would you like to continue?\nType: Yes or No "
    
    def BankBegin(self):
        self.name = input(self.q_name)
        self.BankingPrompt()
        df = pd.DataFrame(self.BankingInfoTable)
        df.to_csv("banking_trans.csv")
        print(df.tail())

    def BankingPrompt(self):
        
        self.deposit = float(input(self.q_deposit))
        self.BankingInfoTable['Deposit'].append(self.deposit)
        self.withdrawal = float(input(self.q_withdrawal))
        self.BankingInfoTable['Withdrawal'].append(self.withdrawal)
        self.BankingCalc()
        self.BankingInfoTable['Balance'].append(self.endBalance)
        self.nxttran = input(self.anotherone)
        while self.nxttran == "Yes":
            self.BankingPrompt()
            if self.nxttran == "No":
                print("Good-bye!")
            else:
                break
    
    def BankingCalc(self):
        # self.BankingTable()
        self.endBalance = self.deposit - self.withdrawal
        print(f"{self.name}, you have ${self.endBalance} in your account!")
    
    def BankingTable(self):
        self.BankingInfoTable = {
            'Deposit':[],
            'Withdrawal':[],
            'Balance':[],
            }


bnk = BankingApp()
bnk.BankBegin()