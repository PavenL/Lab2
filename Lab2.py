def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")  
    display_main_menu()
    num_list = get_user_input()
    print(num_list)
    average = calc_average_temperature(num_list)
    print("Average temperature:", average)
    min_max = find_min_max(num_list)
    print("Minimum temperature:", min_max[0])
    print("Maximum temperature:", min_max[1])

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    user_input = input()
    numbers = user_input.split(",")
    print(numbers)
    return [float(num) for num in numbers]

def calc_average_temperature(numbers):
    total = sum(numbers)
    return total / len(numbers)

def find_min_max(numbers):
    min_value = min(numbers)
    max_value = max(numbers)
    return min_value, max_value

def sort_temperature():
    print("sort_temperature")

def calc_median_temperature(): 
    print("calc_median_temperature")

main()