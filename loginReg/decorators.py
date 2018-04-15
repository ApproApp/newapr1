from loginReg.models import User
from django.core.exceptions import PermissionDenied

def is_Executive(function):
    def wrap(request, *args, **kwargs):
        if request.User.rio == "executive":
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def is_Admin(function):
    def wrap(request, *args, **kwargs):
        if request.User.rio == "admin":
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def is_Applicant(function):
    def wrap(request, *args, **kwargs):
        if request.User.rio == "student":
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
