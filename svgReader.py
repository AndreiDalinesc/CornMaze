import svglib
import svg2json
from xml.dom import minidom
import numpy as np
from svg.path import parse_path
def apply_transformation(mat, point):
    x_nou = mat[0]*point[0] + mat[2]*point[1] + mat[4]
    y_nou = mat[1]*point[0] + mat[3]*point[1] + mat[5]
    return (x_nou, y_nou)

svgFile = "input\\simpleSVG.svg"

svg_dom = minidom.parseString(open(svgFile,'rb').read())

path_strings = [path.getAttribute('d') for path in svg_dom.getElementsByTagName('path')]
path_transformation = [path.getAttribute('transform') for path in svg_dom.getElementsByTagName('path')]
print(path_transformation)

path_trans = []
for i in path_transformation:
    if i != '':
        matrix_arg = [float(num) for num in i.replace('matrix(', '').replace(')', '').split(', ')]
        path_trans.append(matrix_arg)
    else:
        path_trans.append(i)

path_dict = []
for path in path_strings:
    parsed = path.split()
    parsed.pop(0)
    parsed.pop(2)
    print(parsed)
    path_dict.append([float(x) for x in parsed])

line_list=[]
for i in range(len(path_dict)):
    line=[]
    if path_trans[i] != '':
        line.append(apply_transformation(path_trans[i], [path_dict[i][0], path_dict[i][1]]))
        line.append(apply_transformation(path_trans[i], [path_dict[i][2], path_dict[i][3]]))
    else:
        line.append((path_dict[i][0], path_dict[i][1]))
        line.append((path_dict[i][2], path_dict[i][3]))
    line_list.append(line)





