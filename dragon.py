import random
import time
import dragon_multi 

global type_of_game
type_of_game = 0


# selecting the game type
def game_type():
           print("|------|-----------------------------|--------------------------|")
           print("|        |        Game Type          |    No of Dragons     |")
           print("|------|---------------------------- |--------------------------|")
           print("|   1   |             Easy                 |               2                 |")
           print("|   2   |             Hard                |               4                 |")
           print("|------|----------------------------|--------------------------|")
           print()

           global type_of_game
           
           print("Select game type (1/2): ") # user selects the game type
           type_of_game = int(input())

           

           
# display the introduction of the game
def display_intro():
           print("You are in the Kingdom of Dragons. In front of you,")

           # printing the intro according to the game type 
           if type_of_game == 1:
                      print("you see two caves. In one cave, the dragon is friendly")
                      print("and will share his treasure with you. The other dragon\nis hungry and will eat you on sight.")
           else:
                      print("you see 4 caves. In one cave, the dragon is friendly")
                      print("and will share his treasure with you. The other dragons\nare hungry and will eat or freezes or burn you on sight.")
                      
           

# part 4 - player choose the cave
def choose_cave():
           cave = ''          # local variable with empty string

           # getting inputs according to the game type
           if type_of_game == 1:
                      while cave != '1' and cave != '2' :
                                 print('Which cave will you go into? (1 or 2)')
                                 cave = input()
           else:
                     while cave != '1' and cave != '2' and cave != '3' and cave != '4':
                                 print('Which cave will you go into? (1/2/3/4)')
                                 cave = input() 
           return cave


# part 5 -  ckeck the selected cave
def check_cave(chosen_cave):
           print('You approach the cave...')
           time.sleep(2)
           print('A large dragon jumps out in front of you! ')
           print('He opens his jaws and...')
           time.sleep(2)

           friendlyCave = random.randint(1, 2)    # selecting the friendly dragon's cave

           # checking the user selected cave 
           if str(friendlyCave) == chosen_cave:
                      print("Gives you his treasure!")
           else:
                      print("Gobbles you down!")


# main loop           
# play_again = "y"
while True:
           
           game_type()
           display_intro()
           cave_number = choose_cave()

           # checking the cave according to the game type
           if type_of_game == 1: 
                      check_cave(cave_number)
           else:
                      dragon_multi.check_cave(cave_number)
                     
           # asking user to play many more times
           print("Do you want to play again? (y or n)")
           play_again = input().lower()
           if play_again != "y":
                      break
