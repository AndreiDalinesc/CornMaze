from xml.dom import minidom
import coordSystemMod as cm



#import image from svg
svgFile = "input\\simpleSVG.svg"
#svgFile = "input\\simpleSVG2.svg"
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
        line.append(cm.apply_SVG_transformation(path_trans[i], [path_dict[i][0], path_dict[i][1]]))
        line.append(cm.apply_SVG_transformation(path_trans[i], [path_dict[i][2], path_dict[i][3]]))
        # line.append(cm.change4to1(cm.apply_SVG_transformation(path_trans[i], [path_dict[i][0], path_dict[i][1]])))
        # line.append(cm.change4to1(cm.apply_SVG_transformation(path_trans[i], [path_dict[i][2], path_dict[i][3]])))
    else:
        line.append([path_dict[i][0], path_dict[i][1]])
        line.append([path_dict[i][2], path_dict[i][3]])
        # line.append(cm.change4to1(path_dict[i][0], path_dict[i][1]))
        # line.append(cm.change4to1(path_dict[i][2], path_dict[i][3]))
    line_list.append(line)
print(line_list)

img_xmax = img_xmin = int(line_list[0][0][0])
img_ymax = img_ymin = int(line_list[0][0][1])


#edit point for connecting lines
for i in range(len(line_list)):
    for j in range(2):
        if line_list[i][j][0] > img_xmax:
            img_xmax = int(line_list[i][j][0])
        elif line_list[i][j][0] < img_xmin:
            img_xmin = int(line_list[i][j][0])
        if line_list[i][j][1] > img_ymax:
            img_ymax = int(line_list[i][j][1])
        elif line_list[i][j][1] < img_ymin:
            img_ymin = int(line_list[i][j][1])
        line_list[i][j] = [int(line_list[i][j][0]), int(line_list[i][j][1])]

print(line_list)
print()
for i in line_list:

    print(i)
print(img_xmax,img_ymax, img_xmin,  img_ymin)

xmin = img_xmin - img_xmin
ymax = img_ymax - img_ymin
xmax = img_xmax - img_xmin
ymin = img_ymin - img_ymin


#using for change the system coordonates
img_diff = [img_xmax-img_xmin, img_ymax-img_ymin, img_xmin, img_ymin]

limit_point = [[xmin,ymin],[xmin,ymax],[xmax,ymax],[xmax,ymin]]
#print(limit_point)

for i in range(len(limit_point)):
    limit_point[i] = [limit_point[i][0], limit_point[i][1]]

print(limit_point)

#generate a adiacent list
# maze_adiacent_list = { line_list[0][0]:line_list[0][1]}
# print(maze_adiacent_list)
# list = [line_list[0][1]]
#
# while list != []:








