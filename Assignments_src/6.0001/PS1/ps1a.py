# |\     /|     @author: umgbhalla
# | )   ( |     date: 13 Aug 2021
# | |   | |     course: MIT OCW 6.0001
# | |   | |
# | |   | |
# | (___) |
# (_______)

def main():
    annual_salary = int(input("Enter your annual salary:   "))
    portion_saved = float(input("Enter percent of your salary to save, as decimal:   "))
    total_cost = int(input("Enter cost of your dream home:   "))
    portion_down_payment = 0.25 * total_cost
    current_savings = 0
    number_of_months = 0

    while current_savings < portion_down_payment:
        current_savings += portion_saved * annual_salary / 12 + current_savings * 0.04 / 12
        number_of_months += 1

    print("Number of months:  " , number_of_months)

if __name__ == "__main__":
    main()
