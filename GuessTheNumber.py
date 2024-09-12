import requests
import random
import subprocess
import time
import os

# GitHub API 配置
public_repo_api_url = "https://api.github.com/repos/ANDYzytnb/GuessTheNumberPublicDownloadAPI/releases/latest"
public_repo_base_url = "https://github.com/ANDYzytnb/GuessTheNumberPublicDownloadAPI/releases/download"
current_version = "v2.0.0"

# 开发者模式密码
dev_mode_password = "devmodepwd"

def get_latest_version():
    print("正在检查更新...")
    try:
        response = requests.get(public_repo_api_url)
        response.raise_for_status()
        latest_release = response.json()
        return latest_release['tag_name']
    except requests.exceptions.RequestException as e:
        print(f"检查更新时发生错误: {e}")
        return None

def download_update(latest_version):
    print("正在下载更新...")
    download_url = f"{public_repo_base_url}/{latest_version}/GuessTheNumber-{latest_version}.exe"
    try:
        response = requests.get(download_url, stream=True)
        response.raise_for_status()
        filename = f"GuessTheNumber-{latest_version}.exe"
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"更新下载完成: {filename}")
        return filename
    except requests.exceptions.RequestException as e:
        print(f"下载更新时发生错误: {e}")
        return None

def check_for_update():
    latest_version = get_latest_version()
    if latest_version:
        if latest_version != current_version:
            print(f"发现更新: {latest_version}")
            new_file = download_update(latest_version)
            if new_file:
                print(f"即将启动新版本: {new_file}")
                subprocess.Popen(new_file, close_fds=True)
                return True
        else:
            print("当前已经是最新版本。")
    else:
        print("无法获取最新版本信息。")
    return False

def clear_console():
    """根据操作系统清空控制台"""
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # macOS and Linux
        os.system('clear')

def guess_number(min_range, max_range, number_to_guess=None, developer_mode=False, limit_attempts=None, challenge_mode=False):
    if developer_mode:
        print(f"开发者模式已启用。正确的数字是 {number_to_guess}。")
    else:
        number_to_guess = random.randint(min_range, max_range)
    
    if challenge_mode:
        print(f"欢迎来到挑战模式！我已经在{min_range}到{max_range}之间选择了一个数字，快来猜猜看吧！")
    else:
        print(f"欢迎来到猜数字游戏！我已经在{min_range}到{max_range}之间选择了一个数字，快来猜猜看吧！")

    attempts = 0
    while True:
        if limit_attempts is not None:
            if attempts >= limit_attempts:
                print("你已经超过了猜测次数限制。游戏失败！")
                show_answer = input("你想看到正确的数字吗？(y/n)：").lower()
                if show_answer == 'y':
                    print(f"正确的数字是 {number_to_guess}。")
                break
            print(f"你还有 {limit_attempts - attempts} 次猜测机会。")
        
        try:
            guess = int(input("请输入："))  # 用户输入猜测
            clear_console()  # 清除输入行
        except ValueError:
            print("请输入一个有效的整数！")
            time.sleep(1)
            clear_console()  # 清除提示行
            continue
        
        if guess < min_range or guess > max_range:
            print(f"你的输入超出了当前范围，请输入{min_range}到{max_range}之间的数字。")
            time.sleep(1)
            clear_console()  # 清除提示行
            continue
        
        attempts += 1
        
        if guess == number_to_guess:
            print("恭喜你，猜对了！Game Over!")
            break
        elif guess < number_to_guess:
            print("太小了！")
        else:
            print("太大了！")

        time.sleep(1)  # 提示显示1秒钟
        clear_console()  # 清除提示

def select_difficulty():
    print("请选择难度模式：")
    print("1. 简单模式 (0-100)")
    print("2. 中等模式 (0-500)")
    print("3. 困难模式 (0-5000)")
    print("4. 自定义模式 (自定义范围，最大可为0-500000)")
    print("5. 挑战模式 (0-10000)")

    while True:
        try:
            choice = int(input("请输入难度选择 (1-5)："))
            if choice == 1:
                return 0, 100, False, None, False
            elif choice == 2:
                return 0, 500, False, None, False
            elif choice == 3:
                return 0, 5000, False, None, False
            elif choice == 4:
                return *custom_range(), False, None, False
            elif choice == 5:
                return 0, 10000, False, None, True  # 挑战模式范围是0到10000
            elif choice == 9:
                password = input("请输入开发者密码：")
                if password == dev_mode_password:
                    print("密码正确，进入开发者模式。")
                    min_range, max_range = custom_range()
                    number_to_guess = random.randint(min_range, max_range)
                    print(f"当前版本：{current_version}")
                    print(f"OTA 请求 URL：{public_repo_api_url}")
                    print(f"开发者模式提示：正确的数字是 {number_to_guess}")
                    return min_range, max_range, True, number_to_guess, False
                else:
                    print("密码错误，回到普通模式。")
                    return (0, 0, False, None, False)
            else:
                print("请输入有效的数字 (1-5)！")
        except ValueError:
            print("请输入有效的整数！")

def custom_range():
    print("你已选择自定义模式，最大范围可为0到500000。")
    while True:
        try:
            min_range = int(input("请输入自定义最小值："))
            max_range = int(input("请输入自定义最大值（最大不超过500000）："))
            if min_range >= 0 and max_range <= 500000 and min_range < max_range:
                return min_range, max_range
            else:
                print("请确保最小值大于等于0，最大值小于等于500000，且最小值小于最大值。")
        except ValueError:
            print("请输入有效的整数！")

def enable_limit_attempts():
    while True:
        enable_limit = input("你想开启限制猜测次数功能吗？(y/n)：").lower()
        if enable_limit == 'y':
            while True:
                try:
                    limit_attempts = int(input("请输入猜测次数限制："))
                    if limit_attempts > 0:
                        return limit_attempts
                    else:
                        print("请输入一个大于0的整数。")
                except ValueError:
                    print("请输入一个有效的整数！")
        elif enable_limit == 'n':
            return None
        else:
            print("请输入有效的选项 (y/n)！")

def play_game():
    update_success = check_for_update()  # 检查更新
    if update_success:
        return  # 退出当前程序
    
    display_version()  # 显示当前版本号
    while True:
        min_range, max_range, developer_mode, number_to_guess, challenge_mode = select_difficulty()
        if min_range is None:
            print("无法继续游戏。")
            return
        
        limit_attempts = enable_limit_attempts() if not challenge_mode else None
        guess_number(min_range, max_range, number_to_guess, developer_mode, limit_attempts, challenge_mode)
        
        replay = input("你想再玩一次吗？(y/n)：").lower()
        if replay != 'y':
            print("感谢参与，再见！")
            break

# 显示当前版本号
def display_version():
    print(f"当前版本：{current_version}")

# 运行游戏
if __name__ == "__main__":
    play_game()
