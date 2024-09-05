import random

# 当前版本号
current_version = "v0.0.3"
developer_password = "devmodepwd"

def display_version():
    print(f"当前版本：{current_version}")

def guess_number(min_range, max_range, number_to_guess=None, developer_mode=False, limit_attempts=None):
    if developer_mode:
        print(f"开发者模式已启用。正确的数字是 {number_to_guess}。")
    else:
        number_to_guess = random.randint(min_range, max_range)
    
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
            guess = int(input(f"请输入你猜的数字（{min_range}-{max_range}）："))
        except ValueError:
            print("请输入一个有效的整数！")
            continue
        
        if guess < min_range or guess > max_range:
            print(f"你的输入超出了当前范围，请输入{min_range}到{max_range}之间的数字。")
            continue
        
        attempts += 1
        
        if guess == number_to_guess:
            print("恭喜你，猜对了！Game Over!")
            break
        elif guess < number_to_guess:
            min_range = guess
            print(f"你猜的数字在 {min_range} 到 {max_range} 之间。")
        else:
            max_range = guess
            print(f"你猜的数字在 {min_range} 到 {max_range} 之间。")

def select_difficulty():
    print("请选择难度模式：")
    print("1. 简单模式 (0-100)")
    print("2. 中等模式 (0-500)")
    print("3. 困难模式 (0-5000)")
    print("4. 自定义模式 (自定义范围，最大可为0-500000)")
    
    while True:
        try:
            choice = int(input("请输入难度选择 (1-4)："))
            if choice == 1:
                return 0, 100, False, None
            elif choice == 2:
                return 0, 500, False, None
            elif choice == 3:
                return 0, 5000, False, None
            elif choice == 4:
                return custom_range(), False, None
            elif choice == 9:
                return developer_mode()
            else:
                print("请输入有效的数字 (1-4)！")
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

def developer_mode():
    while True:
        password = input("请输入开发者密码：")
        if password == developer_password:
            print("密码正确，进入开发者模式。")
            min_range = 0
            max_range = 100  # 你可以根据需要设置一个默认范围
            number_to_guess = random.randint(min_range, max_range)
            return min_range, max_range, True, number_to_guess
        else:
            print("密码错误，请重新输入。")

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
    display_version()  # 显示当前版本号
    while True:
        min_range, max_range, developer_mode, number_to_guess = select_difficulty()
        limit_attempts = enable_limit_attempts()
        guess_number(min_range, max_range, number_to_guess, developer_mode, limit_attempts)
        
        replay = input("你想再玩一次吗？(y/n)：").lower()
        if replay != 'y':
            print("感谢参与，再见！")
            break

# 开始游戏
play_game()
