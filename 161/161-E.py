"""
問題文
高橋君は明日からのN日間のうちK日を選んで働くことにしました。
整数Cと文字列Sが与えられるので、次の2つの条件を満たすようにして働く日を選びます。

ある日働いたら、その直後のC日間は働かない
Sのi文字目が x のとき、今日から i日後には働かない

高橋君が必ず働く日をすべて求めてください。

制約
1≤N≤2×10^5
1≤K≤N
0≤C≤N
Sの長さは N
Sの各文字は o か x
問題文中の条件を満たすように働く日を選ぶことが可能
===================
improvement:
要は、先頭から出勤日を埋めていくパターンと、末尾から埋めていくパターンを比べて、
両者に共通する日を出力している。
先頭から埋めていくパターンでは、i番目の出勤日は最速何日か
末尾から埋めていくパターンでは、i番目の出勤日は最遅何日か、が分かる。
両者を比較して、i番目の出勤可能範囲が出せるが、これが1日しかない場合、その日は絶対出勤しなければいけない日となる。
よってそれが答えである、という解法。すげー思いつかない―
"""
# === improvement ===
N, K, C = map(int, input().split())
S = input()

latest = [None] * K
i = len(S) + C
for j in range(K):
    i = S.rindex("o", 0, i - C)
    latest[j] = i

if i <= C or "o" not in S[:i - C]:
    i = -C - 1
    for j in range(K - 1, -1, -1):
        i = S.index("o", i + C + 1)
        if i == latest[j]:
            print(i + 1)
