
def lr2xy(l):
	if (len(l)%2 == 0):
		m = len(l) - 2
	else :
		m = len(l) - 3

	new = []
	for i in (0,2,m):	
		left = l[i]
		right = l[i+1]
		x = (left + right)/2
		y = left - right
		new.append([x,y])

	return new 

def apply_linear_prediction(l):
	new = []
	for i in range(len(l)):
		if (i == 0 or i == 1):
			new.append(l[i])
		else:
			#####################################
			predicted_x = 2*l[i-1][0] - l[i-2][0]
			predicted_y = 2*l[i-1][1] - l[i-2][1]
			#####################################
			diff_x = l[i][0] - predicted_x
			diff_y = l[i][1] - predicted_y
			new.append([diff_x,diff_y])
	return new
