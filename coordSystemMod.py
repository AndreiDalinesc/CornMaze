
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
