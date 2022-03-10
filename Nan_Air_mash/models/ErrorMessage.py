class ErrorMessage:
    def __init__(self, errorID, error_message, python_error) -> None:
        self.errorID = errorID #not a ID class just its identifigin number
        self.error_message = error_message
        self.python_error = python_error
    
    def __str__(self) -> str:
        return str(self.errorID)+" ," + str(self.error_message)+" ," + str(self.python_error)
