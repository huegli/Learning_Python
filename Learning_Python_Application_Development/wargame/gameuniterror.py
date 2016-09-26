class GameUnitError(Exception):
    """Custom exceptions class for the 'AbstractGameUnit' and its subclasses"""
    def __init__(self, message=''):
        Exception.__init__(self, message)
        self.padding = '~'*50 + '\n'
        self.error_message = " Unspecified Error!"

class HealthMeterException(GameUnitError):
    def __init__(self, message = ''):
        GameUnitError.__init__(self, message)
        self.error_message = (self.padding +
                "ERROR: Health Meter Problem" +
                '\n' + self.padding )
