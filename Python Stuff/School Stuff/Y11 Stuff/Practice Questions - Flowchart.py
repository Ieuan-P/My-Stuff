# Develop an algorithm using python that allows a taxi company to calculate how much a taxi fare should be.

# The algorithm should:
# - Promt the user to enter the journey distance in kilometres:
#    - The distance entered must be greater than zero
#    - the user should be made to re-enter the distance until the distance entered is valid
# - Prompt the user to enter the number of passengers (no validation is required)
# - Calculate the taxi fare by:
#    - Charging £2 for ever passenger regardless of the distance
#    - Charging a further £1.50 for every kilometre regardless of how many passengers there are
# - Outpit the final taxi fare.

def calculate_fare():
    distance = 0
    while distance <= 0:
        distance = float(input("Enter the journey distance in kilometres: "))
    
    passengers = int(input("Enter the number of passengers: "))
    
    fare = (passengers * 2) + (distance * 1.5)
    
    print(f"The final taxi fare is: £{fare:.2f}")

calculate_fare()