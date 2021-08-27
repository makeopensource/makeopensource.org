from join.models import Member
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import timezone
import datetime


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, member: Member, timestamp) -> str:
        token: str = str(member.pk) + str(timestamp)
        return token
    
    def is_valid(self,member) -> bool:
        return datetime.datetime.now(tz=timezone.utc) - datetime.timedelta(hours=24) < member.join_date

account_activation_token = TokenGenerator()
