from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(func):
    def wrapper_func(req, *args, **kwargs):
        if req.user.is_authenticated:
            return redirect('products')
        else:
            return func(req, *args, **kwargs)
    
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(func):
        def wrapper_func(req, *args, **kwargs):
            
            group = None
            if req.user.groups.exists():
                group = req.user.groups.all()[0].name
                
            if group in allowed_roles:
                return func(req, *args, **kwargs)
            else:
                return HttpResponse('You are no authorized to view this page')
        return wrapper_func
    return decorator


def adminonly(func):
    def wrapper_func(req, *args, **kwargs):
        group = None
        if req.user.groups.exists():
            group = req.user.groups.all()[0].name
            
        if group == 'customer':
            return redirect('products')
        
        if group == 'business':
            return func(req, *args, **kwargs)
    
    return wrapper_func