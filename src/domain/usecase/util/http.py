

# class HttpRequest:

#     def __init__(self, header: Dict = None, body: Dict = None, query: Dict = None) -> None:
#         self.header = header
#         self.body = body
#         self.query = query

#     def __repr__(self) -> str:
#         return f"HttpRequest (header={self.header}, body={self.body}, query={self.query})"


class HttpResponse:

    def __init__(self, statusCode: int, body: any) -> None:
        self.statusCode = statusCode
        self.body = body

    def __repr__(self) -> str:
        return f"HttpRequest (statusCode={self.statusCode}, body={self.body})"