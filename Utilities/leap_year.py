# Leap Year 

year = int(input("Enter Year: "))

def is_leap_year(year):
    """Here if year/4 = 0 AND if year/100 != 0   OR   If year/4 = 0 AND if year/100 = 0 AND year/400 = 0 """
    if year % 4 == 0:
        if year % 100 != 0:
            return True
        else:
            if year % 400 == 0:
                return True
            else:
                return False
    else:
        return False

result = is_leap_year(year)
if result == True:
    print(f"{year} is a leap year")  
else:
    print(f"{year} is not a leap year")
            