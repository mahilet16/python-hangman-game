import random
import hangmanlist
import hangman_diagram
import hangman_logo
stages=hangman_diagram.stages
print(hangman_logo.logo)
word_list=hangmanlist.word_list

chosen_word=random.choice(word_list)
lives=6
display=[]
for i in range(len(chosen_word)):
    display+="_"
end_of_loop=False
while not end_of_loop:  
    guess=input("Guess a letter:").lower()
    if guess in display:
          print(f"you've already guessed {guess} ")
    for i in range(len(chosen_word)):
        letter=chosen_word[i]
        if letter==guess:
            display[i]=letter
    if guess in chosen_word:
        print(stages[lives])        
    
    if guess not in chosen_word:    
        lives-=1
        print(f"you guessed {guess},that's not in the word.you lose a life.")
        print(stages[lives])
        if lives==0:
            print(f"you lose! the word is {chosen_word}")
            end_of_loop=True 
    print(f"{' '.join(display)}")  #to convert list to string 
           
  
    if "_" not in display:
        end_of_loop=True
        print("you win")
    

