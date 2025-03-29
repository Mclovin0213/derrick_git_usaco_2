max_weight = 9

candies = [
    {"name": "Chocolate", "sweetness": 30, "weight": 6},
    {"name": "Gummies", "sweetness": 24, "weight": 4},
    {"name": "Lollipops", "sweetness": 15, "weight": 3},
    {"name": "Caramel", "sweetness": 20, "weight": 5},
    {"name": "Marshmallows", "sweetness": 18, "weight": 2},
    {"name": "Toffee", "sweetness": 25, "weight": 5},
    {"name": "Jelly Beans", "sweetness": 22, "weight": 3},
    {"name": "Hard Candy", "sweetness": 10, "weight": 1},
]

def greedy_algorithm(candies, max_weight):
    # Sort candies by sweetness-to-weight ratio in descending order
    sorted_candies = sorted(candies, key=lambda x: x["sweetness"] / x["weight"], reverse=True)
    
    total_weight = 0
    total_sweetness = 0
    selected_candies = []

    for candy in sorted_candies:
        if total_weight + candy["weight"] <= max_weight:
            selected_candies.append(candy)
            total_weight += candy["weight"]
            total_sweetness += candy["sweetness"]

    return selected_candies, total_sweetness

print(greedy_algorithm(candies, max_weight))