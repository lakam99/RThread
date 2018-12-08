from threading import Thread


class RThread(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, daemon=None):
        Thread.__init__(self, group, target, name, args, kwargs, daemon=daemon)
        self._return = None

    def run(self):
        self._return = self._target(*self._args, **self._kwargs)

    def join(self, timeout=None):
        Thread.join(self, timeout=timeout)
        return self._return

class Holder:
    def __init__(self, data=[], self_reset=True, default_value=None):
        self._data = data
        self.__data = data
        self._complete = False
        self._self_reset_enabled = self_reset
        self._default_value = default_value

    def next(self):
        if len(self._data) != 0:
            r = self._data.pop(0)
            if not self._data and self._self_reset_enabled:
                self.reset()
            return r
        else:
            self._complete = True
            if self._self_reset_enabled:
                self.reset()
            else:
                return self._default_value


    def re_init(self, data=[]):
        self.__init__(data=data)

    def reset(self):
        self._data = self.__data
        self._complete = False

    def is_complete(self):
        return self._complete == True

    def is_not_complete(self):
        return self._complete == False

