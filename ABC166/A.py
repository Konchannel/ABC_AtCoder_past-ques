"""
問題文
AtCoder 社は、毎週土曜日にコンテストを開催しています。
コンテストにはABCとARCの2つの種類があり、毎週どちらか一方が開催されます。
ABC が開催された次の週にはARCが開催され、ARCが行われた次の週にはABCが開催されます。
先週開催されたコンテストを表す文字列Sが与えられるので、今週開催されるコンテストを表す文字列を出力してください。

制約
Sは'ABC'または'ARC'
===================
tried-01:

improvement:
"""

# === tried-01 ===
s = input()
print('ABC' if s == 'ARC' else 'ARC')

# === improvement ===
