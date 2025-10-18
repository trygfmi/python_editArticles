# python work_directory/feature/get_regex_rowNumber.py


import re

# 複数行の文字列
text = """Line 1: Hello, world!
Line 2: This is a test.
Line 3: Python regex example.
Line 4: Another test line."""

# 正規表現パターン（例: "Line \d+: "で始まる行）
# pattern = r"^Line \d+: "
pattern = r"test"

# 行ごとに分割
lines = text.splitlines()

# # 一致する行番号を記録（1-based index）
# matching_lines = []
# for i, line in enumerate(lines, 1):
#     if re.match(pattern, line):  # 行の先頭から一致するかチェック
#         matching_lines.append(i)
        
# 一致する行番号を記録（1-based index）
matching_lines = []
for i, line in enumerate(lines, 1):
    if re.search(pattern, line, re.IGNORECASE):
        matching_lines.append(i)

# 結果を表示
print(f"パターン '{pattern}' に一致する行番号: {matching_lines}")

