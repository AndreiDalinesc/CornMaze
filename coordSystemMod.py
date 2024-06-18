
#mirroring the points
def change4to1(a):
    return (a[0],-a[1])

#syncronize the image point
def coordSync(list, p1,p2):
    if p1[1]-p2[0] < 0.01 and p2[1]-p1[0] < -0.01:
        p2=p1