class Branch:
    def __init__(self, fbus, tbus, r, x, b, rateA, rateB, rateC, ratio, angle, status, angmin, angmax):
        self.fbus = fbus
        self.tbus = tbus
        self.r = r
        self.x = x
        self.b = b
        self.rateA = rateA
        self.rateB = rateB
        self.rateC = rateC
        self.ratio = ratio
        self.angle = angle
        self.status = status
        self.angmin = angmin
        self.angmax = angmax

    def __str__(self):
        return "\t".join(map(str, [
            self.fbus, self.tbus, self.r, self.x, self.b, self.rateA, self.rateB,
            self.rateC, self.ratio, self.angle, self.status, self.angmin, self.angmax
        ]))
