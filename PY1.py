print(" Mahir Lokare")
def future_value(principal, rate, years):
        	return principal * (1 + rate / 100) ** years
p = float(input("Enter principal amount: "))
r = float(input("Enter annual interest rate (in %): "))
n = int(input("Enter number of years: "))
print("Future Value:", round(future_value(p, r, n), 2))
print("---Execution is Done---")