__all__ = ("even_odd",)


def even_odd(numbers: list[int]) -> float:
    chet = []
    nechet = [] 
    for index in numbers:
        if index % 2 == 0:
            chet.append(index)
        if index % 2 != 0:
            nechet.append(index)
    if sum(chet) > 0 and sum(nechet) > 0:
        sum_final = sum(chet) / sum(nechet)
        return sum_final
    else:
        return 0

