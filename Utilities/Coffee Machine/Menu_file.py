class Menu:
    
    menu_item = {
        "latte": {
            "milk": 100,
            "water": 20,
            "coffee": 10,
            "cost": 1.5
        },
        "espresso": {
            "water": 30,
            "coffee": 15,
            "cost": 2.5
        },
        "cappuccino": {
            "milk": 80,
            "water": 25,
            "coffee": 12,
            "cost": 3.5
        }
    }
    
    
    
    def get_ingredients(self,choice):
        for ingridient in self.menu_item[choice]:
            value = self.menu_item[choice][ingridient]
            print(f"{ingridient} {value}")
                
    def get_menu_items(self):
            
            return "|".join(self.menu_item.keys())

    

