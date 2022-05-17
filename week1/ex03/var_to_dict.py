# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    var_to_dict.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gramiro- <gramiro-@student.42roma.it>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/17 16:57:09 by gramiro-          #+#    #+#              #
#    Updated: 2022/05/17 17:39:22 by gramiro-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def convert():
	d = [
	('Hendrix' , '1942'),
	('Allman' , '1946'),
	('King' , '1925'),
	('Clapton' , '1945'),
	('Johnson' , '1911'),
	('Berry' , '1926'),
	('Vaughan' , '1954'),
	('Cooder' , '1947'),
	('Page' , '1944'),
	('Richards' , '1943'),
	('Hammett' , '1962'),
	('Cobain' , '1967'),
	('Garcia' , '1942'),
	('Beck' , '1944'),
	('Santana' , '1947'),
	('Ramone' , '1948'),
	('White' , '1975'),
	('Frusciante', '1970'),
	('Thompson' , '1949'),
	('Burton' , '1939')
	]
 
	for el in d:
		print (el[1] + " : " + el[0])
convert()
		