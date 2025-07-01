import yaml
import inspect
import datetime
import os

class Logger:
    def __init__(self):
        with open("configuration.yaml", 'r') as file:
            data = yaml.safe_load(file)
            
            if data['Logger']['type'] not in ['file', 'console']:
                self.log_type = 'console'
            else: self.log_type = data['Logger']['type']
            
            self.log_file = data['Logger']['file_name']
            
            self.log_level = min(3, data['Logger']['level'])

            if self.log_type == 'file':
                with open(self.log_file, 'w') as file:
                    pass

    # project : date : time : file_name : level : message 
    def __log_str(self, level, message):
        return f"Project - {datetime.datetime.now()} - {os.path.basename(inspect.stack()[3].filename)} - {level} - {message}"
    
    def __log(self, level, message):

        s = self.__log_str(level, message)

        if self.log_type == 'console':
            print(s)
        else:
            with open(self.log_file, 'a') as file:
                file.write(s + '\n')

    def error(self, message):
        if self.log_level >= 1:
            self.__log("ERROR", message)
    
    def info(self, message):
        if self.log_level >= 2:
            self.__log("INFO", message)
    
    def debug(self, message):
        if self.log_level >= 3:
            self.__log("DEBUG", message)
        
log = Logger()