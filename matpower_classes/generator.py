class Generator:
    def __init__(self, bus, Pg, Qg, Qmax, Qmin, Vg, mBase, status, Pmax, Pmin, Pc1=0, Pc2=0, Qc1min=0, Qc1max=0, Qc2min=0, Qc2max=0, ramp_agc=0, ramp_10=0, ramp_30=0, ramp_q=0, apf=0):
        self.bus = bus
        self.Pg = Pg
        self.Qg = Qg
        self.Qmax = Qmax
        self.Qmin = Qmin
        self.Vg = Vg
        self.mBase = mBase
        self.status = status
        self.Pmax = Pmax
        self.Pmin = Pmin
        self.Pc1 = Pc1
        self.Pc2 = Pc2
        self.Qc1min = Qc1min
        self.Qc1max = Qc1max
        self.Qc2min = Qc2min
        self.Qc2max = Qc2max
        self.ramp_agc = ramp_agc
        self.ramp_10 = ramp_10
        self.ramp_30 = ramp_30
        self.ramp_q = ramp_q
        self.apf = apf

    def __str__(self):
        return "\t".join(map(str, [
            self.bus, self.Pg, self.Qg, self.Qmax, self.Qmin, self.Vg, self.mBase,
            self.status, self.Pmax, self.Pmin, self.Pc1, self.Pc2, self.Qc1min, self.Qc1max,
            self.Qc2min, self.Qc2max, self.ramp_agc, self.ramp_10, self.ramp_30, self.ramp_q, self.apf
        ]))
