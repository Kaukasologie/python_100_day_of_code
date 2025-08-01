import colorgram

colors = colorgram.extract('hirst_dot.png', 25)
rgb_colors = []

for color_object in colors:
    rgb = color_object.rgb
    red = rgb[0]  # or red = rgb.r
    green = rgb[1]
    blue = rgb[2]
    color = (red, green, blue)
    rgb_colors.append(color)  # included 5 bg colors

for color in range(5):  # delete 5 first bg colors
    rgb_colors.pop(0)
