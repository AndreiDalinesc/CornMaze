
#mirroring the points
def change4to1(a):
    return (a[0],-a[1])

#syncronize the image point
def coordSync(list, p1,p2):
    if p1[1]-p2[0] < 0.01 and p2[1]-p1[0] < -0.01:
        p2=p1

#svg coord transformation for current location
def apply_SVG_transformation(mat, point):
    x_nou = mat[0]*point[0] + mat[2]*point[1] + mat[4]
    y_nou = mat[1]*point[0] + mat[3]*point[1] + mat[5]
    return [x_nou, y_nou]


#map_diff = [map_xmax - map_xmin, map_ymax - map_ymin, map_xmin, map_ymin]
#img_diff = [img_xmax-img_xmin, img_ymax-img_ymin, img_xmin, img_ymin]
def changeParameters(map_diff, img_diff):
    sx = map_diff[0] / img_diff[0]
    sy = map_diff[1] / img_diff[1]

    tx = map_diff[2] - sx * img_diff[2]
    ty = map_diff[3] - sy * img_diff[3]

    return sx, sy, tx, ty

def isOnTheLine(p1,p2,p):
    if p1[0]==p2[0] and p1[0]==p[0] and ((p1[1]<p[1] and p2[1]>p[1]) or (p1[1]>p[1] and p2[1]<p[1])):
        #is verticla and is between the p1 and p2
        return True
    elif p1[1]==p2[1] and p1[1]==p[1] and ((p1[0]<p[0] and p2[0]>p[0]) or (p1[0]>p[0] and p2[0]<p[0])):
        # is horizontal and is between the p1 and p2
        return True
    else:
        if p1[0]!=p[0] and p2[0]!=p[0] and p1[1]!=p[1] and p2[1]!=p[1] and p1[0]!=p2[0] and p1[1]!=p2[1]:
            #calculate the slope of a line
            m = (p2[1] - p1[1])/(p2[0] - p1[0])
            return p[1]-p1[1] == m*(p[0]-p1[0])
        else:
            return False

def coefficientsOfLine(p1, p2):
    # calculate the coefficients of the line equation from two points
    a = p2[0] - p1[0]
    b = p2[1] - p1[1]
    c = p2[1] * p1[0] - p2[0] * p1[1]

    return [a, b, c]

#coef = [a,b,c]
def intersectionOfLines(coef1, coef2):
    # calculate the determinant
    D = coef1[0] * coef2[1] - coef2[0] * coef1[1]

    if D == 0:
        return None  # the line is paralel or is the same

    # calculate the intersection point with Cramer's equation
    y = -(coef1[2] * coef2[1] - coef2[2] * coef1[1]) / D
    x = (coef1[0] * coef2[2] - coef2[0] * coef1[2]) / D

    return [x, y]

def distanceBetweenPoints(p1, p2):
    return ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5

def absPoint(p1):
    return [abs(p1[0]), abs(p1[1])]

def onTheSegment(point, p1, p2):
    return min(p1[0], p2[0]) <= point[0] <= max(p1[0], p2[0]) and min(p1[1], p2[1]) <= point[1] <= max(p1[1], p2[1])

def scale_point(px, py, cx, cy, scale_factor):
    return cx + scale_factor * (px - cx), cy + scale_factor * (py - cy)