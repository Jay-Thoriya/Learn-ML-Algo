# y = m + c

# weight = float(input("Enter your weight : "))
# height = float(input("Enter your Height : "))


# age = (weight/height)*100 - 13

# print("Your age is : " , age )


def calculate_bmi(weight, height):
    height_in_meters = height / 100  # Convert height from centimeters to meters
    bmi = weight / (height_in_meters ** 2)
    return bmi

def main():
    weight = float(input("Enter weight in kilograms: "))
    height = float(input("Enter height in centimeters: "))

    bmi = calculate_bmi(weight, height)
    print("BMI:", bmi)

if __name__ == "__main__":
    main()
