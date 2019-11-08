# Script that will take inputs of weight (pounds or kilograms) and amount of
# reps performed and output an estimated one rep max based on an average of three
# formulas



def calculate_one_rep_max(weight, reps):
    weight_lifted=float(weight)
    while weight_lifted<0:
        weight_lifted=float(input("Weight must be greater than zero. Enter a weight greater than zero: "))
    
    total_reps=float(reps)
    while total_reps<0 or total_reps > 10:
        total_reps=float(input("Reps must be greater than zero or less than 10. Enter amount of reps between zero and 10: "))


    brzycki=weight_lifted*(36/(37-total_reps))
    lombardi=weight_lifted*total_reps**0.1
    wendler=weight_lifted*total_reps*0.0333+weight_lifted

    if total_reps == 1:
        one_rep_max=int(weight_lifted)
        return one_rep_max

    else:
        one_rep_max=int((brzycki+lombardi+wendler)/3)
        return one_rep_max

if __name__ == '__main__':
    output = calculate_one_rep_max(input("Enter weight in pounds or kilograms: "), input("Enter amount of reps performed: "))
    print("Your one rep max estimate is: "+str(output))