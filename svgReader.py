from xml.dom import minidom
import coordSystemMod as cm

def addLinkd(dicts,segment,point):
    if point not in dicts[tuple(segment[0])]:
            dicts[tuple(point)].append(segment[0])
            dicts[tuple(segment[0])].append(point)
            dicts[tuple(segment[0])].remove(segment[1])

    if point not in adj_list[tuple(segment[1])]:
            dicts[tuple(point)].append(segment[1])
            dicts[tuple(segment[1])].append(point)
            dicts[tuple(segment[1])].remove(segment[0])

def changePoint(lists,point,value):
    for i in range(len(lists)):
        for j in range(len(lists[i])):
            if lists[i][j] == point:
                lists[i][j] = value

def syncPoint(lists):
    error = 5
    allPoint = []
    for i in lists:
        for j in i:
            allPoint.append(j)
    value = [ ]
    for i in range(len(allPoint)-1):
       if i not in value:
           for j in range(i+1,len(allPoint)):
               errorX=allPoint[i][0]-allPoint[j][0]
               errorY=allPoint[i][1]-allPoint[j][1]
               if abs(errorX)<error and errorY==0:
                   changePoint(lists,allPoint[j],allPoint[i])
               elif abs(errorY)<error and errorX==0:
                   changePoint(lists,allPoint[j],allPoint[i])
               elif (abs(errorX)<error and abs(errorY)<error and errorX>0 and errorY>0):
                   changePoint(lists,allPoint[j],allPoint[i])
       value.append(i)

    return allPoint

def makeAdjList(pointList):
    dicts = dict()
    for i in range(len(pointList)):
        if tuple(pointList[i][0]) not in dicts.keys():
            dicts[tuple(pointList[i][0])] = list()
            dicts[tuple(pointList[i][0])].append(pointList[i][1])
            if tuple(pointList[i][1]) not in dicts.keys():
                dicts[tuple(pointList[i][1])] = list()
                dicts[tuple(pointList[i][1])].append(pointList[i][0])
            else:
                dicts[tuple(pointList[i][1])].append(pointList[i][0])
        else:
            dicts[tuple(pointList[i][0])].append(pointList[i][1])
            if tuple(pointList[i][1]) not in dicts.keys():
                dicts[tuple(pointList[i][1])] = list()
                dicts[tuple(pointList[i][1])].append(pointList[i][0])
    return dicts

def extremIsIntersection(dicts):
    for i in dicts.keys():
        for j in dicts[i]:
            for k in dicts.keys():
                if k != i and k != tuple(j):
                    if cm.isOnTheLine(i, tuple(j), k):
                        dicts[i].append(list(k))
                        dicts[i].remove(j)
                        dicts[tuple(j)].append(list(k))
                        dicts[tuple(j)].remove(list(i))
                        dicts[k].append(list(i))
                        dicts[k].append(list(j))

def isALinesIntersection(dicts,lineList):
    for i in range(len(lineList) - 1):
        for j in range(i + 1, len(lineList)):
            coef_i = cm.coefficientsOfLine(lineList[i][0], lineList[i][1])
            coef_j = cm.coefficientsOfLine(lineList[j][0], lineList[j][1])
            intersection = cm.intersectionOfLines(coef_i,coef_j)
            if intersection != None and cm.onTheSegment(intersection, lineList[i][0],
                                                        lineList[i][1]) and cm.onTheSegment(intersection,
                                                                                             lineList[j][0],
                                                                                             lineList[j][1]):
                if tuple(intersection) not in dicts.keys():
                    dicts[tuple(intersection)] = list()
                if lineList[i][0] in dicts[tuple(lineList[i][1])] and lineList[i][1] in adj_list[
                    tuple(lineList[i][0])]:
                    addLinkd(dicts, lineList[i], intersection)
                if lineList[j][0] in dicts[tuple(lineList[j][1])] and lineList[j][1] in adj_list[
                    tuple(lineList[j][0])]:
                    addLinkd(dicts, lineList[j], intersection)

#import image from svg
#svgFile = "input\\simpleSVG.svg"
svgFile = "input\\simpleSVG2.svg"
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

#change in float the value of coordonates
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
        line.append(cm.change4to1(cm.apply_SVG_transformation(path_trans[i], [path_dict[i][0], path_dict[i][1]])))
        line.append(cm.change4to1(cm.apply_SVG_transformation(path_trans[i], [path_dict[i][2], path_dict[i][3]])))
    else:
        line.append(cm.change4to1(path_dict[i][0], path_dict[i][1]))
        line.append(cm.change4to1(path_dict[i][2], path_dict[i][3]))
    line_list.append(line)

img_xmax = img_xmin = int(line_list[0][0][0])
img_ymax = img_ymin = int(line_list[0][0][1])

#calculating the min and max points of system
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

limits = {str(img_xmax):[], str(img_xmin):[], str(img_ymax):[], str(img_ymin):[]}

#synchronizing the points of vectors
syncPoint(line_list)

#generating an adjacency list for an unoriented graph
adj_list = makeAdjList(line_list)

#completing the adjacency list with the intersections which is on the lines
extremIsIntersection(adj_list)

#completing the adjacency list with the intersections which is the intersections on lines
isALinesIntersection(adj_list,line_list)

#get the limit of the maze

for i in adj_list.keys():
    for j in limits.keys():
        if i[0]==int(j) or i[1]==int(j):
            limits[j].append(i)

# for i in limits.keys():
#     if len(limits[i])>1:
#         x=0
#         y=0
#         for j in limits[i]:
#             x = x + limits[i][j][0]
#             y = y + limits[i][j][1]
#         x = x//len(limits[i])
#         y = y//len(limits[i])
#         if x == int(i):
#             x = x+0.5
#             limits[str(x)] = [[x,y]]
#         elif y == int(i):
#             y = y+0.5
#             limits[str(y)] = [[x,y]]

limit_point = []
for i in limits.keys():
    limit_point.append(limits[i][0])

#using for change the system coordonates
img_diff = [img_xmax-img_xmin, img_ymax-img_ymin, img_xmin, img_ymin]
