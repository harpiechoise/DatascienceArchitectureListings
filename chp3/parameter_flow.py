from metaflow import FlowSpec, Parameter, step


class ParameterFlow(FlowSpec):
    """Flow with parameters

    Args:
        FlowSpec (FlowSpec): Base class for flows
    """

    animal = Parameter('creature', help='Specify an animal', required=True)
    count = Parameter('count', help='Number of animals', default=1)
    ratio = Parameter('ratio', help='Ratio between 0.0 and 1.1', type=float)

    @step
    def start(self):
        """Shows the animals in the logs
        """
        print(self.animal, 'Is a string of:', len(self.animal), 'characters')
        print(f'Count is an integer: {self.count}+1={self.count+1}')
        print('Ratio is a', type(self.ratio), 'and whose value is', self.ratio)
        self.next(self.end)

    @step
    def end(self):
        """Ends the workflow
        """
        print('Done!')


if __name__ == '__main__':
    ParameterFlow()
