from join.models import Member
from django.contrib.auth.tokens import PasswordResetTokenGenerator

import datetime


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, member: Member, timestamp) -> str:
        token: str = str(member.pk) + str(timestamp)
        return token
    
    def is_valid() -> bool:
        return datetime.datetime.now() - datetime.timedelta(hours=24) > datetime.timedelta(hours=0)

account_activation_token = TokenGenerator()