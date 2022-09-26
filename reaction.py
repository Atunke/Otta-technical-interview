import pandas as pd

file = pd.read_csv("reaction.csv")
reactionLikedJobs = file[(file["direction"] == True)]
groupedData = reactionLikedJobs.groupby(["user_id"])

tempRes = []
result = []
finalRes = []


def reaction():
    for key, item in groupedData:
        for key2, item2 in groupedData:
            if str(key) == str(key2):
                continue
            similarityScore = item2["job_id"].isin(item["job_id"]).sum()
            if similarityScore > 0:
                tempRes = [key, key2, similarityScore]
                result.append(tempRes)

    finalRes = max(result, key=lambda x: x[2])

    return finalRes


def main():
    print(reaction())

main()