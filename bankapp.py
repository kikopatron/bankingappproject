class BankingApp():
    def __init__(self):
        self.BankingQuestions()
        
    def BankingQuestions(self):
        self.q_name = "What's your name? "
        self.q_deposit = "How much do you want to deposit? "
        self.q_withdrawal = "How much do you want to withdrawal? "
        self.anotherone = "Would you like to continue?\nType: Yes or No "
    
    def BankBegin(self):
        self.name = input(self.q_name)
        self.BankingPrompt()

    def BankingPrompt(self):
        self.deposit = float(input(self.q_deposit))
        self.withdrawal = float(input(self.q_withdrawal))
        self.BankingCalc()
        self.nxttran = input(self.anotherone)
        while self.nxttran == "Yes":
            self.BankingPrompt()
            if self.nxttran == "No":
                print("Good-bye!")
            else:
                break
    
    def BankingCalc(self):
        endBalance = self.deposit - self.withdrawal
        print(f"{self.name}, you have ${endBalance} in your account!")

bnk = BankingApp()
bnk.BankBegin()