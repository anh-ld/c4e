def is_inside(point, rect):
    return (point[0] in range(rect[0], rect[0] + rect[2] + 1)) and \
        (point[1] in range(rect[1], rect[1] + rect[3] + 1))

test1 = is_inside([200, 120], [140, 60, 100, 200])
if test1:
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
