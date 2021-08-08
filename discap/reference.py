
class MR:
    @staticmethod
    def custom(*, message_id:int, guild_id:int, channel_id:int=None, retry:bool=True):
        return {
        "message_id": message_id,
        "guild_id": guild_id,
        "channel_id": channel_id,
        "fail_if_not_exists": False if retry else True
        }
    
    @staticmethod
    def reply_message(msg, *, retry:bool=True):
        return {
        "message_id": msg.id,
        "guild_id": msg.guild.id,
        "fail_if_not_exists": False if retry else True
        }