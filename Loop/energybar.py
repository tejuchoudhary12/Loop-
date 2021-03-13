correct=5
chances=10
while chances>0:
    diffrence=0
    guess=int(input("Enter a number"))
    if guess==correct:
        print("you WIN this game!")
        break
    elif guess>correct:
        diffrence=guess-correct
        chances-=diffrence
        if chances<0:
            print("Chances Finish")
            break
        else:
            print("Remaining chances",chances)
    elif guess<correct:
        diffrence=correct-guess
        chances=chances-diffrence
        if chances<0:
            print("chances finished")
            break
        else:
            print("Remaining chnaces",chances)
else:
    print("Right guess number is finished")

