colors = ["red", "yellow", "green", "blue"]

i = 0
while i < len(colors):
    print("when I was %d, my favorite color was %s" % (i, colors[i]))  # https://pyformat.info/)
    print("when I was %d, my favorite color was %s".format(i, colors[i])) # % (i, colors[i]))  # https://pyformat.info/)
    i = i + 1
