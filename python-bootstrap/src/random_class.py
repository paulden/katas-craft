import os


class RandomClass:

    def __init__(self, parameter=1):
        self.parameter = parameter

    def multiply_parameter(self):
        self.parameter *= 2
        return self.parameter

    def retrieve_environment_variable(self, variable):
        return os.getenv(variable)
