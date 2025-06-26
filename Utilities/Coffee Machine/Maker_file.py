from Menu_file import Menu
class Maker:
    total_resources = {
        
        "milk": 500,
        "water": 500,
        "coffee": 100,
    }
    
    
    def cost_of_item(self,choice):
        return menu.menu_item[choice]["cost"]
    
    def is_resource_sufficent(self,choice):
        wanna_know = True
        for i in self.total_resources:
            # print(self.total_resources[i])    
            # print(Menu.menu_item[choice][i])
            
            if self.total_resources[i] > menu.menu_item[choice][i]:
                continue
            else:
                print(f"Sorry we don't have enough {i}")
                wanna_know = False
        return wanna_know
    
    def report(self):
        for i in self.total_resources:
            value = self.total_resources[i]
            print(f"{i} : {value}")
    
    def make_coffee(self,choice):
        for i in self.total_resources:
            # print(f"Total : {self.total_resources[i]} - {Menu.menu_item[choice][i]}")
            new_value = self.total_resources[i] - menu.menu_item[choice][i]
            self.total_resources[i] = new_value
        
                
menu = Menu()