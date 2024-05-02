def calculate_bmi(height,weight):
    print("Height="+str(height))
    print("Weight="+str(weight))

    bmi=weight/(height*height)

    print("BMI="+str(bmi))

    if bmi<18.5:
        print("Under weight")
        return -1

    if bmi<=18.5 or bmi <=25.0:
        print ("Normal weight")
        return 0

    if bmi>25.0:
        print("Over weight")
        return 1

calculate_bmi(weight=85, height=1.73)