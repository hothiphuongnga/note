import os
import datetime
import subprocess
import random


# Đường dẫn tới repository
REPO_PATH = "/Users/phuongnga/Documents/Project/note"  # Thay bằng đường dẫn thực tế tới thư mục repository của bạn
COMMIT_MESSAGE = "Auto commit for day {}"
FILE_NAME = "auto_commit.txt"  # Tệp sẽ được chỉnh sửa để tạo commit

# Đảm bảo đang ở trong thư mục repository
os.chdir(REPO_PATH)

# Hàm để tạo commit cho một ngày cụ thể
def create_commit_for_date(date):
    # Ghi nội dung vào file để tạo thay đổi
    with open(FILE_NAME, 'w') as f:
        f.write(f"Commit for {date.strftime('%Y-%m-%d')}\n")
    
    # Thêm file vào staging
    subprocess.run(["git", "add", FILE_NAME], check=True)
    
    # Tạo commit với ngày cụ thể
    date_str = date.strftime('%Y-%m-%dT12:00:00')
    commit_msg = COMMIT_MESSAGE.format(date.strftime('%Y-%m-%d'))
    subprocess.run(
        ["git", "commit", "-m", commit_msg, f"--date={date_str}"],
        check=True,
        env={**os.environ, "GIT_AUTHOR_DATE": date_str, "GIT_COMMITTER_DATE": date_str}
    )

# Tạo commit cho 365 ngày (chỉ Thứ 2 → Thứ 6)
start_date = datetime.datetime(2024, 1, 1)
for i in range(30):
    current_date = start_date + datetime.timedelta(days=i)

    # Chỉ commit từ Thứ 2 (0) đến Thứ 6 (4)
    if current_date.weekday() < 5:
        for _ in range(random.randint(1, 3)):
            create_commit_for_date(current_date)
    else:
        print(f"Skip weekend {current_date.strftime('%Y-%m-%d')}")
# Push tất cả commit lên remote
subprocess.run(["git", "push", "origin", "main"], check=True)  # Thay 'main' bằng nhánh của bạn nếu cần
print("All commits have been pushed to remote repository!")