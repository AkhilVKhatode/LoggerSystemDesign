# LoggerSystemDesign - Chain of Responsibility Logger System

This project implements a logging system using the **Chain of Responsibility** design pattern in Python.

## 🧩 Overview

The Chain of Responsibility pattern allows you to pass requests along a chain of handlers. Each handler decides either to process the request or to pass it along to the next handler in the chain. This approach promotes loose coupling and flexibility in the system.

In this implementation, the logging mechanism is designed to handle messages at different levels: `DEBUG`, `INFO`, and `ERROR`. Each logger handles messages at or above its designated level and can pass them down the chain.

## 🧪 Features

- Chainable loggers with different output mediums:
  - `ConsoleLogger`: Prints messages to the console.
  - `FileLogger`: Writes messages to a file.
  - `ErrorLogger`: Prints error messages to the console (can be extended for stderr or monitoring tools).
- Extensible logging levels.
- Flexible logger pipeline configuration.

## 🛠️ Usage

```
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

Console::Logger: This is an information.
File::Logger: This is an information.
Console::Logger: This is a debug level information.
Console::Logger: This is an error information.
File::Logger: This is an error information.
Error::Logger: This is an error information.
```
