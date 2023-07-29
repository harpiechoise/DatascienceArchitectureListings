"""First flow in the book Effective DataScience Infrastructure
"""
from metaflow import FlowSpec, step

# The workflow is defined by subclassing from flowspec


class HelloWorldFlow(FlowSpec):
    """Is a example flow to make a hello world with metaflow

    Args:
        FlowSpec (FlowSpec): Main class from which all flows inherits
    """
    @step  # Step decorator denotes a flow step
    def start(self):  # the entry point of the flow must be called start
        """Flow starting point"""
        print("This is the starting step")
        self.next(self.hello)  # Next denotes an edge in the workflow

    # _________    _________
    # |       |    |       |
    # | START | -> | HELLO |
    # |_______|    |_______|

    @step
    def hello(self):
        """Just say hello world"""
        print("Hello World")
        self.next(self.end)

    # _________    _________     _______
    # |       |    |       |    |       |
    # | START | -> | HELLO | -> |  END  |
    # |_______|    |_______|    |_______|

    @step
    def end(self):
        """Ending point of the flow"""
        print("Flows end")  # End of the flow


if __name__ == '__main__':
    HelloWorldFlow()  # Instantiating the workflow allows it to be excecuted
