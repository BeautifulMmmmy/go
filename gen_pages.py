import shutil
import os

template = "a13.html"   # 用你已经确认没问题的页面
start = 14
end = 32

for i in range(start, end + 1):
    name = f"a{i:02d}.html"
    if not os.path.exists(name):
        shutil.copy(template, name)
        print(f"created {name}")
    else:
        print(f"skip {name} (exists)")
