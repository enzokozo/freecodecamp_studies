class Category:
    
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        dictionary = {'amount' : amount, 'description' : description}
        self.ledger.append(dictionary)
    
    def withdraw(self, amount, description="") -> bool:
        if self.check_funds(amount):
            dictionary = {'amount' : -amount, 'description' : description}
            self.ledger.append(dictionary)
            return True 
        return False
    
    def get_balance(self):
        return sum([x['amount'] for x in self.ledger])
    
    def transfer(self, amount, category) -> bool:
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False
    
    def check_funds(self, amount) -> bool:
        return self.get_balance() >= amount
    
    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            amount = f"{item['amount']:.2f}"
            description = item['description'][:23]
            items += f"{description:<23}{amount:>7}\n"
            total = f"Total: {self.get_balance():.2f}"
        return title + items + total

def create_spend_chart(categories):
    title = "Percentage spent by category\n"
    spent_amounts = [sum(-item['amount'] for item in category.ledger if item['amount'] < 0) for category in categories]
    total_spent = sum(spent_amounts)
    percentages = [int((amount / total_spent) * 100) // 10 * 10 for amount in spent_amounts]

    chart = ""
    for i in range(100, -1, -10):
        chart += f"{i:>3}|"
        for percentage in percentages:
            chart += " o " if percentage >= i else "   "
        chart += " \n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_length = max(len(category.name) for category in categories)
    for i in range(max_length):
        chart += "     "
        for category in categories:
            chart += f"{category.name[i]}  " if i < len(category.name) else "   "
        chart += "\n"

    return title + chart.rstrip("\n")

def main():
    food = Category('Food')
    food.deposit(1000, 'initial deposit')
    food.withdraw(10.15, 'groceries')
    food.withdraw(15.89, 'restaurant and more food for dessert')
    clothing = Category('Clothing')
    food.transfer(50, clothing)
    print(food)
    print(create_spend_chart([food, clothing]))

if __name__ == "__main__":
    main()