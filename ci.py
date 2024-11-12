

def compound_interest(principal, rate, time):

	
	Amount = principal * (pow((1 + rate / 100), time))
	CI = Amount - principal
	print("Compound interest is", CI)

	
rate=float(input("Enter the rate:"))
principal=int(input("Enter the principal :"))
time=int(input("Enter the time :"))
compound_interest(principal,rate,time)

