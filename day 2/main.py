print("Welcome to tip calculator !!")
t_bill =float(input("Enter the total bill ? "))
tip_perc = int(input("Enter the percentage of tip you want to give?10,12 or 15 ? "))
n_per = int(input("Enter the number of persons ? "))

perc = tip_perc/100
tip = t_bill*perc
total = t_bill+tip
b_per = round((total/float(n_per)),2)
print("Each person should pay ? ",b_per)