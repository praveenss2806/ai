import pandas as pd
import copy
seq = input("Enter the Sequence :")

start_to_H = 0.5
start_to_L = 0.5

H_to_H = 0.5
H_to_L = 0.5
L_to_L = 0.6
L_to_H = 0.4

H = {'A': 0.2, 'C': 0.3, 'G': 0.3, 'T': 0.2 }
L = {'A': 0.3, 'C': 0.2, 'G': 0.2, 'T': 0.3 }

ans = []
for i in range(2):
    t = []
    for j in range(len(seq)):
        t.append(0)
    ans.append(t)

ans1 = copy.deepcopy(ans)

ans[0][0] = start_to_H * H[seq[0]]
ans[1][0] = start_to_L * L[seq[0]]

ans1[0][0] = start_to_H * H[seq[0]]
ans1[1][0] = start_to_L * L[seq[0]]

for i in range(1, len(seq)):
    ans[0][i] = H[seq[i]] * (H_to_H * ans[0][i - 1] + L_to_H * ans[1][i - 1])
    ans[1][i] = L[seq[i]] * (L_to_L * ans[1][i - 1] + H_to_L * ans[0][i - 1])
    
df = pd.DataFrame(ans, columns = [i for i in seq])
print(df)

if ans1[0][0] > ans1[1][0]:
    print('H', end = "")
else:
    print('L', end = "")
for i in range(1, len(seq)):
    ans1[0][i] = H[seq[i]] * max(H_to_H * ans1[0][i - 1], L_to_H * ans1[1][i - 1])
    ans1[1][i] = L[seq[i]] * max(L_to_L * ans1[1][i - 1], H_to_L * ans1[0][i - 1])
    if ans1[0][i] > ans1[1][i]:
        print('H', end = "")
    else:
        print('L', end = "")