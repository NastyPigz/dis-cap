from .objects import *

class ServerGuild:
    def __init__(self, payload:dict):
        self.original= payload
        self.id = payload["id"]
        self.name = payload["name"]
        self.description = payload["description"]
        self.mfa_level = payload["mfa_level"]
        self.nsfw = payload["nsfw"]
        self.nsfw_level = payload["nsfw_level"]
        self.owner = payload["owner_id"]
        self._channels_data = payload["channels"] # channels
        self._members_data = payload["members"] # members
        self.premium_tier = payload["premium_tier"]
        self._roles_data = payload["roles"] #roles
        self.threads = payload["threads"] # threads
        self.rule_channel = payload["rules_channel_id"]
        self.system_channel = payload["system_channel_id"]
        self.verification_level = payload["verification_level"]
        self._stickers_data = payload["stickers"] #stickers
        self.banner = payload["banner"]
        self._emojis_data = payload["emojis"] #emojis
        self.icon = payload["icon"]
    
    @property
    def channels(self):
        list_channels = []
        for _channel in self._channels_data:
            list_channels.append(DiscordChannel(_channel))
        
