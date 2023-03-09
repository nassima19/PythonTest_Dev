from requests import get


def get_error_message(error_type):
    if error_type == 404:
        return 'red'
    elif error_type == 403:
        return 'orange'
    elif error_type == 401:
        return 'yellow'
    else:
        return 'blue'


def main():
    res = get('https://api.github.com/events')
    status = res.status_code
    if res.ok:
        print(f'{status}')
    else:
        print(get_error_message(status))


if __name__ == '__main__':
    main()
