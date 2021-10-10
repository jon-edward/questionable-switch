class UndefinedCasesError(Exception):
    """When an out value is attempted to be accessed before cases are defined."""
    pass


class CaseDoesNotExistError(Exception):
    """When a path for a case does not exist, but it is attempted to be used."""
    pass
