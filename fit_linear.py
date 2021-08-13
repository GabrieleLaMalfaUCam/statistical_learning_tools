import pandas as pd
import os
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt


class LinearRegressionFit:
    def __init__(self):
        super().__init__()

        self.upload_folder = None  # 'statistical_learning_tools'
        self.upload_files = None  # 'FTSE100_financial_crisis_2007'
        self.setup_sheet_name = None  # 'Values_FTSE_100'
        self.msg = None
        self.df = []
        self.file = None
        self.train_share = None
        self.test_share = None
        self.train_set_x = None
        self.train_set_y = None
        self.test_set = None
        self.test_set_x = None
        self.test_set_y = None
        self.prediction = None

    def process_inputs(self, upload_folder, upload_files, setup_sheet_name):
        try:
            self.read_file(upload_folder, upload_files, setup_sheet_name)
        except Exception as e:
            self.msg = 'Input file cannot be processed: ' + str(e)

        return self.msg

    def read_file(self, upload_folder, upload_files, setup_sheet_name):
        self.file = os.path.join(upload_folder, upload_files)
        self.df.append(pd.read_excel(self.file, setup_sheet_name))

        return None

    def train_test_sets(self, index_name, train_percentage):
        seq_train = pd.DataFrame()
        seq_test = pd.DataFrame()
        self.train_share = int(len(self.df[0]) * train_percentage + 1)
        self.test_share = int(len(self.df[0]) * (1-train_percentage))
        seq_train['sequence_train'] = pd.Series(range(self.train_share))
        seq_test['sequence_test'] = pd.Series(range(self.test_share))

        self.train_set_x = seq_train['sequence_train'].values.reshape(-1, 1)
        self.train_set_y = self.df[0][index_name][:self.train_share].values.reshape(-1, 1)
        self.test_set_x = seq_test['sequence_test'].values.reshape(-1, 1)
        self.test_set_y = self.df[0][index_name][self.train_share:].values.reshape(-1, 1)

        return None


    def linear_regression(self):
        regr = linear_model.LinearRegression()
        regr.fit(self.train_set_x, self.train_set_y)
        self.prediction = regr.predict(self.test_set_x)

        print('Coefficients: \n', regr.coef_)
        # The mean squared error
        print('Mean squared error: %.2f'
              % mean_squared_error(self.test_set_y, self.prediction))
        print('Coefficient of determination: %.2f'
              % r2_score(self.test_set_y, self.prediction))

        plt.scatter(self.test_set_x, self.test_set_y, color='black')
        plt.plot(self.test_set_x, self.prediction, color='blue', linewidth=3)
        plt.xticks(())
        plt.yticks(())
        plt.show()

        return None



input = LinearRegressionFit()
upload_folder = os.getcwd() + '\\input_files'
upload_files = r'FTSE100_financial_crisis_2007.xlsx'
sheet_name = 'Values_FTSE_100'
input.read_file(upload_folder, upload_files, sheet_name)
path = os.getcwd()
print(path)
input.train_test_sets('FTSE_100', 0.8)
input.linear_regression()
print('end')
