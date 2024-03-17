def main():
    scores = input("Please enter the judges' scores:\n")
    diff = float(input("Please enter the difficulty rating:\n"))
    scoreList = scoresToList(scores)
    dScore = sum(scoreList)*diff
    print("The remaining three judges' scores are:")
    print(*scoreList, sep=", ")
    print("The diver's score is:",end="")
    print(round(dScore,2))

def scoresToList(scores):
    scoreList = scores.split(", ")
    scoreList = [float(x) for x in scoreList]
    scoreList = sorted(scoreList)
    scoreList = scoreList[2:-2]
    return scoreList

if __name__ == "__main__":
    main()