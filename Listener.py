from robot import running, result


def start_keyword(data: running.Keyword, result: result.Keyword):
    print(data.name, data.args, data.lineno, result.status)


def start_user_keyword(data: running.Keyword,
                       impl: running.UserKeyword,
                       result: result.Keyword):
    print(f"User keyword '{data.name}' used on line {data.lineno} "
          f"and implemented on line {impl.lineno} at '{impl.source.name}'.")
    impl.body.clear()
    impl.body.create_keyword('Log', ['Hello, RoboCon!', 'INFO'])
    impl.body.create_return(['something'])


def start_library_keyword(data: running.Keyword,
                          impl: running.LibraryKeyword,
                          result: result.Keyword):
    print(f"Library keyword '{data.name}' used on line {data.lineno} "
          f"and implemented on line {impl.lineno} at '{impl.source.name}'.")
    print(impl.owner.instance)


def start_return(data: running.Return, result: result.Return):
    result.values = ['<secret>']


def start_body_item(data, result):
    print(type(data))
