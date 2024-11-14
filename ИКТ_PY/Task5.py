from itertools import product

# Provided lists of products
bread_types = ["white", "whole grain", "rye"]
meat_types = ["chicken", "beef", "turkey"]
vegetables = ["lettuce", "tomato", "cucumber"]
sauces = ["mayo", "mustard", "ketchup"]

# Generate and print all possible combinations
print("All possible sandwich combinations:")
for combo in product(bread_types, meat_types, vegetables, sauces):
    print(f"Bread: {combo[0]}, Meat: {combo[1]}, Vegetable: {combo[2]}, Sauce: {combo[3]}")