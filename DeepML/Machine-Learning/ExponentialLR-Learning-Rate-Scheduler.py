class ExponentialLRScheduler:
    def __init__(self, initial_lr, gamma):
        # Initialize initial_lr and gamma
        self.initial_lr=initial_lr
        self.gamma=gamma

    def get_lr(self, epoch):
        # Calculate and return the learning rate for the given epoch
        lr=self.initial_lr*self.gamma**epoch
        lr=round(lr, 4)
        return lr