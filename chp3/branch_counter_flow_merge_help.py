from metaflow import FlowSpec, step


class CounterBranchFlow(FlowSpec):
    """A flow with a split banching

    Args:
        FlowSpec (FlowSpec): Is the superclass for all flows
    """
    @step
    def start(self):
        """Defines 'creature' and 'count' variables and split the flow
        """
        self.creature = 'dog'
        self.count = 0
        self.next(self.add_one, self.add_two)

    @step
    def add_one(self):
        """Adds one the the count
        """
        self.count += 1
        self.next(self.join)

    @step
    def add_two(self):
        """Adds two to the count
        """
        self.count += 2
        self.next(self.join)

    @step
    def join(self, inputs):
        """Recieves the input from the merging, and joins the two prior steps

        Args:
            inputs (metaflow.datastore.inputs.Inputs): Is the object that stores the prior steps outputs
        """
        self.count = max(inp.count for inp in inputs)
        print('Count from add_one', inputs.add_one.count)
        print('Count from add_two', inputs.add_two.count)
        # Excluding creature from self
        self.merge_artifacts(inputs, exclude=['creature'])
        self.next(self.end)

    @step
    def end(self):
        """End of the workflow
        """
        # print('The creature is', self.creature)
        print('The final count is', self.count)


if __name__ == '__main__':
    CounterBranchFlow()
