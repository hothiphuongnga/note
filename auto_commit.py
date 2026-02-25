# import os
# import datetime
# import subprocess
# import random

# REPO_PATH = "/Users/phuongnga/Documents/Project/note"
# FILE_NAME = "auto_commit.txt"

# os.chdir(REPO_PATH)

# def create_commit_for_date(date):
#     # random giờ hành chính
#     hour = random.randint(9, 18)
#     minute = random.randint(0, 59)

#     date_str = date.replace(hour=hour, minute=minute).strftime('%Y-%m-%dT%H:%M:00')

#     # ghi timestamp để mỗi commit luôn khác
#     with open(FILE_NAME, "w") as f:
#         f.write(str(datetime.datetime.now()))

#     subprocess.run(["git", "add", FILE_NAME], check=True)

#     subprocess.run(
#         ["git", "commit", "-m", f"commit {date.strftime('%Y-%m-%d')}", "--date", date_str],
#         check=True,
#         env={**os.environ, "GIT_AUTHOR_DATE": date_str, "GIT_COMMITTER_DATE": date_str}
#     )

# start_date = datetime.datetime(2024, 2,1)

# # 30 ngày
# for i in range(7):
#     current_date = start_date + datetime.timedelta(days=i)

#     # chỉ thứ 2 -> thứ 6  tử 0-> 4
#     # if 0 <= current_date.weekday() <= 4:
#     if current_date.weekday() ==4 or current_date.weekday() == 2:
#         for _ in range(random.randint(1, 3)):
#             create_commit_for_date(current_date)

# subprocess.run(["git", "push", "origin", "main"], check=True)

# print("DONE")

# chạy random ngày
import os
import datetime
import subprocess
import random

REPO_PATH = "/Users/phuongnga/Documents/Project/note"
FILE_NAME = "auto_commit.txt"

os.chdir(REPO_PATH)

def create_commit_for_date(date):
    hour = random.randint(9, 18)
    minute = random.randint(0, 59)

    date_str = date.replace(hour=hour, minute=minute).strftime('%Y-%m-%dT%H:%M:00')

    with open(FILE_NAME, "w") as f:
        f.write(str(datetime.datetime.now()))

    subprocess.run(["git", "add", FILE_NAME], check=True)

    subprocess.run(
        ["git", "commit", "-m", f"up {date.strftime('%Y-%m-%d')}", "--date", date_str],
        check=True,
        env={**os.environ, "GIT_AUTHOR_DATE": date_str, "GIT_COMMITTER_DATE": date_str}
    )

start_date = datetime.datetime(2024, 2, 1)
end_date = datetime.datetime(2024, 5, 1)

# random 30 ngày trong khoảng
random_days = random.sample(
    [start_date + datetime.timedelta(days=i)
     for i in range((end_date - start_date).days)
     if 0 <= (start_date + datetime.timedelta(days=i)).weekday() <= 4],
    30
)

for day in random_days:
    # mỗi ngày 1–3 commit
    for _ in range(random.randint(1, 3)):
        print("Commit:", day.strftime("%Y-%m-%d"))
        create_commit_for_date(day)

subprocess.run(["git", "push", "origin", "main"], check=True)

print("DONE")