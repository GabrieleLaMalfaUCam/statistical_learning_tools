import pandas as pd
import os
from sklearn import linear_model
from sklearn.model_selection import train_test_split
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
        self.x_train = None
        self.x_test = None
        self.y_train = None
        self.y_test = None
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
        x = self.df[0][index_name]
        self.df[0]['sequence'] = pd.Series(range(len(self.df[0])))
        y = self.df[0]['sequence']
        self.x_train, self.x_test, self.y_train, self.y_test = \
            train_test_split(x, y, test_size= 1 - train_percentage)

        return None

    def simple_linear_regression(self):
        self.x_train = self.x_train.values.reshape(-1, 1)
        self.x_test = self.x_test.values.reshape(-1, 1)
        self.y_train = self.y_train.values.reshape(-1, 1)
        self.y_test = self.y_test.values.reshape(-1, 1)
        regr = linear_model.LinearRegression()
        regr.fit(self.x_train, self.y_train)
        self.prediction = regr.predict(self.x_test)

        print('Coefficients: \n', regr.coef_)
        # The mean squared error
        print('Mean squared error: %.2f'
              % mean_squared_error(self.y_test.reshape(-1, 1), self.prediction))
        print('Coefficient of determination: %.2f'
              % r2_score(self.y_test.reshape(-1, 1), self.prediction))

        plt.scatter(self.x_test, self.y_test, color='black')
        plt.plot(self.x_test, self.prediction, color='blue', linewidth=3)
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
input.simple_linear_regression()
print('end')
