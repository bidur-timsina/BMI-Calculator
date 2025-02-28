
# < 16.0            Severely Underweight
# 16.0 - 18.4      Underweight
# 18.5 - 24.9      Normal
# 25.0 - 29.9      Overweight
# 30.0 - 34.9      Moderately Obese
# 35.0 - 39.9      Severely Obese
# > 40.0           Morbidly Obese

def bmi_to_remarks(bmi):
    if bmi < 16.0:
        return "Severely Underweight"
    elif bmi >= 16.0 and bmi < 18.5:
        return "Underweight"
    elif bmi >= 18.5 and bmi < 25.0:
        return "Normal"
    elif bmi >= 25.0 and bmi < 30.0:
        return "Overweight"
    elif bmi >= 30.0 and bmi < 35.0:
        return "Moderately Obese"
    elif bmi >= 35.0 and bmi < 40.0:
        return "Severely Obese"
    else:
        return "Morbidly Obese"
    
def bmi_calculate(weight, height):
    hight_in_squre_meter = (float(height)*0.0254)**2

    bmi = float(weight)/hight_in_squre_meter
    return round(bmi,2)