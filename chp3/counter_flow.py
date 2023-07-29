"""CounterFlow listing from the book Effective DataScience Infrastructure
"""
from metaflow import FlowSpec, step


class CounterFlow(FlowSpec):
    """Example flow with a simple counter to interact with datastore

    Args:
        FlowSpec (FlowSpec): Is the flow wich all flow classes should inherit
    """
    @step
    def start(self):
        """Entry point, sets counter to zero
        """
        self.counter = 0  # Initalizes the count to zero
        self.next(self.add)

    @step
    def add(self):
        """Increments the count by one
        """
        self.counter += 1  # Increments the count by one
        self.next(self.end)

    @step
    def end(self):
        """Workflow end, and prints the counter result
        """
        print("The final count is %d" % self.counter)  # Shows the final count


if __name__ == '__main__':
    CounterFlow()
