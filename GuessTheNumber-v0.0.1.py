print ('#################################')
print ('#             猜数字            #')
print ('#  这是一个非常有趣的猜数字游戏 #')
print ('# 我已经想了一个数字在1-100中间 #')
print ('#           请你猜出他          #')
print ('#################################')
import random

def guess_number():
    # 随机生成1到100之间的数字
    number_to_guess = random.randint(1, 100)
    
    print("欢迎来到猜数字游戏！我已经在1到100之间选择了一个数字，快来猜猜看吧！")
    
    while True:
        try:
            guess = int(input("请输入你的猜测："))
        except ValueError:
            print("请输入一个有效的整数！")
            continue
        
        if guess < 1 or guess > 100:
            print("请输入1到100之间的数字。")
            continue
        
        if guess < number_to_guess:
            print(f"你猜的数字在 {guess} 到 100 之间。")
        elif guess > number_to_guess:
            print(f"你猜的数字在 1 到 {guess} 之间。")
        else:
            print("恭喜你，猜对了！Game Over!")
            break

# 开始游戏
guess_number()
# 询问是否再来一局，输入y再来一把，输入n关闭