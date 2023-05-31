class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def get_withdrawals(self):
        withdrawals = 0
        for item in self.ledger:
            if item["amount"] < 0:
                withdrawals += item["amount"]
        return abs(withdrawals)

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            items += f"{item['description'][:23]:23}{item['amount']:7.2f}\n"
            total += item["amount"]
        output = title + items + f"Total: {total:.2f}"
        return output


def create_spend_chart(categories):
    total_withdrawals = sum(category.get_withdrawals() for category in categories)
    category_percentages = [(category.name, category.get_withdrawals() / total_withdrawals * 100) for category in categories]

    chart = "Percentage spent by category\n"
    for i in range(100, -10, -10):
        chart += f"{i:3}| "
        for name, percentage in category_percentages:
            bar = "o" if percentage >= i else " "
            chart += f" {bar} "
        chart += "\n"
    
    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"
    
    max_name_length = max(len(category.name) for category in categories)
    for i in range(max_name_length):
        chart += "     "
        for name, _ in category_percentages:
            if i < len(name):
                chart += f" {name[i]} "
            else:
                chart += "   "
        chart += "\n"
    
    return chart


# Example usage
food_category = Category("Food")
clothing_category = Category("Clothing")
entertainment_category = Category("Entertainment")

food_category.deposit(1000, "Initial deposit")
food_category.withdraw(50, "Groceries")
food_category.withdraw(30, "Restaurant")

clothing_category.deposit(500, "Initial deposit")
clothing_category.withdraw(100, "Shoes")
clothing_category.withdraw(75, "T-shirt")

entertainment_category.deposit(800, "Initial deposit")
entertainment_category.withdraw(200, "Concert tickets")
entertainment_category.withdraw(100, "Movie night")

categories = [food_category, clothing_category, entertainment_category]
chart = create_spend_chart(categories)

print(food_category)
print(clothing_category)
print(entertainment_category)
print(chart)
