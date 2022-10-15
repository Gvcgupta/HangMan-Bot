from english_words import english_words_lower_alpha_set
import random

class Hangman:
    graphics = ['''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''', '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''']

    def __init__(self):
        self.word=random.choice(list(english_words_lower_alpha_set))
        self.word=list(self.word)
        self.sol=["_" for i in range(len(self.word))]
        self.finished=False

        self.wrongs=6


    def check(self,sol):
        if "_" not in self.sol:
            self.finished=True
        return self.finished

    def ask(self,sol,word):
        a=input("Enter your letter:")
        ch = False

        for i in range(len(word)):
            if self.word[i]==a:
                ch=True
                self.sol[i]=a
        if ch==False:
            print("Wrong guess!")
            print(self.graphics[self.wrongs])
            self.wrongs-=1

    

    def display(self,sol):
        for i in range(len(self.sol)):
            print(self.sol[i],end="")
        print()

    def rightAnswer(self,word):
        for i in range(len(self.word)):
            print(self.word[i],end="")
        print()

