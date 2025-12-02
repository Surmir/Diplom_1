from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class DataTest:
    
    INGREDIENTS = [(INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
                   (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
                   (INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
                   (INGREDIENT_TYPE_FILLING, "cutlet", 100),
                   (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
                   (INGREDIENT_TYPE_FILLING, "sausage", 300)]
    
    #значения класса Burgers по умолчанию
    BURGER_INIT_BUN = None
    BURGER_INIT_INGREDIENTS = []

    PRICE_PARAM = [[24.5, [], 49.0],
                   [24.5, [50.5], 99.5]]
    
    RECEIPT_PARAM = [("White Bun",
                      [],
                      ["(==== White Bun ====)",
                       "(==== White Bun ====)\n",
                       "Price: 200.0"]),
                     ("Black Bun",
                      [("Cheese", "TOPPING", 50.0)],
                      ["(==== Black Bun ====)",
                       "= topping Cheese =",
                       "(==== Black Bun ====)\n",
                       "Price: 250.0",])]
    
class DataMock:
    
    BUN_NAME = "black bun"
    BUN_PRICE = 100.0

    INGREDIENT_TYPE = INGREDIENT_TYPE_SAUCE
    INGREDIENT_NAME = "hot sauce"
    INGREDIENT_PRICE = 100.0
