import abc

class AbstractLogger(abc.ABC):
    def __init__(self, level):
        self.level = level
        self.next_logger = None

    def set_next_logger(self, next_logger):
        self.next_logger = next_logger
        return next_logger

    def log_message(self, level, message):
        if self.level <= level:
            self.write(message)
        if self.next_logger:
            self.next_logger.log_message(level, message)

    @abc.abstractmethod
    def write(self, message):
        pass

class ConsoleLogger(AbstractLogger):
    def __init__(self, level):
        super().__init__(level)

    def write(self, message):
        print(f"Console::Logger: {message}")

class FileLogger(AbstractLogger):
    def __init__(self, level, filename):
        super().__init__(level)
        self.filename = filename

    def write(self, message):
        with open(self.filename, "a") as f:
            f.write(f"File::Logger: {message}\n")

class ErrorLogger(AbstractLogger):
    def __init__(self, level):
        super().__init__(level)

    def write(self, message):
        print(f"Error::Logger: {message}")

DEBUG = 1
INFO = 2
ERROR = 3

console_logger = ConsoleLogger(DEBUG)
file_logger = FileLogger(INFO, "log.txt")
error_logger = ErrorLogger(ERROR)

console_logger.set_next_logger(file_logger).set_next_logger(error_logger)

console_logger.log_message(INFO, "This is an information.")
console_logger.log_message(DEBUG, "This is a debug level information.")
console_logger.log_message(ERROR, "This is an error information.")
