class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "1813305809"
    sudo_users = "1813305809"
    GROUP_ID = -1002023327777
    TOKEN = "5383246595:AAF7UYG-baggRelLuAATKQ6qPpANq_qJP6Q"
    mongo_url = "mongodb+srv://manudarkdevil911:manu1234@cluster0.alnwwhb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "Collect_em_support"
    UPDATE_CHAT = "Collect_em_support"
    BOT_USERNAME = "AnilistXBot"
    CHARA_CHANNEL_ID = "-1002078628248"
    api_id = 8143727
    api_hash = "e2e9b22c6522465b62d8445840a526b1"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
