# python work_directory/test/other/user_subprocess.py


import subprocess


# 非同期で実行
process = subprocess.run(["python3", "work_directory/test/other/test_subprocess.py"])
# process = subprocess.Popen(["python3", "work_directory/test/other/test_subprocess.py"])
# 親プロセスはここで続行
print("子プロセスが実行中...")
