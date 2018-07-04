def slices(series, length):
    if len(series) < length or length <= 0 :
        raise ValueError('you deserve what you get.')
    else:
        return [series[i: i + length] for i in range(len(series) - length + 1)]


# def getSubSeries(*, series, length, result=[]):
#     return result + [series] if len(series) == length else getSubSeries(series=series[1:],
#                                                                         length=length,
#                                                                         result=result + [series[0:length]])
