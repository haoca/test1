from turtle import *
speed(9)            # 画笔速度
pensize(3)			# 画笔的宽度
bgcolor("black")		# 画布背景色
colors = ["red", "yellow", "purple", "blue"]  # 定义画笔线色
print(colors[0 % 4])
for x in range(400):		# 循环一次 画一条线
    print(x)
    forward(2*x) 	        # 向当前方向前进n像素
    color(colors[x % 4])  # 根据求余 调整画笔线色
    left(90)                # 向左旋转91度

mainloop()
