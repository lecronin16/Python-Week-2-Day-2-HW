from IPython.display import clear_output
shopping_list = []
# Ask the user four bits of input: Do you want to : Show/Add/Delete or Quit?

def askShopper():
    answer = input("What would you like to do? (Show/Add/Delete or Quit?)")
    return answer.lower()
def goShopping():
    while True:
        ans = askShopper()
        if ans == "quit":
            print("Thanks for shopping, come again soon!")
            break
        elif ans == "add":
            new=input("What would you like to add? ")
            shopping_list.append(new)
        elif ans == "delete":
            old = input("What would you like to delete? ")
            shopping_list.pop()
        elif ans == "show":
            print(shopping_list)
        else:
            print("Invalid response, please try again!")

goShopping()  