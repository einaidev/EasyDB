def Mode(mode,json_):
    def wrapper(f):
        if not mode in json_:
            json_[mode] = [{"name":f.__code__.co_name,"function":f}]
        else:
            json_[mode].append({"name":f.__code__.co_name,"function":f})
    return wrapper