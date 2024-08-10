class GeneratorCost:
    def __init__(self, model, startup, shutdown, n, *coefficients):
        self.model = model
        self.startup = startup
        self.shutdown = shutdown
        self.n = n
        self.coefficients = coefficients

    def __str__(self):
        return "\t".join(map(str, [
            self.model, self.startup, self.shutdown, self.n, *self.coefficients
        ]))
