def httpError(status):
    match status:
        case 400:
            return "Bad request"
        case 401 | 402 | 403:   # literals can be combined this way
            return "Not allowed"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something wrong with the internet"

print(httpError(402))