#Given an array of dictionaries, find the median rating and return the id

#Expected: 5.0
businesses_odd = [

{'id': 101, 'rating' : 5.0},
{'id': 102, 'rating' : 2.0},
{'id': 103, 'rating' : 5.0},
{'id': 104, 'rating' : 1.0},
{'id': 105, 'rating' : 5.0}

]
#Expected: 4.0
businesses_even = [

{'id': 101, 'rating' : 5.0},
{'id': 102, 'rating' : 2.0},
{'id': 103, 'rating' : 5.0},
{'id': 104, 'rating' : 1.0},
{'id': 105, 'rating' : 5.0},
{'id': 106, 'rating' : 3.0}

]

#Expected: None
businesses_zero = []

#Expected: 5.0
businesses_one = [
{'id': 101, 'rating' : 5.0}
]

#Expected: 3.5
businesses_two = [
{'id': 101, 'rating' : 5.0},
{'id': 102, 'rating' : 2.0},
]

def medianRating(dictBusinesses):
	seenValuesArray = []
	for business in dictBusinesses: #Theta(N)
		seenValuesArray.append(business['rating'])
	seenValuesArray.sort() #Theta(NlogN)
	length = len(seenValuesArray)
	if length == 0:
		return None
	if length % 2 == 0:
		return averageRating(seenValuesArray[length//2], seenValuesArray[length//2-1])
	else:
		return seenValuesArray[length//2]

def averageRating(num1, num2):
	return (num1 + num2) / 2.0
#Overall runtime Theta(NlogN)
