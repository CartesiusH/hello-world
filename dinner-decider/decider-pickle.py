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

#Saving information
def saveFoodList():
    import pickle
    with open('foodList.pickle','wb') as f:
        for i in foodList:
            pickle.dump(foodList[i],f)

#Loading information
def loadFoodList():
    import pickle
    with open('foodList.pickle','rb') as f2:
        pickle.load(f2)


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
while True:
    c = input()
    if 'Add Food' in c: 
        loadFoodList()
        addFood()
        saveFoodList()
    if 'Stop' in c: 
        break





'''
The final product: enter a command add new food, what should I eat right now, or inspire me 
and you get the right response
also delete new food?

To-do:
+ make this work for mutiple items
- auto-loads at beginning, auto-saves at the end
- fetch for certain day


Basic Program Idea:
- list of food with phase and meal attributes
- print meals of correct attribute

#Old Write Attempt
with open('foodList.txt','w') as f:
    for i in range(len(foodList)):
        f.write(foodList[i].name)
        f.write(foodList[i].phase)
        f.write(foodList[i].meal)
       

#Weekday If Statements
if (today >=1) and (today <= 5):
    stage = 'weekday'
else:
    stage = 'weekend'



#How to store data in python:

As Unstructured Data:
plain text files (read only)
plain text files (RegEx)
2plain text files (Numpy)

As Structured Data:
pickle
    turn the whole thing into bytes and back
JSON
    save each instances and then recreate stucture

I love how code is color coded. Me encanta.
'''