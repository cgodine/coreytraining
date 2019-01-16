# Script that will take inputs of weight (pounds or kilograms) and amount of
# reps performed and output an estimated one rep max based on an average of three
# formulas


weight_lifted=float(input("Enter amount of weight lifted (in either pounds or kilograms): "))
while weight_lifted<0:
    weight_lifted=float(input("Weight must be greater than zero. Enter a weight greater than zero: "))
    
exercise_reps=float(input("Enter amount of repetitions performed: "))
while exercise_reps<0:
    exercise_reps=float(input("Reps must be greater than zero. Enter amount of reps greater than zero: "))

brzycki=weight_lifted*(36/(37-exercise_reps))
lombardi=weight_lifted*exercise_reps**0.1
wendler=weight_lifted*exercise_reps*0.0333+weight_lifted

one_rep_max=int((brzycki+lombardi+wendler)/3)
print("Your one rep max estimate is: "+str(one_rep_max)+" pounds")