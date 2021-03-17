import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    while True:
        try:
            graph_data = open('adc_data.txt','r').read()
        except:
            continue
        lines = graph_data.split('\n')
        xs = []
        ys = []
        for line in lines:
            if len(line) > 1:
                x, y = line.split(',')
                xs.append(float(x))
                ys.append(float(y))
        ax1.clear()
        ax1.plot(xs, ys)
        break

ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()