def split_list(lst: list, interval: int):
    """Creates a list of nested lists which length is based on the interval

    Args:
        lst (list): any list
        interval (int): any positive digit that is less than the length of lst

    Returns:
        list: nested lists of lists
    """
    return [lst[i:i + interval] for i in range(0, len(lst), interval)]