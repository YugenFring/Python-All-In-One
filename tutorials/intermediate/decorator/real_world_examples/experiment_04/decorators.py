def set_unit(unit):
    """Register a unit on a func"""
    def decorator_set_unit(func):
        func.unit = unit
        return func
    return decorator_set_unit