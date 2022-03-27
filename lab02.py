from enum import Enum

class FoodCategory(Enum):
  VEGETABLE = 1
  FRUIT = 2
  GRAIN = 3
  PROTEIN = 4
  DAIRY = 5
  OIL = 6
  OTHER = 7

class FoodItem:
  def __init__(self, name, category, cal):
    self.nme = name
    self.ctgry = FoodCategory(category)
    self.calories = int(cal)

  def name(self):
    return self.nme

  def category(self):
    return self.ctgry

  def calories_per_100g(self):
    return self.calories

  def __str__(self):
    return f"{self.nme} ({self.ctgry}) {self.calories}cal/100g"

class FoodServing:
  def __init__(self, food, amount):
    self.item = food
    self.grams = amount

  def food(self):
    return self.item

  def amount(self):
    return self.grams

  def calories(self):
    return int(self.grams * (self.item).calories_per_100g() / 100)

  def __str__(self):
    return f"{self.grams}g of {self.item}"

class Meal:
  def __init__(self):
    self.foods = []

  def addFood(self, food):
    self.foods.append(food)

  def calories(self):
    total_cal = 0
    for food in self.foods:
      total_cal = total_cal + food.calories()
    return total_cal

  def __str__(self):
    ret_str = ""
    for food in self.foods:
      ret_str = ret_str + food.__str__() + "\n"
    if len(self.foods) > 0:
      ret_str = ret_str[0:len(ret_str) - 1]
    return ret_str