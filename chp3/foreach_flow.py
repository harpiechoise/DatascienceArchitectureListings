from metaflow import FlowSpec, step


class ForEachFlow(FlowSpec):

    @step
    def start(self):
        """Defines creatures and excecutes a dynamic flow
        """
        self.creatures = ['bird', 'mouse', 'dog']
        # Creatures key is readed from the class properties
        self.next(self.analyze_creatures, foreach='creatures')

    @step
    def analyze_creatures(self):
        """Scores and analyses every creature on the `self.creature`
        key
        """
        # Input points to foreach list
        print("Analyzing", self.input)
        self.creature = self.input
        self.score = len(self.creature)
        self.next(self.join)

    @step
    def join(self, inputs):
        """Evaluates the creatures and choose the best to store
        them into `self.creatures` property

        Args:
            inputs (metaflow.datastore.inputs.Input): Output from the prior step
        """
        self.best = max(inputs, key=lambda x: x.score).creature
        self.next(self.end)

    @step
    def end(self):
        """Displays `self.best` class property
        """
        print(self.best, 'Won!')


if __name__ == '__main__':
    ForEachFlow()
