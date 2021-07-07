import datetime


def logging(path):
    def decorator(function):
        def new_function(*args, **kwargs):
            result = function(*args, **kwargs)
            with open(path, 'a', encoding='utf-8') as f:
                f.write(f'{datetime.datetime.now()} ; {function.__name__} ; {args} ; {kwargs} ; {result}\n')
        return new_function
    return decorator


@logging('log.txt')
def foo(arg1, arg2):
    return 666


documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


@logging('log.txt')
def whose_document(number):
    for document in documents:
        if document['number'] == number:
            print('Документ пренадлежит:', document['name'])
            return
    print('Неизвестный документ')


@logging('log.txt')
def add_document(document, shelf):
    if document in documents:
        print('Такой документ уже присутствует')
        return
    if shelf not in directories:
        print('Такой полки не существует')
        return
    documents.append(document)
    directories[shelf].append(document['number'])


def main():
    foo(5, "foo")
    whose_document('10006')
    add_document({"type": "passport", "number": "2207 111111", "name": "Василий Васильев"}, '1')


if __name__ == '__main__':
    main()