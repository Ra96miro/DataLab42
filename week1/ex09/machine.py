# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    machine.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gramiro- <gramiro-@student.42roma.it>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/22 16:22:16 by gramiro-          #+#    #+#              #
#    Updated: 2022/05/22 20:39:54 by gramiro-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import beverages
import random

class CoffeeMachine:
	broken = True
	n_serving = 0
	def __init__(self):
		pass

	class EmptyCup(beverages.HotBeverage):
		name = "empty cup"
		price = "0.90"
		def description(self):
			return "An empty cup?! Gimme my money back!"

	class BrokenMachineException(Exception):
		def __init__(self):
			super().__init__("This coffee machine has to be repaired.")

	def repair(self):
		self.broken = False
		self.n_serving = 0
		return "Repairing Coffee Machine.."
	def serve(self, hot_beverage: beverages.HotBeverage):
		empty = self.EmptyCup()
		if self.n_serving >= 10:
			raise self.BrokenMachineException()
		self.n_serving += 1
		if random.randint(0, 1) % 2 == 0:
			return hot_beverage
		else:
			return empty

cm = CoffeeMachine()

hot_beverage = beverages.HotBeverage()
coffee = beverages.Coffee()
tea = beverages.Tea()
chocolate = beverages.Chocolate()
capuccino = beverages.Cappuccino()

print(cm.serve(hot_beverage))
print(cm.serve(hot_beverage))
print(cm.serve(hot_beverage))
print(cm.serve(coffee))
print(cm.serve(coffee))
print(cm.serve(tea))
print(cm.serve(tea))
print(cm.serve(chocolate))
print(cm.serve(chocolate))
print(cm.serve(capuccino))

try:
	print(cm.serve(capuccino))
except Exception as e:
	print(e)

print(cm.repair())
print(cm.serve(hot_beverage))
print(cm.serve(hot_beverage))
print(cm.serve(hot_beverage))
print(cm.serve(coffee))
print(cm.serve(coffee))
print(cm.serve(tea))
print(cm.serve(tea))
print(cm.serve(chocolate))
print(cm.serve(chocolate))
print(cm.serve(capuccino))