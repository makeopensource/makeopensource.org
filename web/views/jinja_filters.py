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


# This function uses a bunch of regex, some of it is pretty messy.
# Each line adds a new type of substitution to the previous, the 
# comments detail what each line is intended to substitute for.

# This follows **discord** markdown, which is much more limited
# than traditional markdown. However, it is *nearly* complete subset of
# traditional markdown, the comment divides traditional vs discord-specific

# Currently supports: bold, italics, strikethrough, code (single line), links

def discordify(value: str, channels = {}): 

    matching = lambda x: f'({x})([^*]+?)({x})'  # generate regex to match *both* sides of element
    replace_channel = lambda match: f'<div class="channel">#{channels[match.group(1)]}</div>'

    # traditional markdown syntax
    value = re.sub(matching(r'\*\*'), r'<b>\2</b>', value)      # bold
    value = re.sub(matching(r'\*'), r'<i>\2</i>', value)        # italics
    value = re.sub(matching(r'~~'), r'<del>\2</del>', value)    # strikethrough
    value = re.sub(matching(r'`'), r'<code>\2</code>', value)   # code
    value = re.sub(r'(https?://[a-zA-Z0-9~._~/\+-?]+)', r'<a href="\1">\1</a>', value)  # links

    # discord-exclusive syntax
    value = re.sub(r'<:\w+:(\d+)>', r'<img class="emoji" src="https://cdn.discordapp.com/emojis/\1.png">', value)  # in-text img
    if channels:
        value = re.sub(r'<#(\d+)>', lambda x: replace_channel(x), value)  # replaces channels
    return value.replace('\n', '<br>')

