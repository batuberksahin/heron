from math import sqrt
def heron(x: int, y: int, z: int):
    u=(x+y+z)/2
    return False if (u-x)<=0 or (u-y)<=0 or (u-z)<=0 else sqrt(u*(u-x)*(u-y)*(u-z)); del u