from hangman import Hangman

hang=Hangman()

while hang.wrongs>=0:

    hang.ask(hang.sol,hang.word)
    hang.display(hang.sol)
    if hang.check(hang.sol)==True:
        hang.wrongs=-1
        print("You guessed the word")
    elif hang.wrongs<0:
        print("Chances are over")
        print("Right answer is",end=" ")
        hang.rightAnswer(hang.word)
