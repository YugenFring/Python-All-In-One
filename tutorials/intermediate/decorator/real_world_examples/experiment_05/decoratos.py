import functools

def validate_json(*expected_args):
    def decorator_validate_json(func):
        @functools.wraps(func)
        def wrapper_validate_json(*args, **kwargs):
            """Validate if the target json object exists"""
            json_object = request.get_json()
            for expected_arg in expected_args:
                if expected_arg not in json_object:
                    return Exception
                return func(*args, **kwargs)
            return wrapper_validate_json
    return decorator_validate_json