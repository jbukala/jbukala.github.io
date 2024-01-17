import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,2000,0.1)
f1 = 0.01
f2 = 0.02
sin_x_f1 = np.sin(f1 * x)
sin_x_f2 = 1.4 * np.sin(f2 * (x + 100))

# Create two subplots and unpack the output array immediately
plotcolor = '0.8' # Light gray for all axes and labels
with plt.rc_context({'axes.edgecolor':plotcolor, 'xtick.color':plotcolor, 'ytick.color':plotcolor}):
    f, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True)
    ax1.plot(x, sin_x_f1 + sin_x_f2, 'r')
    ax2.plot(x, sin_x_f1, 'b')
    ax3.plot(x, sin_x_f2, 'g')

    ax1.set_title('Decomposing a periodic signal into sine waves', color=plotcolor)
    ax3.set_xlabel('Time', color=plotcolor)

#ax1.axes.get_yaxis().set_ticks([])
plt.savefig('./images/sine-wave-decomposition.svg', transparent=True)
