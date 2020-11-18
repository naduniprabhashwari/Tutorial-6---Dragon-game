import random
import time

def check_cave(chosen_cave):
          print('You approach the cave...')
          time.sleep(2)
          print('A large dragon jumps out in front of you! ')
          print('He opens his jaws and...')
          time.sleep(2)

          friendlyCave = random.randint(1, 4)


          one = "Gobbles you down!"
          two = "Burns you down!"
          three = "Freezes you by ice forever!"

          results = [one,two,three]

          if str(friendlyCave) == chosen_cave:
                    print("Gives you his treasure!")
          else:
                    print(random.choice(results))
          
                    
                                      
