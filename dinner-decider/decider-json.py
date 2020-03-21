#Add New Food To Data File
def addFood():
    print('Enter name of new food:')
    newName = input()
    print('Enter phase:')
    newPhase = input()
    int(newPhase)
    print('Enter type of meal:')
    newMeal = input()

    newFood = {
        "name": newName,
        "phase": newPhase,
        "meal": newMeal,
    }
    return newFood

def encodeFood(newFood):
    import json    
    with open('foodList.json','a+') as f:
        json.dump(newFood, f, indent=2, separators=(',', ': '))


#Tell What Food To Eat Based on Time of Day
def getTime():
    from datetime import datetime
    from datetime import date

    today = date.today()
    today = today.strftime('%w') 
    today = int(today) # Monday = 1, Sunday = 7

    now = datetime.now()
    now = now.strftime('%H')
    now = int(now)

    return today, now

def getFood(today, now):
    import json
    with open('foodList.json','r') as f:
        foods = json.load(f)
    
    for i in foods:
        print(i)
        print(foods[i])
    
    if foods['phase'] == 1:
        print('Phase 1')


    '''
    if today <=5: #Weekday
        if now <= 10:
            print('It is the morning!')
        elif now <= 16:
            print('It is the afternoon!')
        else:
            print('It is nightime!')
    else: #Weekend
        if now <= 10:
            print('It is the morning!')
        elif now <= 16:
            print('It is the afternoon!')
        else:
            print('It is nightime!')'''


#Command Listener
while True:
    c = input()
    if 'Add Food' in c: 
        newFood = addFood()
        encodeFood(newFood)
    if 'What Now?' in c:
        today, now = getTime()
        getFood(today, now)
    if 'Stop' in c: 
        break


'''
The final product: enter a command add new food, what should I eat right now, or inspire me 
and you get the right response
also delete new food?

'''
