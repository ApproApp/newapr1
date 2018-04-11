from loginReg.models import User

def is_Executive(function):
    def wrap(request, *args, **kwargs):
        if request.User.rio == "Executive":
            return function(request, *args, **kwargs)
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def is_Admin(function):
    def wrap(request, *args, **kwargs):
        if request.User.rio == "Admin":
            return function(request, *args, **kwargs)
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def is_Student(function):
    def wrap(request, *args, **kwargs):
        if request.User.rio == "Student":
            return function(request, *args, **kwargs)
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap