# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    print_secs.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gramiro- <gramiro-@student.42roma.it>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/17 16:12:49 by gramiro-          #+#    #+#              #
#    Updated: 2022/05/17 16:53:04 by gramiro-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

i = len(sys.argv)
if (i < 4):
	print("Few arguments!")
	exit()
if (i > 4):
	print("Too arguments!")
	exit()
x = (sys.argv[1])
y = (sys.argv[2])
z = (sys.argv[3])
try:
	print(int (x) * 3600 + int (y) * 60 + int (z))
except ValueError:
	print("Input must be int!")
	