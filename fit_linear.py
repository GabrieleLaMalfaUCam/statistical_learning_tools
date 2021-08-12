import pandas as pd
import os


class LinearRegressionFit:
    def __init__(self):
        super().__init__()

        self.upload_folder = None  # 'statistical_learning_tools'
        self.upload_files = None  # 'FTSE100_financial_crisis_2007'
        self.setup_sheet_name = None  # 'Values_FTSE_100'
        self.msg = None
        self.df = None
        self.file = None

    def process_inputs(self, upload_folder, upload_files, setup_sheet_name):
        try:
            self.read_file(upload_folder, upload_files, setup_sheet_name)
        except Exception as e:
            self.msg = 'Input file cannot be processed: ' + str(e)

        return self.msg

    def read_file(self, upload_folder, upload_files, setup_sheet_name):
        self.file = os.path.join(upload_folder, upload_files)
        self.df = pd.read_excel(self.file, setup_sheet_name)

        return None


input = LinearRegressionFit()
upload_folder = os.getcwd() + '\\input_files'
upload_files = r'FTSE100_financial_crisis_2007.xlsx'
sheet_name = 'Values_FTSE_100'
input.read_file(upload_folder, upload_files, sheet_name)
path = os.getcwd()
print(path)
print('end')
