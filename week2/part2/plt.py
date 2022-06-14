# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    plt.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gramiro- <gramiro-@student.42roma.it>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/23 16:24:01 by gramiro-          #+#    #+#              #
#    Updated: 2022/06/14 17:54:26 by gramiro-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import matplotlib.pyplot as plt
import urllib.request
from PIL import Image

array = np.random.randint(10, size=(20))

array_one = np.arange(12)
array_one = np.reshape(array_one, (-1, 4))

# def	create_incremental_array():
def incremental_array(n):
  ar4 = np.linspace(0, 1, n).reshape(1, n)
  return ar4
# print(incremental_array(10))

# array_ten = np.zeros((10, 12))
array_ten = np.arange(120)
array_ten = np.reshape(array_ten, (-1, 12))
columns = array_ten[0:4, :]
row = array_ten[: , 7:12]


# print (array_one)
# print (array_ten)
# print (columns)
# print (row)

# matr3 = np.full((3, 3), incremental_array(3))
# plt.imshow(matr3)
# urllib.request.urlretrieve(
#   'https://media-exp1.licdn.com/dms/image/C4E03AQE3ziXsx7XLXw/profile-displayphoto-shrink_200_200/0/1618747198897?e=1657152000&v=beta&t=ic5ILC3tyvCgaPAPfOrGavQ8Za1Vxg9SIeUg4ZM3p48', "img.png")
# img = np.asarray(Image.open("img.png"))
# img2 = img.reshape((img.shape[0] * img.shape[1], 3))
# img2 = np.matmul(img, matr3)
# img = img2.reshape(img.shape).astype(img.dtype)
# print(plt.imshow(img))

matr3 = np.full((3, 3), incremental_array(3))
plt.imshow(matr3)
urllib.request.urlretrieve('https://media-exp1.licdn.com/dms/image/C4E03AQE3ziXsx7XLXw/profile-displayphoto-shrink_200_200/0/1618747198897?e=1657152000&v=beta&t=ic5ILC3tyvCgaPAPfOrGavQ8Za1Vxg9SIeUg4ZM3p48', "img.png")
img = np.asarray(Image.open("img.png"))
img2 = img.reshape((img.shape[0] * img.shape[1], 3))
img2 = np.matmul(img, matr3)
img = img2.reshape(img.shape).astype(img.dtype)
print(plt.imshow(img))