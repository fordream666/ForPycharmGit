import turtle, datetime
def drawGap(): #绘制数码管间隔
    turtle.penup() #抬笔
    turtle.fd(5)  #行进距离是5
def drawLine(draw):   #绘制单段数码管
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)
def drawDigit(d): #根据数字绘制七段数码管
    drawLine(True)if d in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if d in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()  # 为绘制后续数字确定位置
    turtle.fd(20)  
def drawDate(date):         #根据日期画出对应数字，data为日期，格式：'%Y-%m=%d+
    turtle.pencolor("red")  #字体的颜色
    for i in date:          #设置具体的格式
        if i == '-':
            turtle.write('年',font=("楷体", 30, "normal"))
            turtle.pencolor("yellow")
            turtle.fd(40)
        elif i == '=':
            turtle.write('月',font=("楷体", 30, "normal"))
            turtle.pencolor("pink")
            turtle.fd(40)
        elif i == '+':
            turtle.write('日',font=("楷体", 30, "normal"))
        else:
            drawDigit(eval(i))
def main():
    turtle.setup(800, 350, 200, 200)  #显示窗体的大小
    turtle.speed(10) # 设置画笔移动速度，画笔绘制的速度范围[0,10]整数，数字越大越快。
    turtle.penup()
    turtle.fd(-350)
    turtle.pensize(5)
    drawDate(datetime.datetime.now().strftime('%Y-%m=%d+'))  #日期的读取方式，便于控制输出的顺序
    turtle.hideturtle()
main()
