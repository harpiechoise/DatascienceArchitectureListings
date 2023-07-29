"""Metaflow file parameter
"""
import csv
from io import StringIO
from metaflow import FlowSpec, Parameter, step, IncludeFile


class CSVFileFlow(FlowSpec):
    """Flow to read simple csv file

    Args:
        FlowSpec (Flowspec): Superclass for all flow types
    """
    # Include file persist as a metaflow artifact
    data = IncludeFile('csv', help='CSV file to be parsed', is_text=True)

    delimiter = Parameter(
        'delimiter', help='Row delimiter of the input csv', default=',')

    @step
    def start(self):
        """Read csv and display row numbers and row contents
        """
        fileobj = StringIO(self.data)
        for i, row in enumerate(csv.reader(fileobj, delimiter=self.delimiter)):
            print(f'Row {i}: {row}')

        self.next(self.end)

    @step
    def end(self):
        """Display 'Done' in the console
        """
        print('Done!')


if __name__ == '__main__':
    CSVFileFlow()
