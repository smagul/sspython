class PulicPrivateExample:
    def __init__(self):
        self.public = "safe"
        self._unsafe = "unsafe"

    def public_method(self):
        # clients can use this
        pass

    def _unsafe_method(self):
        # clients can't use this
        pass
        self.public = "safe"
        sefl._unsafe = "unsafe"
