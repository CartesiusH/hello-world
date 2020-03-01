#Adding New Foods To List with Phase and Type of Meal Attributes
foodList = []
class food:
    def __init__(self, name, phase, meal):
        self.name = name
        self.phase = phase
        self.meal = meal
def addFood():
    print('Enter a new food:')
    newName = input()
    print('Enter phase:')
    newPhase = input()
    int(newPhase)
    print('Enter type of meal:')
    newMeal = input()

    newFood = food(newName,newPhase,newMeal)
    foodList.append(newFood)

#Store foodList with JSON
import json
def encode_food(myFood):
    if isinstance(myFood, food):
        return(myFood.name, myFood.phase, myFood.meal)
    else:
        raise TypeError (f'Object is not JSON serializable')

def saveFoodList():
    for i in range(len(foodList)):
        encode_food(foodList[i])
        with open('foodList.json','a') as f:
            f.write(json.dumps(foodList[i], default=encode_food)) 
            f.write('\n')

#Command Listener
while True:
    c = input()
    if 'Add Food' in c: 
        addFood()
    if 'Commit Food' in c:
        saveFoodList()
    if 'Stop' in c: 
        break


'''
#Getting Date (Week) & Time (Hours) as Integers
from datetime import datetime
from datetime import date

today = date.today()
today = today.strftime('%w')
today = int(today)

now = datetime.now()
now = now.strftime('%H')
now = int(now)

#Command Listener



The final product: enter a command add new food, what should I eat right now, or inspire me 
and you get the right response
also delete new food?

'''
