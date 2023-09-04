from math import cos, sin, sqrt, radians

def caculate(theta=0, h2=0, v=0, g=980):
    """
    v1=2.21
    v2=2.93
    v3=3.13
    v4=4.18
    :param theta:
    :param h2:
    :param v:
    :param g:
    :return:
    """
    h2 = h2 -4.5
    v =v*100
    g = g * 100
    left = v * cos(radians(theta)) * v * sin(radians(theta)) / g
    right = v * cos(radians(theta)) * (sqrt(pow(v,2)*pow(sin(radians(theta)), 2)/pow(g, 2) + 2*h2/g))
    L =  left + right
    print("theta=%s, h2=%s, v=%s" % ('{:.6f}'.format(theta),
                                     '{:.6f}'.format(h2),
                                     '{:.6f}'.format(v)),
          "L=",'{:.6f}'.format(L))
    return L


def caculate2(theta=0, h2=0, h4=0, v=0, g=980):
    """
    v1=2.21
    v2=2.93
    v3=3.13
    v4=4.18
    :param theta:
    :param h2:
    :param v:
    :param g:
    :return:
    """
    h2 = h2 -4.5
    v =v*100
    g = g * 100
    p1 = v*cos(radians(theta))
    p2 = pow(v, 2) * pow(sin(radians(theta)), 2) / pow(g, 2)
    p3 = 2*(h2 + h4)/g
    p4 = pow(v, 2) * pow(sin(radians(theta)), 2) / pow(g, 2)
    p5 = 2*h2/g

    delta_L =  p1 * (sqrt(p2+p3) - sqrt(p4+p5))
    print("theta=%s, h2=%s, h4=%s, v=%s" % ('{:.6f}'.format(theta),
                                     '{:.6f}'.format(h2),
                                            '{:.6f}'.format(h4),
                                     '{:.6f}'.format(v)),
          "L=",'{:.6f}'.format(delta_L))
    return delta_L

# caculate(theta=35, h2=13.19, v=4.18, g=9.8)
# caculate(theta=40, h2=14.78, v=2.93, g=9.8)
# caculate(theta=30, h2=11.50, v=4.18, g=9.8)
# caculate(theta=20, h2=7.87, v=2.93, g=9.8)
# caculate(theta=35, h2=13.19, v=2.93, g=9.8)
# caculate(theta=25, h2=9.72, v=4.18, g=9.8)
# caculate(theta=40, h2=14.78, v=4.18, g=9.8)
# caculate(theta=20, h2=7.87, v=4.18, g=9.8)
# caculate(theta=25, h2=9.72, v=3.13, g=9.8)
# caculate(theta=40, h2=14.78, v=3.13, g=9.8)
# caculate(theta=30, h2=11.50, v=3.13, g=9.8)
# caculate(theta=25, h2=9.72, v=2.93, g=9.8)
# caculate(theta=35, h2=13.19, v=3.13, g=9.8)
caculate2(theta=15, h2=5.95, h4=3.7, v=4.18, g=9.8)
caculate2(theta=20, h2=7.87, h4=3.4,v=3.13, g=9.8)
caculate2(theta=30, h2=11.50,h4=1.6, v=2.93, g=9.8)
