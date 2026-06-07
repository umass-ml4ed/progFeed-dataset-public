# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(firstList, lastList):
    nameList = []
    for firstName in firstList:
        for lastName in lastList:
            nameList.append(f"{firstName} {lastName}")
    return nameList

def average_scores(scoresList):
    averageScores = []
    for students in scoresList:
        assignments = len(students)
        scoreSum = 0
        for assignment in students:
            match assignment[1]:
                case 0:
                    scoreSum += assignment[0]
                case 1:
                    scoreSum += 0.9 * assignment[0]
                case 2:
                    scoreSum += 0.75 * assignment[0]
                case 3:
                    scoreSum += 0.5 * assignment[0]
                case 4:
                    scoreSum += 0
        averageScore = scoreSum / assignments
        averageScores.append(averageScore)

    return averageScores



