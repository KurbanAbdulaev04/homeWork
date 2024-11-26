def introspection_info(obj):
    dict_info = {'type': type(obj).__name__,
                 'attributes': obj.__class__.__dict__,
                 'methods': [i for i in dir(obj) if callable(getattr(obj, i))],
                 'module': __name__,
                 'id': id(obj)
                 }
    return dict_info


number_info = introspection_info(42)
print(number_info)