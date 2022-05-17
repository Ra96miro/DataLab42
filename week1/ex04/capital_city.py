# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    capital_city.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gramiro- <gramiro-@student.42roma.it>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/17 17:41:53 by gramiro-          #+#    #+#              #
#    Updated: 2022/05/17 19:00:44 by gramiro-         ###   ########.fr        #
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

x = len(sys.argv)
if (x == 2):
	try:
		print (capital_cities[states[sys.argv[1]]])
	except KeyError:
		print ("Unknown state")
else:
	exit()
