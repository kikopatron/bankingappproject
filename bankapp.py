import pandas as pd
import csv
import os


class BankingApp():
    def __init__(self):
        self.BankingQuestions()
        self.BankingTable()
        self.openingBalance = 0
        self.endBalance = self.openingBalance
        self.filename = "bankingapptransactions.csv"

        
    def BankingQuestions(self):
        self.q_name = "What's your name? "
        self.q_deposit = "How much do you want to deposit? "
        self.q_withdrawal = "How much do you want to withdrawal? "
        self.anotherone = "Would you like to continue?\nType: Yes or No "
        self.saveTrans = "Would you like to save this transaction?\nType: Yes or No"
    
    def BankBegin(self):
        self.name = input(self.q_name)
        self.BankingPrompt()

    def BankSaveTran(self):
        df = pd.DataFrame(self.BankingInfoTable)
        df.to_csv(self.filename, index=False)
        print(df.tail())    

    def BankingPrompt(self):
        while True:
            self.deposit = float(input(self.q_deposit))
            self.BankingInfoTable['Deposit'].append(self.deposit)
            self.withdrawal = float(input(self.q_withdrawal))
            self.BankingInfoTable['Withdrawal'].append(self.withdrawal)
            self.BankingCalc()
            self.BankingInfoTable['Balance'].append(self.endBalance)
            self.nxttran = input(self.anotherone)
            if self.nxttran == "Yes":
                continue
            if self.nxttran == "No":
                self.BankingTranPrompt()
                break
            print("Please type 'No' or 'Yes'")
        
    def BankingTranPrompt(self):
        self.downTran = input(self.saveTrans)
        if self.downTran == "Yes":
            self.BankSaveTran()
        elif self.downTran == "No":
            print(f"Good-Bye! {self.name}")
        elif self.downTran != "Yes" | "No":
            self.BankingTranPrompt()    


    def BankingCalc(self):
        # self.BankingTable()
        self.endBalance = self.endBalance + self.deposit
        self.endBalance = self.endBalance - self.withdrawal
        print(f"{self.name}, you have ${self.endBalance} in your account!")
    
    def BankingTable(self):
        self.BankingInfoTable = {
            'Deposit':[],
            'Withdrawal':[],
            'Balance':[],
            }


bnk = BankingApp()
bnk.BankBegin()