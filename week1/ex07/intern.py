# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    intern.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gramiro- <gramiro-@student.42roma.it>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/19 15:25:09 by gramiro-          #+#    #+#              #
#    Updated: 2022/05/22 20:38:03 by gramiro-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Intern:
	def __init__(self, name = "My name? I’m nobody, an intern, I have no name."):
			self.name = name

	def __str__(self):
		return self.name

	class Coffe:
		def __str__(self):
			return "This is the worst coffee you ever tasted."

	def work(self):
		raise Exception("I'm just an intern, I can't do that...")

	def	make_coffee(self):
		return self.Coffe()
