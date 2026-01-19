def change(celsius):
    fahrenheit = celsius*1.8+32
    return fahrenheit
celsius = int(input('输入温度（摄氏度)'))
print(f'{celsius}摄氏度是{change(celsius):.1f}华氏度。')