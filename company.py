import pandas as pd

file = pd.read_csv("company.csv")
file2 = pd.read_csv("reaction.csv")

reactionLikedJobs = file2[(file2["direction"] == True)]

file["job_id"].convert_dtypes(convert_integer=True)

mergeFile = pd.merge(file, reactionLikedJobs)
groupedMf = mergeFile.groupby(["company_id"])

tempRes = []
result = []
finalRes = []

def company():
    for key, item in groupedMf:
        for key2, item2 in groupedMf:
            if str(key) == str(key2):
                continue
            similarityScore = item2["user_id"].isin(item["user_id"]).sum()
            if similarityScore > 0:
                tempRes = [key, key2, similarityScore]
                result.append(tempRes)

    finalRes = max(result, key=lambda x: x[2])

    return finalRes

def main():
    print(company())

main()