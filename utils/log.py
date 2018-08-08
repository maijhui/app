import logging
from logging.handlers import TimedRotatingFileHandler
from utils.yaml_reader import YamlReader

class Log():
    def __init__(self,log_path="C:\\Users\\Administrator\\Desktop\\test_log.txt",
                 backup_count=5,
                 console_output_level="WARNING",
                 file_output_level="DEBUG",
                 pattern='%(asctime)s - %(name)s - %(levelname)s - %(message)s'):

        self.logger = logging.getLogger("framework") #实例化一个叫framework的log
        logging.root.setLevel(logging.NOTSET)  #先不设置级别
        self.log_path=log_path
        self.backup_count=backup_count  #备份数
        self.console_output_level=console_output_level  #控制台输出级别
        self.file_output_level=file_output_level  #文件输出级别
        self.formatter=logging.Formatter(pattern)  #日志输出格式

    def log_input(self):
        #console
        console=logging.StreamHandler()
        console.setFormatter(self.formatter)
        console.setLevel(self.console_output_level)
        self.logger.addHandler(console)

        #file
        file=TimedRotatingFileHandler(filename=self.log_path,  #传参
                                 when="D",
                                 interval=1,
                                 backupCount=5,
                                 delay=True,
                                 encoding="utf-8")
        file.setFormatter(self.formatter)  #格式
        file.setLevel(self.file_output_level)  #级别
        self.logger.addHandler(file)

        return self.logger

logger=Log().log_input()