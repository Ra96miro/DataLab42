# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ipynb.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gramiro- <gramiro-@student.42roma.it>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/23 15:55:52 by gramiro-          #+#    #+#              #
#    Updated: 2022/05/23 18:46:42 by gramiro-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

array_zero = np.zeros(10)
# array_zero.fill(0)

array_ones = np.arange(10)
array_ones.fill(1)

array_to_fifty = np.arange(10, 51)

array_even_to_fifty = np.arange(10, 51, 2)

array_matrix=np.identity(3)

rand_num = np.random.random()

array_to = np.arange(0, 1, 0.1111111111)



print (array_zero)
print (array_ones)
print (array_to_fifty)
print (array_even_to_fifty)
print (array_matrix)
print (rand_num)
print (array_to)