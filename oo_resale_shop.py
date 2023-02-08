from computer import *

class ResaleShop:

    # Attributes needed in resale shop
    inventory=[]

    # setting up constructor
    def __init__(self,inventory):
        self.inventory=inventory
  

    # Methods

  

    #buying a computer and store computer info into the inventory
    def buy(self,computer):
        self.inventory.append(computer)
        print("Successful purchase")


    #update computer price
    def update_price(self,computer, new_price: int):
        if computer in self.inventory:
            computer.update_price(new_price)
        else:
            print("Item", computer, "not found. Cannot update price.")


    #selling a computer
    def sell(self,computer):
        if computer in self.inventory:
            self.inventory.remove(computer)
            print("Item", computer, "sold!")
        else: 
            print("Item", computer, "not found. Please select another item to sell.")


    #refurbishing a computer
    def refurbish(self,computer, new_os):
        #check if the computer is in the inventory
        if computer in self.inventory:
            if int(computer.year_made) < 2000:
                computer["price"] = 0 # too old to sell, donation only
            
            elif int(computer.year_made) < 2012:
                computer.price = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer.year_made) < 2018:
                computer.price = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer.price = 1000 # recent stuff

            if new_os is not None:
                computer.operating_system = new_os # update details after installing new OS
        
        #if the computer is not in the inventory, error message
        else:
            print("Item", computer, "not found. Please select another item to refurbish.")






