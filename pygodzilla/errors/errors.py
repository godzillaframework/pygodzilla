class GodzillaException(Exception):
    pass


class MethodNotFoundException(GodzillaException):
    pass


class TimeoutException(GodzillaException):
    pass


class ConnectionException(GodzillaException):
    pass


class RemoteException(Exception):
    pass