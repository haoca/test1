def print_hello(name: str) -> str:
    """
    Greets the user by name
        Parameters:
                name (str): The name of the user
        Returns:
                str: The greeting
        """
    print('hello '+name)


def sorter(item):
    return item['name']


presenters = [{'name': 'huhujjjjjjj', 'age': '19'},
              {'name': 'aiaoming', 'age': '22'}]
print(presenters)
presenters.sort(key=sorter)
print(presenters)
