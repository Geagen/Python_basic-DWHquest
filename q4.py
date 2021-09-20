dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4, 'five': 5}


D_max = {}


for key_d in dict:
        val = dict[key_d]
        if val >= 3 :
                D_max[key_d]= val


print (D_max)
