#Randolph Paul 3/19/2024 randolphPaul_lab01
#The purpose of this program is to calculate the amount of ingredients needed to make sugar, butter, and flour cookies based on the number of cookies specified by the user.

#Constants for the recipe
sugarPerCookies = 2.5
butterPerCookies = 1.75
flourPerCookies = 3.75
cookiesPerRecipe = 63

#Get the user's input on the number of cookies needed
print("This program calculates the amount of ingredients needed to make the number of cookies you want.")
cookiesNeeded = int(input("Please enter the number of cookies you want to make: "))

#Calculate the amount of ingredients needed
sugarNeeded = (cookiesNeeded / cookiesPerRecipe) * sugarPerCookies
butterNeeded = (cookiesNeeded / cookiesPerRecipe) * butterPerCookies
flourNeeded = (cookiesNeeded / cookiesPerRecipe) * flourPerCookies


#Display the amount of ingredients needed
print(f"For {cookiesNeeded:,} cookies, you will need:")
print(f"{sugarNeeded:,.2f} cups of sugar")
print(f"{butterNeeded:,.2f} cups of butter")
print(f"{flourNeeded:,.2f} cups of flour")