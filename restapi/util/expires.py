from datetime import timedelta

from restapi.config import Config
from restapi.util import now

def user_expires_at():
	return now() + timedelta(days=Config.USER_DEFAULT_EXPIRY_TIME)