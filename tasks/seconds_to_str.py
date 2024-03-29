__all__ = ("seconds_to_str",)

import time


def seconds_to_str(seconds: int) -> str:
    time_convert = time.strftime("%Dd%Hh%Mm%Ss", time.gmtime(seconds))
    print(time_convert)
    raise NotImplementedError
