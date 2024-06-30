def mdw(next_mdw):
    def mdw(request, *args, **kwargs):
        print("I'm a middleware")
        return next_mdw(request, *args, **kwargs)
    return mdw
