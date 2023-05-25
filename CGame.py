#audio version
import simpleaudio as sa
import pygame
import random

class Game:
    def __init__(self) -> None:
        self.StartGame()
    def StartGame(self):
        numbers = self.GetRandomNumbers(5)
        for number in numbers:
            self.Play(number)
        answer = self.GenerateQuestion(numbers)
        pygame.time.wait(int(4 * 1000))
        
        self.Play(answer)
        from Claser import ColorTracking

       
            
        
    def GetRandomNumbers(self,length):
        nums = []
        choices = [1,2,3,4,5,6,7,8,9,10]
        for i in range (0,length):
            nums.append(random.choice(choices))
        
        return nums
    def GenerateQuestion(self,numbers_in_question):
        choices = [1,2,3,4,5,6,7,8,9,10]
        wrong_choices = []
        for i in choices:
            if i not in numbers_in_question:
                wrong_choices.append(i)
        right_choice = random.choice(numbers_in_question)
        wrong_choice = random.choice(wrong_choices)
        
        
        yes_no = [0,1]
        pick = random.choice(yes_no)
        print (pick)
        if pick == 0:
            return wrong_choice
        else:
            return right_choice
  
    def Play(self,number):
        
        # Specify the path to your WAV file
        
        audio_file = "audio_assets\\" + str(number)+".mp3"
        print(audio_file)
        pygame.mixer.init()
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()
        pygame.time.wait(int(2 * 1000))


                    
        
def main():
    game = Game()
    
    
main()