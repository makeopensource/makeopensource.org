import re

def to_date(value: str):
    date_format = re.compile(r'^(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})' \
                             r'.{3}:(?P<hours>\d{2}):(?P<minutes>\d{2})' \
                             r'.(?P<seconds>\d{2}).{2}$')
    match = date_format.match(value)
    if match:
        return f"{match.group('month')}-{match.group('day')}-{match.group('year')}"
    else: 
        return ''


def discordify(value: str):
    matching = lambda x: f'({x})([^*]+?)({x})'
    value = re.sub(matching(r'\*\*'), r'<b>\2</b>', value)  # bold
    value = re.sub(matching(r'\*'), r'<i>\2</i>', value)     # italics
    value = re.sub(r'(https?://[a-zA-Z0-9~._~/\+-?]+)', r'<a href="\1">\1</a>', value)
    return value.replace('\n', '<br>')
