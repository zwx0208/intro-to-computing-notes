import time
import random


def countdown():
    print("🚀 游戏即将开始...")
    for i in range(3, 0, -1):
        print(f"⏰ {i}...")
        time.sleep(1)  # 暂停1秒
    print("🎮 开始！")


def guess_number():
    countdown()  # 添加倒计时效果

    secret = random.randint(1, 100)
    count = 0

    print("✨ 我在想1-100之间的一个数字...")

    while True:
        guess = int(input("🔍 你的猜测："))
        count += 1

        if guess < secret:
            print("📉 太低了！", end=" ")
        elif guess > secret:
            print("📈 太高了！", end=" ")
        else:
            print(f"\n🎊 太棒了！第{count}次猜中！")
            print(f"🏅 答案就是{secret}！")
            break

        # 添加一些随机鼓励语
        encouragements = ["继续加油！", "快接近了！", "不错的感觉！", "再试一次！"]
        print(random.choice(encouragements))


# 运行游戏
guess_number()