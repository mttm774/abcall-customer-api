class ChannelPlan:
    """
    This class represent a Channel in plan of abcall service
    Attributes:
        id (UUID): channel plan  id
        channel_id: (UUID): channel id
        plan_id: (UUID): plan id
    """
    def __init__(self, id, channel_id,plan_id):
        self.id=id
        self.channel_id=channel_id
        self.plan_id=plan_id