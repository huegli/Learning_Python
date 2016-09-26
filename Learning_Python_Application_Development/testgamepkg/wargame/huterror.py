class HutError(Exception):
    """Custom exceptions class for the 'Hut' and its subclasses"""
    def __init__(self, message=''):
        Exception.__init__(self, message)
        self.padding = '~'*50 + '\n'
        self.error_message = " Unspecified Error!"

class HutNumberGreaterThanFiveError(HutError):
    def __init__(self, message = ''):
        HutError.__init__(self, message)
        self.error_message = (self.padding +
                "ERROR: Hut Number is greater than 5" +
                '\n' + self.padding )

class NegativeHutNumberError(HutError):
    def __init__(self, message = ''):
        HutError.__init__(self, message)
        self.error_message = (self.padding +
                "ERROR: Hut Number has to be greater than 0" +
                '\n' + self.padding )
