import pyttsx3
import speech_recognition as sr
import random
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# engine.setProperty('voice',voices[1].id)
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
speak("hii guys lets play the snake water gun game ")
def play_game():
    choices=['snake','gun','water']
    speak(f"choose the options {choices}")
    player_choice=input(f"enter your choice {choices}  ").lower()
    computer_choices=random.choice(choices)
    if player_choice not in choices:
        speak(f"plese choose the correcr option as {choices}")
        print(f"plese choose the correcr option as {choices}")
        return
    print(f"the player choice is {player_choice}")
    speak(f"the player choice is {player_choice}")
    print(f"the computer choice is {computer_choices}")
    speak(f"the computer choice is {computer_choices}")
    if player_choice==computer_choices:
        print("ohhh! it's a tied")
        speak("ohhh! it's a tied")
    elif (player_choice == "snake" and computer_choices == "water") or (
            player_choice == "water" and computer_choices == "gun") or (
            player_choice == "gun" and computer_choices == "snake"):
        print("You win!")
        speak("you win")
    else:
        print("computer win")
        speak("computer win ")
# if __name__ == "__main__":
#     while True:
#         play_game()
#         play_again=print("do you want to play again"),speak("do you want to play again ")
#         if play_again!="yes":
#             break
if __name__ == "__main__":
    while True:
      play_game()
      speak("do you want to play again")
      play_again=input("Do you want to play again:")
      if play_again!="yes":
         break