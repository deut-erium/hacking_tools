from io import BytesIO
from requests import get
from PIL import Image as Hacker

BASE = "https://github.com/deut-erium/hacking_tools/blob/master/forbidden_images/{}?raw=1"

LEETS = [
    "hackerIP.png",
    "hackerIhaveurIP.png",
    "hackerInsta.jpg",
    "hackerPSN.png",
    "haker.png",
    "hakerTiktok.png"]

HACKED_CONTENT = [Hacker.open(
    BytesIO(get(BASE.format(i)).content)) for i in LEETS]
for i in range(9):
    for HACKED in HACKED_CONTENT:
        HACKED.show()
