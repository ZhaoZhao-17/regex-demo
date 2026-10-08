import re
import time

print("=" * 50)
print("演示1：正则表达式 = 文字寻人启事")
print("=" * 50)
text = "我的电话是13812345678，邮箱是test@example.com"
phones = re.findall(r"1\d{10}", text)
emails = re.findall(r"[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.[a-zA-Z0-9_]+", text)
print("原文:", text)
print("手机号:", phones)
print("邮箱:", emails)

print()
print("=" * 50)
print("演示2：有限自动机 状态A->B->C")
print("=" * 50)

def match_ab(s):
    state = 0
    for ch in s:
        if state == 0 and ch == 'a':
            state = 1
        elif state == 1 and ch == 'b':
            state = 2
        else:
            return False
    return state == 2

for s in ["ab", "ba", "aab", "aba", "abab"]:
    print(f"输入 {s!r:8} -> {'通过' if match_ab(s) else '不通过'}")

print()
print("=" * 50)
print("演示3：灾难性回溯（理论说线性，实践在指数）")
print("=" * 50)
pattern = re.compile(r"(a+)+b")
for n in [20, 22, 24, 26]:
    s = "a" * n + "!"
    t0 = time.perf_counter()
    pattern.match(s)
    cost = time.perf_counter() - t0
    print(f"输入 {n:2d} 个 a 加 ! -> 耗时 {cost:8.4f} 秒")
