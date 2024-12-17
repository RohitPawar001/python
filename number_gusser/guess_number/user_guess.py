from guess_number.random_number import returnNumber
from guess_number import score

class GuessNumber:
    print("hi")
    
    def guess(self):
        name = input("Enter your name: ")
        random_number = returnNumber()
        
        i = 0
        while i < 10:
            self.number = int(input("Enter a number between 1 and 10: "))
            
            if random_number == self.number:
                print("You guessed it correctly!")
                score.UserScore.addScore(name, 1)
                break
            elif self.number < random_number:
                print("You have guessed a smaller number.")
            elif self.number > random_number:
                print("You have guessed a larger number.")
            i += 1
            
        print(f"Your final score is: {score.UserScore.finalScore(name)}")
