# insertion sort
def insertion(given_array):
	for j in range(len(given_array)):
		for i in range(len(given_array)-1):
			if given_array[i+1] < given_array[i]:
				given_array[i+1],given_array[i] = given_array[i],given_array[i+1]

	return given_array

given_array = [5,1,2,6,8,2,0]

print(insertion(given_array))