import pygal


def draw_line(title, xvals, yvals):
    lineplot = pygal.Line(height=400)
    lineplot.title = title
    lineplot.x_labels = xvals
    lineplot.add("Data", yvals)
    lineplot.render_in_browser()


x_vals = [0, 1, 3, 5, 4, 6, 2, 9, 8, 7]
y_vals = [4, 6, 2, 6, 5, 1, 3, 5, 8, 1]

draw_line("My Line Plot", x_vals, y_vals)


def draw_xy(title, xvals, yvals):
    coords = [(xval,yval) for xval, yval in zip(xvals,yvals)]
    xyplot = pygal.XY(height= 400)
    xyplot.title = title
    xyplot.add("Data", coords)
    xyplot.render_in_browser()
    
draw_xy("My XY plot",x_vals, y_vals)