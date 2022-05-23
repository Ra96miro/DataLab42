# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    plt.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gramiro- <gramiro-@student.42roma.it>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/23 16:24:01 by gramiro-          #+#    #+#              #
#    Updated: 2022/05/23 18:06:42 by gramiro-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import matplotlib.pyplot as plt

array = np.random.randint(10, size=(20))

array_one = np.arange(12)
array_one = np.reshape(array_one, (-1, 4))

# def	create_incremental_array():
	


# array_ten = np.zeros((10, 12))
array_ten = np.arange(120)
array_ten = np.reshape(array_ten, (-1, 12))
columns = array_ten[0:4, :]
row = array_ten[: , 7:12]


print (array_one)
print (array_ten)
print (columns)
print (row)