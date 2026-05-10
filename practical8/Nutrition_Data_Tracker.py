class food_item:
    def __init__(self, name, calories, carbohydrates, protein, fat):
        self.name = name
        self.calories = calories
        self.carbohydrates = carbohydrates
        self.protein = protein
        self.fat = fat

    def __str__(self):
        return f"{self.name}: {self.calories} calories, {self.carbohydrates}g carbs, {self.protein}g protein, {self.fat}g fat"
    
def calculate_daily_nutrition(food_items):
    total_calories = sum(item.calories for item in food_items)
    total_carbohydrates = sum(item.carbohydrates for item in food_items)
    total_protein = sum(item.protein for item in food_items)
    total_fat = sum(item.fat for item in food_items)
    if total_calories > 2500:
        print("Warning: Total calorie intake exceeds the recommended daily limit of 2500 calories.")
    if total_fat > 90:
        print("Warning: Total fat intake exceeds the recommended daily limit of 90 grams.")
    print(f"Total calories consumed: {total_calories} calories")
    print(f"Total carbohydrates consumed: {total_carbohydrates} grams")
    print(f"Total protein consumed: {total_protein} grams")
    print(f"Total fat consumed: {total_fat} grams")
    return total_calories, total_carbohydrates, total_protein, total_fat

apple = food_item("Apple", 60, 15, 0.3, 0.5)
banana = food_item("Banana", 105, 27, 1.3, 0.3)
chicken_breast = food_item("Chicken Breast", 165, 0, 31, 3.6)
salmon = food_item("Salmon", 206, 0, 22, 12)

# input food eaten within the day(example)
food_items = [apple, banana, chicken_breast, salmon,salmon,salmon, salmon, salmon, salmon, salmon, salmon, salmon, salmon, salmon, salmon, salmon, salmon, salmon, salmon, salmon]
calculate_daily_nutrition(food_items)

# Allow user input for food items
food_consumption=input("Enter the food items consumed today (comma separated): ")
food_items = []
for food in food_consumption.split(","):
    food = food.strip().lower()
    if food == "apple":
        food_items.append(apple)
    elif food == "banana":
        food_items.append(banana)
    elif food == "chicken breast":
        food_items.append(chicken_breast)
    elif food == "salmon":
        food_items.append(salmon)
    else:
        print(f"Warning: Food item '{food}' not recognized. Skipping.")
calculate_daily_nutrition(food_items)

   



 