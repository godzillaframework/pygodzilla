class GodzillaException(Exception):
    pass

class MethodNotFoundException(Exception):
    pass

class TimeoutException(GodzillaException):
    pass

class ConnectionException(GodzillaException):
    pass