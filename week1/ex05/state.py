# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    state.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gramiro- <gramiro-@student.42roma.it>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/17 19:42:59 by gramiro-          #+#    #+#              #
#    Updated: 2022/05/17 19:43:03 by gramiro-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

states = {
"Oregon" : "OR",
"Alabama" : "AL",
"New Jersey": "NJ",
"Colorado" : "CO"
}
capital_cities = {
"OR": "Salem",
"AL": "Montgomery",
"NJ": "Trenton",
"CO": "Denver"
}

def find_city():

		for keys, value in capital_cities.items():
			if (sys.argv[1] == value):
				for x, y in states.items():
					if (keys == states[x]):
						print (x)
						return
			print ("Unknow capital city")
i = len(sys.argv)
if (i == 2):
		find_city()
	
			
	