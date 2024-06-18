from xml.dom import minidom
import coordSystemMod as cm

#svg coord transformation for current location
def apply_transformation(mat, point):
    x_nou = mat[0]*point[0] + mat[2]*point[1] + mat[4]
    y_nou = mat[1]*point[0] + mat[3]*point[1] + mat[5]
    return (x_nou, y_nou)

#import image from svg
svgFile = "input\\simpleSVG.svg"
svg_dom = minidom.parseString(open(svgFile,'rb').read())

#extract xml's attributes from svg
path_strings = [path.getAttribute('d') for path in svg_dom.getElementsByTagName('path')]
path_transformation = [path.getAttribute('transform') for path in svg_dom.getElementsByTagName('path')]

#extract vector coordonates from svg
path_trans = []
for i in path_transformation:
    if i != '':
        matrix_arg = [float(num) for num in i.replace('matrix(', '').replace(')', '').split(', ')]
        path_trans.append(matrix_arg)
    else:
        path_trans.append(i)

#change in int the value of coordonates
path_dict = []
for path in path_strings:
    parsed = path.split()
    parsed.pop(0)
    parsed.pop(2)
    path_dict.append([float(x) for x in parsed])

#apply the matrix transformations on the points
line_list=[]
for i in range(len(path_dict)):
    line=[]
    if path_trans[i] != '':
        line.append(cm.change4to1(apply_transformation(path_trans[i], [path_dict[i][0], path_dict[i][1]])))
        line.append(cm.change4to1(apply_transformation(path_trans[i], [path_dict[i][2], path_dict[i][3]])))
    else:
        line.append(cm.change4to1(path_dict[i][0], path_dict[i][1]))
        line.append(cm.change4to1(path_dict[i][2], path_dict[i][3]))
    line_list.append(line)

xmax = xmin = int(line_list[0][0][0])
ymax = ymin = int(line_list[0][0][1])


#edit point for connecting lines
for i in range(len(line_list)):
    for j in range(2):
        if line_list[i][j][0] > xmax:
            xmax = int(line_list[i][j][0])
        elif line_list[i][j][0] < xmin:
            xmin = int(line_list[i][j][0])
        if line_list[i][j][1] > ymax:
            ymax = int(line_list[i][j][1])
        elif line_list[i][j][1] < ymin:
            ymin = int(line_list[i][j][1])
        line_list[i][j] = (int(line_list[i][j][0]), int(line_list[i][j][1]))


xmin = xmin - xmin
ymax = ymax - ymin
xmax = xmax - xmin
ymin = ymin - ymin


limit_point = [(xmin % 180,ymin % 360),(xmin % 180,ymax % 360),(xmax % 180,ymax % 360),(xmax % 180,ymin % 360)]

print(limit_point)
# #generate a adiacent list
# maze_adiacent_list = { line_list[0][0]:line_list[0][1]}
# print(maze_adiacent_list)
# list = [line_list[0][1]]
#
# while list != []:
#







