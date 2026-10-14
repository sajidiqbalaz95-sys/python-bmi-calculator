








#write a function t make a program using calculate_bmi
def calculate_bmi(weight_kg: float, height_cm: float) -> tuple[float, str]:

#Write a loops only use positive value sighn for user
    if weight_kg <=0  or height_cm <= 0:
       raise ValueError("Weight and height must be positive values.") 
    
#change a value 
    height_cm = height_cm/100
    bmi_value = weight_kg / (height_cm **2)

#wirte a loops for a codition weight
    if bmi_value < 18.5:
        return bmi_value, "Underweight"
    
    elif bmi_value < 25:
        return bmi_value,"Normal"
    
    elif bmi_value < 30:
        return bmi_value,"Overweight"
    
    else:
        return bmi_value, "obese"
    
#make a main function where use value
def main():
    try:
        weight = float(input("Enter your weight in kg:"))
        height = float(input("Enter your height in cm:"))
        bmi, category = calculate_bmi(weight,height)
        print(f"Your BMI is {bmi:.2f}, which is considered {category}.")
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()
    main()
    main()
    main()
    main()
    main()