"""A dumy docstring."""
from requests import get


def get_error_message(error_type):
    """A dummy docstrig."""
    if error_type == 404:
        return 'red'
    if error_type == 403:
        return 'orange'
    if error_type == 401:
        return 'yellow'
    return 'blue'


def main():
    """A dummy docstring."""
    res = get('https://api.github.com/events', timeout=10)
    status = res.status_code
    if res.ok:
        print(f'{status}')
    else:
        print(get_error_message(status))


if __name__ == '__main__':
    main()
