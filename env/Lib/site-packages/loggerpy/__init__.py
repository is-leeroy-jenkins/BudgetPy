from enum import Enum

from loggerpy.colors import colors

__all__ = ['Level', 'Logger']


class Level(Enum):
    """
    Useful class that collects all the possible levels
    NO_LOGGER: str
        Neither printing nor saving
    DEBUG: str
    INFO: str
    WARNING: str
    ERROR: str
    CRITICAL: str
    """
    NO_LOGGER = 'NO LOGGER'
    DEBUG = 'DEBUG'
    INFO = 'INFO'
    WARNING = 'WARNING'
    ERROR = 'ERROR'
    CRITICAL = 'CRITICAL'


from loggerpy.logger_exception import LoggerLevelException, LoggerNameException


class _Level(Enum):
    NO_LOGGER = (Level.NO_LOGGER, colors.get_color(), 5)
    DEBUG = (Level.DEBUG, colors.get_color(fg=colors.fg.blue), 0)
    INFO = (Level.INFO, colors.get_color(fg=colors.fg.lightgreen), 1)
    WARNING = (Level.WARNING, colors.get_color(fg=colors.fg.yellow, type=colors.bold), 2)
    ERROR = (Level.ERROR, colors.get_color(fg=colors.fg.red), 3)
    CRITICAL = (Level.CRITICAL, colors.get_color(bg=colors.bg.red), 4)

    def __init__(self, level_type: Level, color: str, level: int):
        self.level_type = level_type
        self.color = color
        self.level = level

    def __str__(self) -> str:
        return str(self.level_type.value)

    @staticmethod
    def get_level(level: Level):
        for enum_level in _Level:
            if enum_level.level_type == level:
                return enum_level
        raise LoggerLevelException(level)


class Logger:
    lock_print = False
    lock_save = False

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Logger, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.__name = None
        self.__log_folder = None
        self.__print_level: _Level = _Level.INFO
        self.__save_level: _Level = _Level.NO_LOGGER

    def configure(self, name=None, log_folder=None, print_level=None, save_level=None):
        if name is not None:
            self.name = name
        if log_folder is not None:
            self.folder = log_folder
        if print_level is not None:
            self.print_level = print_level
        if save_level is not None:
            self.save_level = save_level

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if not isinstance(name, str):
            raise TypeError("The name has to be a string")
        self.__name = name.upper()

    @property
    def folder(self):
        return self.__log_folder

    @folder.setter
    def folder(self, folder_path: str):
        import os
        if not isinstance(folder_path, str):
            raise TypeError("The folder path has to be a string")

        path = os.path.abspath(folder_path)
        if os.path.exists(path) and not os.path.isdir(path):
            raise ValueError("The specified path is not a directory")

        if os.path.exists(path):
            folder_name = os.path.basename(path)
            if folder_name != 'logs':
                path = os.path.join(path, 'logs')
                os.makedirs(path, exist_ok=True)
        else:
            path = os.path.join(path, 'logs')
            os.makedirs(path)

        self.__log_folder = path

    @property
    def print_level(self):
        return str(self.__print_level)

    @print_level.setter
    def print_level(self, level: Level):
        self.__print_level = _Level.get_level(level)

    @property
    def save_level(self):
        return str(self.__save_level)

    @save_level.setter
    def save_level(self, level: Level):
        self.__save_level = _Level.get_level(level)

    def info(self, *args, source: str = None):
        """
        Print an _info_ log
        :param source: the piece of code from the log came from
        :type source: str
        :param args: body
        :type args: list, str
        """
        text = ' '.join([str(arg) for arg in args])
        self.__log(_Level.INFO, source, text)

    def error(self, *args, source: str = None):
        """
        Print an _error_ log
        :param source: the piece of code from the log came from
        :type source: str
        :param args: body
        :type args: list, str
        """
        text = ' '.join([str(arg) for arg in args])
        self.__log(_Level.ERROR, source, text)

    def critical(self, *args, source: str = None):
        """
        Print an _critical_ log
        :param source: the piece of code from the log came from
        :type source: str
        :param args: body
        :type args: list, str
        """
        text = ' '.join([str(arg) for arg in args])
        self.__log(_Level.CRITICAL, source, text)

    def debug(self, *args, source: str = None):
        """
        Print an _debug_ log
        :param source: the piece of code from the log came from
        :type source: str
        :param args: body
        :type args: list, str
        """
        text = ' '.join([str(arg) for arg in args])
        self.__log(_Level.DEBUG, source, text)

    def warning(self, *args, source: str = None):
        """
        Print an _warning_ log
        :param source: the piece of code from the log came from
        :type source: str
        :param args: body
        :type args: list, str
        """
        text = ' '.join([str(arg) for arg in args])
        self.__log(_Level.WARNING, source, text)

    def __log(self, level: _Level, source: str, text: str):
        """
        This hidden method prepares the setting to print and save the log, depending on the chosen level
        :param level: level of printing and saving log
        :type level: _Level
        :param source: the piece of code from the log came from
        :type source: str
        :param text: body of printing or saving log
        :type text: str
        """
        if self.name is None:
            raise LoggerNameException("Set the _name_ variable")

        s = self.__formatter(level, source, text)

        if self.__print_level.level <= level.level:
            string = colors.start + level.color + s + colors.stop
            Logger.__print_log(string)

        if self.__save_level.level <= level.level:
            if self.__log_folder is None:
                # TODO trovare un path
                raise Warning("Set the _folder_ variable in order to save the log")
            else:
                Logger.__save_log(s, self.__log_folder)

    def __formatter(self, level: _Level, source: str, text: str):
        """
        Depends on the level, formats the logging string
        :param level: level of logging
        :type level: str
        :param source: the piece of code from the log came from
        :type source: str
        :param text: body of logging
        :type text: str
        :return: completed string, composed by: timestamp + domain of logger + name of logger + logging message
        :rtype: str
        """
        from datetime import datetime
        time = datetime.now().strftime("%y-%b-%d %H:%M:%S.%f")

        if source is None:
            name = self.name
        else:
            name = f"{self.name}/{source.upper()}"

        if len(name) > 30:
            name = '...' + name[-27:]
        return f'{time} | {level:<8} | {name:<30} | {text:<80}'

    @staticmethod
    def __save_log(text, path):
        """
        This method saves the log given as input in the specified path
        :param text: log message
        :type text: str
        :param path: path of the folder in which save logs
        :type path: str
        """
        text = text + '\n'
        from datetime import datetime
        import os

        time = datetime.now().strftime('%Y-%m-%d')
        file_name = f'{time}.log'
        path = os.path.join(path, file_name)

        with open(path, 'a') as file:
            file.write(text)

    @staticmethod
    def __print_log(text):
        """
        This method print the log on the stdout. It is developed for multi threads logging
        :param text: log message
        :type text: str
        """
        while Logger.lock_print:
            pass
        Logger.lock_print = True
        print(text)
        Logger.lock_print = False
