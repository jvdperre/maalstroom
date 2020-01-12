from math_generator import *
from math_pdf import *

def main():
    #exercises = generateMix(2)
    #exercises = generateMultiMix([4, 3], 28*5, distribution= [0, 0, 10, 10, 10, 10, 10, 10, 10, 10, 0])
    exercises = generateMultiMix([4, 3, 2, 5], 28 * 5, distribution=[5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 5], problem_distribution=[3, 0, 2])
    exercises = generateMultiMix([4, 3, 2, 5], 28 * 2, distribution=[5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 5],
                                 problem_distribution=[1, 0, 1])
    createExercices(exercises)


def poll():
    multiplications = generateMultiplications(2)
    for m in multiplications:
        result = input(str(m.x) + " " + str(m.operator) + " " + str(m.y) + " = ")

        try:
            result = int(result)
            if result == m.z:
                print("correct")
            else:
                print("wrong")
        except:
            print("wrong")

if __name__ == "__main__":
    main()