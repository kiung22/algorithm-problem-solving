def checkio(data):
    data = list(filter(lambda x: x.isdigit(), list(data)))

    for i, n in enumerate(data):
        data[i] = int(n)

    x1, y1, x2, y2, x3, y3 = data

    import numpy as np
    import numpy.linalg as la

    A = np.array([[x1, y1, 1],[x2, y2, 1],[x3, y3, 1]])
    B = np.array([[-(x1**2)-(y1**2)],[-(x2**2)-(y2**2)],[-(x3**2)-(y3**2)]])
    C = la.solve(A, B)

    x0 = '%g'%round(float(-C[0]/2), 2)
    y0 = '%g'%round(float(-C[1]/2), 2)
    r = '%g'%round(float((C[0]**2 + C[1]**2 - 4*C[2])**0.5/2), 2)
    return "(x-{})^2+(y-{})^2={}^2".format(x0, y0, r)
