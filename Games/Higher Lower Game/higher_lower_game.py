import random
from instagram_profiles import social_media_profiles

LOGO = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ '/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/        

"""
VS = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)

"""
# --------- Function for finding which one is greater A or B  ----------
def Func_for_greater(A,B):
    
    if A > B:
        return 'a'
    else:
        return 'b'
    
# --------- Function  ----------
def func_for_work():
    rand_1 = random.randint(0,len(social_media_profiles))
    rand_2 = random.randint(0,len(social_media_profiles))
    print(LOGO)
    print("\n---------- Welcome to the Guess Higher Lower Game , Guess who has more followers and win a point ---------\n")
    
    print(f"Person A =   {social_media_profiles[rand_1]["name"] } is  {social_media_profiles[rand_1]["Description"]} and he is from {social_media_profiles[rand_1]["Country"] }")
    print(VS)
    print(f"Person B =   {social_media_profiles[rand_2]["name"] } is  {social_media_profiles[rand_2]["Description"]} and he is from {social_media_profiles[rand_2]["Country"] }")
    
    A = social_media_profiles[rand_1]["Insta_followers_in_millions"]
    B = social_media_profiles[rand_2]["Insta_followers_in_millions"]
    
    greater_one =  Func_for_greater(A,B)
    
    Guess = input("\nSo Person A or B ?   ").lower()
    
    if Guess == greater_one:
        return True
    else:
        return False
    

#------------------------------

Checker = True
Score = 0
while Checker == True:
    Your_answer =  func_for_work()
    
    if Your_answer == True:
        Score += 1
    else:
        print(f"Your Total score is {Score}")
        Checker = False
        
        