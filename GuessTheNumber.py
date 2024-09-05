import random

def guess_number(min_range, max_range, limit_attempts=None):
    # 根据难度选择随机生成数字
    number_to_guess = random.randint(min_range, max_range)
    
    print(f"欢迎来到猜数字游戏！我已经在{min_range}到{max_range}之间选择了一个数字，快来猜猜看吧！")
    
    attempts = 0  # 猜测次数

    while True:
        # 如果开启了限制猜测次数功能
        if limit_attempts is not None:
            if attempts >= limit_attempts:
                print("你已经超过了猜测次数限制。游戏失败！")
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
        
        attempts += 1  # 每次有效输入增加猜测次数
        
        if guess == number_to_guess:
            print("恭喜你，猜对了！Game Over!")
            break
        elif guess < number_to_guess:
            min_range = guess  # 更新最小范围为当前猜测值
            print(f"你猜的数字在 {min_range} 到 {max_range} 之间。")
        else:
            max_range = guess  # 更新最大范围为当前猜测值
            print(f"你猜的数字在 {min_range} 到 {max_range} 之间。")

def select_difficulty():
    print("请选择难度模式：")
    print("1. 简单模式 (0-100)")
    print("2. 中等模式 (0-500)")
    print("3. 困难模式 (0-5000)")
    
    while True:
        try:
            choice = int(input("请输入难度选择 (1-3)："))
            if choice == 1:
                return 0, 100
            elif choice == 2:
                return 0, 500
            elif choice == 3:
                return 0, 5000
            else:
                print("请输入有效的数字 (1-3)！")
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
    while True:
        # 玩家选择难度模式
        min_range, max_range = select_difficulty()
        
        # 玩家选择是否启用猜测次数限制
        limit_attempts = enable_limit_attempts()
        
        # 开始游戏
        guess_number(min_range, max_range, limit_attempts)
        
        # 询问玩家是否继续
        replay = input("你想再玩一次吗？(y/n)：").lower()
        if replay != 'y':
            print("感谢参与，再见！")
            break

# 开始游戏
play_game()
