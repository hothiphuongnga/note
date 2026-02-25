import os
import datetime
import subprocess
import random

REPO_PATH = "/Users/phuongnga/Documents/Project/note"
FILE_NAME = "auto_commit.txt"

os.chdir(REPO_PATH)

def create_commit_for_date(date):
    # random giờ hành chính
    hour = random.randint(9, 18)
    minute = random.randint(0, 59)

    date_str = date.replace(hour=hour, minute=minute).strftime('%Y-%m-%dT%H:%M:00')

    # ghi timestamp để mỗi commit luôn khác
    with open(FILE_NAME, "w") as f:
        f.write(str(datetime.datetime.now()))

    subprocess.run(["git", "add", FILE_NAME], check=True)

    subprocess.run(
        ["git", "commit", "-m", f"commit {date.strftime('%Y-%m-%d')}", "--date", date_str],
        check=True,
        env={**os.environ, "GIT_AUTHOR_DATE": date_str, "GIT_COMMITTER_DATE": date_str}
    )

start_date = datetime.datetime(2024, 3, 1)

# 30 ngày
for i in range(30):
    current_date = start_date + datetime.timedelta(days=i)

    # chỉ thứ 2 -> thứ 6
    if 0 <= current_date.weekday() <= 4:
        print("Commit:", current_date.strftime("%Y-%m-%d"))
        create_commit_for_date(current_date)
    else:
        print("Skip:", current_date.strftime("%Y-%m-%d"))

subprocess.run(["git", "push", "origin", "main"], check=True)

print("DONE")