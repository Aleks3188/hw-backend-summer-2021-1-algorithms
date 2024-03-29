__all__ = ("seconds_to_str",)

def seconds_to_str(seconds: int) -> str:
    days_value = seconds // (24 * 60 * 60)
    seconds -= days_value * (24 * 60 * 60)
    hours = seconds // (60 * 60)
    seconds -= hours * (60 * 60)
    minutes = seconds // 60
    seconds -= minutes * 60
    result = []
    if days_value > 0:
        result.append(f'{"%02d" % (days_value)}d')
    if hours > 0 or result:
        result.append(f'{"%02d" % (hours)}h')
    if minutes > 0 or result:
        result.append(f'{"%02d" % (minutes)}m')
    if seconds > 0 or result:
        result.append(f'{"%02d" % (seconds)}s')
    else:
        if seconds == 0:
            return (f'00s')
    return ''.join(result)