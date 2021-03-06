# Copyright 2017, Inderpreet Singh, All rights reserved.


class AppError(Exception):
    """
    Exception indicating an error
    """
    pass


class ServiceExit(AppError):
    """
    Custom exception which is used to trigger the clean exit
    of all running threads and the main program.
    """
    pass


class ServiceRestart(AppError):
    """
    Exception indicating a restart is requested
    """
    pass
