# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    beverages.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gramiro- <gramiro-@student.42roma.it>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/22 16:21:10 by gramiro-          #+#    #+#              #
#    Updated: 2022/05/22 20:39:50 by gramiro-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class HotBeverage:
    def __init__(self, price = "0.30", name = "hot beverage"):
        self.price = price
        self.name = name
    def description(self, desc = "Just some hot water in a cup"):
        self.desc = desc
        return desc
    def __str__(self):
        return (
            "name : " + self.name + "\n" +
            "price : " + self.price + "\n"
            "description : " + self.description())

class Coffee(HotBeverage):
    def __init__(self):
        super().__init__("0.40", "coffee")
    def description(self):
        return super().description("A coffee, to stay awake.")

class Tea(HotBeverage):
    def __init__(self):
        super().__init__("0.30", "tea")
    def description(self):
        return super().description()

class Chocolate(HotBeverage):
    def __init__(self):
        super().__init__("0.50", "chocolate")
    def description(self):
        return super().description("Chocolate, sweet chocolate...")

class Cappuccino(HotBeverage):
    def __init__(self):
        super().__init__("0.45", "cappuccino")
    def description(self):
        return super().description("Un po' di Italia nella sua tazza!")