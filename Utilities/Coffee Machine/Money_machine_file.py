from Menu_file import Menu


class MoneyMachine:
    Total_money = 0
    
    def make_payment(self,cost):
        Money_received = float(input("Enter your amount in $:   "))
        if Money_received < cost:
            print("Insufficent Amount (Money Refunded)")
            return False
        else:
            self.Total_money += cost
            money_to_refund =  Money_received - cost
            if money_to_refund > 0:
                print(f"The Amount Refunded is {money_to_refund}")
                
            return True
    
    def total_money(self):
        
        print(f"Money : {self.Total_money}")
        

    
            