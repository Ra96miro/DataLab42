# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    print_sum.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gramiro- <gramiro-@student.42roma.it>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/17 15:13:47 by gramiro-          #+#    #+#              #
#    Updated: 2022/05/17 16:12:00 by gramiro-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

i = len(sys.argv)
if (i > 3):
	print("Too agruments!")
if (i < 3):
	print("Few arguments!")
	exit()
x = (sys.argv[1])
y = (sys.argv[2])
if (i == 3):
	try:
		print(int (x)  + int (y))
	except ValueError:
		print("Input must be int!")