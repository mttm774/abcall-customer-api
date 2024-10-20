class Channel:
    """
    This class represent a Channel of service abcall
    Attributes:
        id (UUID): channel id
        name (str): channel name
    """
    def __init__(self, id, name):
        self.id=id
        self.name=name