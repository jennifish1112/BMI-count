height = input('Please enter your height (cm):')
weight = input('Please enter your weight (kg):')
BMI = float(weight) / (float(height) / 100)**2
print('Your BMI is: ', BMI)
if(BMI < 18.5):
	print('underweight')
elif(18.6 <= BMI and BMI < 24.9):
	print('normal weight')
elif(25 <= BMI and BMI < 29.9):
	print('overweight')
elif(BMI > 30):
	print('obesity')