import matplotlib
matplotlib.use("TkAgg")

from matplotlib import pyplot

# preparation
labels = ["Web","iOs","Android","React Native"]
values = [40, 20, 25, 15]
colors = ["red","green","gold","purple"]
explode = [0,0.1,0,0]
# plot
pyplot.pie(values, labels=labels,colors=colors,explode=explode,shadow=True)
pyplot.axis("equal")
# show
pyplot.show()
