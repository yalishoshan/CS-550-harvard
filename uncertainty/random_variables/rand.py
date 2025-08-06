class Probability:
    def __init__(self, flight):
        self.flight = flight

    def on_time(self):
        return f"{self.flight} = on time = 0.6"

    def delay(self):
        return f"{self.flight} = delay = 0.3"

    def cancel(self):
        return f"{self.flight} = cancel = 0.1"

    def probability_distribution(self):
        return f"{self.on_time()}, {self.delay()}, {self.cancel()}"

    def independence(self):
        # p(a and b) = p(a) * p(b)
        return f"{self.flight} = independence = 0.6 * 0.3 = 0.18"