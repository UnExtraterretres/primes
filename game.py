class Game:

    def __init__(self, file_path="primes.txt", condition="True"):
        # load arguments
        self.file_path = file_path
        self.condition = condition

        # boolean states of the game
        self.states = {
            "running": True
        }

        # to load the series
        try:
            self.primes = [int(i) for i in open(self.file_path, "r").read().split(",")]
        except FileNotFoundError:
            self.primes = [2]
            open(self.file_path, "w").write("2")

        # initialize n
        self.n = self.primes[-1]

    def handling_events(self):
        pass

    def update(self):
        if eval(self.condition):
            if self.n % 2 == 0:
                self.n += 1
            else:
                self.n += 2

            is_prime = True
            for q in self.primes:
                if self.n % q == 0:
                    is_prime = False
                    break
            if is_prime:
                self.primes.append(self.n)
                open(self.file_path, "a").write(f",{self.n}")
        else:
            self.states["running"] = False

    def display(self):
        pass

    def run(self):
        # game LOOP
        while self.states["running"]:
            # check events
            self.handling_events()
            # logic of the game
            self.update()
            # displays
            self.display()
