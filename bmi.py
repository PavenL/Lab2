def calculate_bmi(height,weight):
    print("Height="+str(height))
    print("Weight="+str(weight))

    bmi=weight/(height*height)

    print("BMI="+str(bmi))

    if bmi<18.5:
        print("Under weight")

    if bmi<=18.5 or bmi <=25.0:
        print ("Normal weight")

    if bmi>25.0:
        print("Over weight")

calculate_bmi(weight=85, height=1.73)