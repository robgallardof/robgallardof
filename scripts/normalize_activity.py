"""Keep generated activity consistent with the profile's local SVG icon policy."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
EVENT_ICON = '<img src="assets/icons/lucide/git-branch.svg" width="16" height="16" alt="" />'
EMOJI = re.compile('[\U0001f000-\U0001faff\u2300-\u23ff\u2600-\u27ff][\U0001f000-\U0001faff\u2300-\u23ff\u2600-\u27ff\ufe0f\u200d]*')


def normalize(source):
    """Change generated activity icons only; preserve the header and final signature."""
    return re.sub(r'(<!--START_SECTION:activity-->)(.*?)(<!--END_SECTION:activity-->)',
                  lambda match: match[1] + EMOJI.sub(EVENT_ICON, match[2]) + match[3],
                  source, flags=re.S)


if __name__ == '__main__':
    for name in ('README.md', 'README.es.md'):
        path = ROOT / name
        before = path.read_bytes()
        updated = normalize(before.decode('utf-8'))
        if updated != before.decode('utf-8'):
            path.write_bytes(updated.encode('utf-8'))
