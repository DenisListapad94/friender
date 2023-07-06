from .models import PlaceQueue

class Queue:

    FIFO = "FIFO"
    LIFO = "LIFO"
    STRATEGIES = [FIFO] #, LIFO]

    def __init__(self, strategy):
        if strategy not in self.STRATEGIES:
            raise ValueError(f' {strategy} not in supported strategies: {self.STRATEGIES}')
        self.storage = []
        self.strategy = strategy

    def add(self, value):
        PlaceQueue.objects.create(value=value)
    def pop(self):
        val = None
        if self.strategy == self.FIFO:
            val = PlaceQueue.objects.order_by("id").first()

        elif self.strategy == self.LIFO:
            val = PlaceQueue.objects.order_by("id").last()
        if val:
            val.delete()
            return val.value
        return None
