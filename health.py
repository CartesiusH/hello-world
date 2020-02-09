#Inspire Me Command



#Adding New Foods To List with Phase and Type of Meal Attributes
foodList = []
class food:
    def setName(self, name):
        self.name = name
    def setPhase(self, phase):
        self.phase = phase
    def setMeal(self, meal):
        self.meal = meal

print('Enter a new food:')
newName = input()
print('Enter phase:')
newPhase = input()
int(newPhase)
print('Enter type of meal:')
newMeal = input()

newFood = food()
newFood.setName(newName)
newFood.setPhase(newPhase)
newFood.setMeal(newMeal)
foodList.append(newFood)



#Storing new food objects in file
import pickle
with open('foodList.pickle','wb') as f:
    pickle.dump(foodList[0].name, f)
    pickle.dump(foodList[0].phase, f)
    pickle.dump(foodList[0].meal, f)
    
    #pickle.dump(food.name(foodList[0]),f)
    #pickle.dump(food('phase'),f)
    #pickle.dump(food('meal'),f)
    #pickle.dump(foodList,f)
    #pickle.dump(food,f)

#Retrieving food objects from file
with open('foodList.pickle','rb') as f2:
    a = pickle.load(f2)
    print()
    print(a.meal)


#Getting Date (Week) & Time (Hours) as Integers
from datetime import datetime
from datetime import date

today = date.today()
today = today.strftime('%w')
today = int(today)

now = datetime.now()
now = now.strftime('%H')
now = int(now)





'''


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