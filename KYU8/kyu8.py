class NumToStr:
    def convert(self,num):
        return str(num)

class CalculateBMI:
    def calculate_bmi(self,w,h):
        bmi = w / h ** 2

        if bmi <= 18.5 :
            return "underweight"
        elif bmi <= 25.0:
            return "normal weight"
        elif bmi <= 30:
            return "overweight"
        else:
            return "obese"

