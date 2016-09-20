import math


def getPage(page, limit, totalCount):

    # limit = 3
    if page != None:
        page = int(page)
        if page <= 0:
            page = 1
    else:
        page = 1
    totalPage = math.ceil(totalCount * 1.0 / limit)
    if page >= totalPage:
        page = totalPage
    if totalPage <= 5:
        beginIndex = 1
        endIndex = totalPage
    else:
        beginIndex = page - 2
        endIndex = page + 2
        if beginIndex < 1:
            beginIndex = 1
            endIndex = 5
        if endIndex > totalPage:
            beginIndex = totalPage - 5 + 1;
            endIndex = totalPage

    indexList = ''
    for i in range(beginIndex, endIndex + 1):
        indexList = indexList + str(i)
    pageInfo = {
        'page': page,
        'limit': limit,
        'indexList': indexList,
        'totalPage': totalPage
    }
    return pageInfo
