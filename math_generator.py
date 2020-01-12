import random
from dataclasses import dataclass
from enum import Enum

def distributionAsPercentage(distribution):
    distr_tot = 0
    distr = []

    for i in distribution:
        distr_tot += i

    for i in distribution:
        distr.append(i / distr_tot)

    return distr

def createDistributionString(distribution):
    distr_print = []

    for i in distribution:
        distr_print.append(i * 100)

    percentage_string = "0: {0:.2f}%, 1: {1:.2f}%, 2: {2:.2f}%, 3: {3:.2f}%, 4: {4:.2f}%, 5: {5:.2f}%, 6: {6:.2f}%, 7: {7:.2f}%, 8: {8:.2f}%, 9: {9:.2f}%, 10: {10:.2f}%".format(
        *distr_print)

    return percentage_string

def getFactorDistribution(factors):
    counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    if len(factors) == 0:
        return ""

    for i in factors:
        counts[i]+=1

    for i in range(len(counts)):
        counts[i] = counts[i] / len(factors)

    return createDistributionString(counts)


# fishy as fuck...
def generateFactors(amount = 100, factor_distribution = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]):
    factor_distribution = distributionAsPercentage(factor_distribution)

    print("Generating {0:d} factors with requested distribution {1}".format(amount, createDistributionString(factor_distribution)))

    result = []

    for i in range(len(factor_distribution)):
        for j in range(round(factor_distribution[i] * amount)):
            result.append(i)

    # append with randoms
    for i in range(len(result), amount):
        result.append(result[int(random.random() * len(result))])

    # remove randoms until amount is reached
    while (len(result) > amount):
        result.remove(result[int(random.random() * len(result))])

    for i in range(10):
        random.shuffle(result)

    print(
        "Generated  {0:d} factors with actual distribution    {1}".format(amount, getFactorDistribution(result)))

    return result


def generateMultiplications(factor, amount = 100, factor_distribution = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]):
    factors = generateFactors(amount, factor_distribution)

    result = []

    for i in factors:
        result.append(MathProblem(i, factor, i*factor, MathProblemType.MULTIPLY, UnknownElement.Z))

    return result

def generateDivisions(factor, amount = 100, factor_distribution = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]):
    factors = generateFactors(amount, factor_distribution)

    result = []

    for i in factors:
        result.append(MathProblem(i*factor, factor, i, MathProblemType.DIVIDE, UnknownElement.Z))

    return result

def generateMultiplicationsWithUnknownX(factor, amount = 100, factor_distribution = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]):
    factors = generateFactors(amount, factor_distribution)

    result = []

    for i in factors:
        result.append(MathProblem(i, factor, i*factor, MathProblemType.MULTIPLY, UnknownElement.X))

    return result


def generateMix(factor, amount = 28*5, distribution = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], problem_distribution = [3, 1, 1]):
    problem_distribution = distributionAsPercentage(problem_distribution)

    multiplications = generateMultiplications(factor, int(amount * problem_distribution[0]), distribution)
    multiplicationsWithUnknownX = generateMultiplicationsWithUnknownX(factor, int(amount * problem_distribution[1]), distribution)
    divisions = generateDivisions(factor, int(amount * problem_distribution[2]), distribution)

    return multiplications + multiplicationsWithUnknownX + divisions


def generateMultiMix(factor_list, amount = 28*5, distribution = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], problem_distribution = [3, 1, 1]):
    multiplications = []
    multiplicationsWithUnknownX = []
    divisions = []

    problem_distribution = distributionAsPercentage(problem_distribution)

    for i in factor_list:
        multiplications += generateMultiplications(i, int(amount * problem_distribution[0] / len(factor_list)), distribution)
        multiplicationsWithUnknownX += generateMultiplicationsWithUnknownX(i, int(amount * problem_distribution[1] / len(factor_list)), distribution)
        divisions += generateDivisions(i, int(amount * problem_distribution[2] / len(factor_list)), distribution)

    random.shuffle(multiplications)
    random.shuffle(multiplicationsWithUnknownX)
    random.shuffle(divisions)

    return multiplications + multiplicationsWithUnknownX + divisions


class MathProblemType(Enum):
    MULTIPLY = 1
    DIVIDE = 2

    def __str__(self):
        strings = {
            MathProblemType.MULTIPLY.value: "x",
            MathProblemType.DIVIDE.value: ":"
        }
        return strings[self.value]

class UnknownElement(Enum):
    X = 1
    Y = 2
    Z = 3

@dataclass
class MathProblem:
    x: int
    y: int
    z: int
    operator: MathProblemType
    unknown: UnknownElement

