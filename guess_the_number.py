"""
1. O'yin tugagandan keyin "Yana o'ynaysizmi?" deb so'ralsin. 
User  klaviatura orqali "Yes" yoki "No" deb kiritishiga qarab o'yin davom ettirilsin yoki to'xtatilsin. 
2. Userga maximum 5 martagacha sonlarni guess qilishga imkon berilsin. 
Agar 5 martada topa olmasa "Siz yutqazdingiz!"  degan xabar chiqsin. 

User yutsa ham yutqazsa ham "Yana o'ynaysizmi?" deb so'ralishi kerak.
Agar 5 martada topa olmasa "Siz yutqazdingiz deb to'g'ri javobni chiqarsin.

"""
from random import randint
control = True
main = True
attempt = 5


while control == True:
        answer = randint(1, 100)
        print("You have 5 attempts to win!")
        while main == True:
            number = int(input("Okay, guess the number:>>> "))
            if number == answer:
                print("\nCongrats. You win!")
                main = False
                control = False
                
            if number < answer:
                attempt -= 1
                print("\nToo small")
                main = True
            
            if number > answer:
                attempt -= 1
                print("\nToo high!")
                main = True
            
            if attempt == 0:
                print("\nYou lose!")
                print(f"\nCorrect answer is {answer}")
                main = False   
        
        again = input("\nWould you like to play again?('yes' to play or 'no' to exit):")
        if again != "yes":
            break
        
        print("Thank you!")
       

       
