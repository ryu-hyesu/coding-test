n, m= map(int, input().split())
data = []
for _ in range(n) :
    data.append(input())

type1 = ["BWBWBWBW","WBWBWBWB", "BWBWBWBW","WBWBWBWB", "BWBWBWBW","WBWBWBWB", "BWBWBWBW","WBWBWBWB"]
type2 = ["WBWBWBWB", "BWBWBWBW","WBWBWBWB", "BWBWBWBW","WBWBWBWB", "BWBWBWBW","WBWBWBWB", "BWBWBWBW"]

result = 250
for a in range(n - 7) :
    for b in range(m - 7) :
        compare_data = [row[b:b+8] for row in data[a:a+8]]

        cnt1 = 0
        cnt2 = 0
        for i in range(8) :
            for j in range(8) :
                compare = compare_data[i][j]
                if type1[i][j] != compare :
                    cnt1 += 1

                if type2[i][j] != compare :
                    cnt2 += 1

        result = min(result, cnt1, cnt2)

print(result)