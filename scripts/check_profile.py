"""Validate profile assets and links without fetching third-party widgets."""
from html.parser import HTMLParser
from pathlib import Path
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


class Images(HTMLParser):
    def __init__(self):
        super().__init__()
        self.paths = []
    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in ('src', 'srcset') and value:
                self.paths.append(value)


def main():
    for file in ('README.md', 'README.es.md'):
        text = (ROOT / file).read_text(encoding='utf-8')
        parser = Images()
        parser.feed(text)
        for path in parser.paths:
            if not path.startswith(('https://', 'http://')):
                assert (ROOT / path).is_file(), f'{file}: missing {path}'
        for tag in ('table', 'picture', 'tr', 'td'):
            assert len(re.findall(r'<' + tag + r'(?:\s|>)', text)) == text.count('</' + tag + '>'), (file, tag)
        ids = set(re.findall(r'<a id="([^"]+)"', text))
        for anchor in re.findall(r'href="#([^"]+)"', text):
            assert anchor in ids, (file, anchor)
        assert 'readme-builder' in text and 'OpenCode' in text and 'DeepSeek' in text
        assert 'pacman-contribution-graph-dark.svg' in text
        assert not re.search('[\U0001f000-\U0001faff\u2300-\u23ff\u2600-\u27ff]', text), f'{file}: decorative emoji remains'
    for svg in (ROOT / 'assets').rglob('*.svg'):
        ET.parse(svg)
    print('PASS: EN/ES assets, local links, navigation, balanced layouts, SVG XML and icon policy')


if __name__ == '__main__':
    main()
