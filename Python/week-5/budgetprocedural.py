# the amount of money we have to spend
funds=2500

# A dictionary of our items we are spanding our items we are spending
budgets = {}

# A dictanary of the expenses of each budged item
expenses = {}



#adds an item to the budgets dictanary
def addBudget(name, amount):
    global funds
    if name in budgets:
        raise ValueError("Budget for item alredy exists")
    if amount > funds:
        raise ValueError("no your to broke")

    budgets[name] = amount 
    funds-=amount 
    expenses[name] = 0
    return funds

def spend(name, amount):
    if name not in expenses:
        raise ValueError("item not in budget")
    expenses[name] += amount 
    budgeted = budgets[name]
    spent = expenses[name]
    return budgeted - spent

def printBudget():
    for name in budgets:
        budgeted = budgets[name]
        spent= expenses[name]
        remaningbudget = budgeted - spent
        print(f'{name:15s}, {budgeted:10.2f}, {spent:10.2f}' 
              f'{remaningbudget:10.2f}')



print("Total funds:",funds)
addBudget("clothes", 200)
addBudget("money", 500)
addBudget(" clothes", 300)

spend("clothes",50)
spend("money", 100)
spend(" clothes", 200)

printBudget()
