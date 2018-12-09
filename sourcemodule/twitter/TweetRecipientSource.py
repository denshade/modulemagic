import tokenize
from io import StringIO
from typing import List


def get_recipients(tweet: str) -> List:
    g = tokenize.generate_tokens(StringIO(tweet).readline)
    recipients = []
    for toknum, tokval, _,_,_ in g:
        if tokval.startswith("@"):
            recipients.append(tokval[1:len(tokval)])
    return recipients
