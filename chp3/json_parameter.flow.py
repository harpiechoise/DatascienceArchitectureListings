from metaflow import FlowSpec, step, Parameter, JSONType


class JsonParameterFlow(FlowSpec):
    """Flow that accepts a json type parameter

    Args:
        FlowSpec (FlowSpec): Superclass for all flows
    """
    mapping = Parameter('mapping', help='Specify a mapping',
                        default={'some': 'default'}, type=JSONType)

    @step
    def start(self):
        """Read the 'mapping' parameter and display
        key and value
        """
        for key, value in self.mapping.items():
            print(f'{key}:{value}')
        self.next(self.end)

    @step
    def end(self):
        """End of the metaflow's flow.
        """
        print('Done!')


if __name__ == "__main__":
    JsonParameterFlow()
