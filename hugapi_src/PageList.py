class PageList:
    def __init__(self, content=[], pageSize=20, pageIndex=1, lastPage=true):
        self.content = content
        self.pageSize = pageSize
        self.pageIndex = pageIndex
        self.lastPage = lastPage
	
