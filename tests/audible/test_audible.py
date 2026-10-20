from datetime import datetime, date, timedelta
from audiobook.audible import Audible
from audiobook.utils.ui_utils import rprint_

ASIN_LIST_FR = [
    "B0D7D39LP5",  # La bataille des Jedi
    "B0G5QKNT1J",  # Assassin’s Apprentice (The Farseer Trilogy, Book 1)
    "B0G71PC24C",  # La Conquête des Nébuleuses
    "B0BVGSJ9TD",  # One Foot in the Grave (Dramatized Adaptation)
    "B00BSX9XM4",  # Twice Tempted
    "B0FSDY3D2F",  # L'Épée de la Providence
    "2367627002",  # L'œil d'Otolep
    "2075136246",  # La mémoire de Babel
]
ASIN_LIST_UK = [
    "B0BVGSYL4Q",  # One Foot in the Grave
]


# Assassin’s Apprentice (The Farseer Trilogy, Book 1) from Audible.fr
def test_farseer():
    audible = Audible("0008487278", "com")
    rprint_(audible.audiobook)

    assert audible.success is True
    audiobook = audible.audiobook
    assert audiobook.asin == "0008487278"
    assert isinstance(audiobook.fetched_at, datetime)
    assert isinstance(audiobook.url, str)
    assert audiobook.original_title
    assert "The Lord of the Rings" in audiobook.original_title
    assert audiobook.subtitle is None
    assert isinstance(audiobook.description, str)
    assert audiobook.copyright_ == "©1954 The Tolkien Estate Limited (P)1954 HarperCollins Publishers Limited"
    assert audiobook.publisher == "HarperCollins"
    assert audiobook.authors == ["J. R. R. Tolkien"]
    assert audiobook.narrators == ['Andy Serkis']
    assert audiobook.published_at == date(2021, 9, 16)
    assert audiobook.duration == timedelta(seconds=81480)
    assert audiobook.language == "English"
    assert audiobook.abridged is False
    assert isinstance(audiobook.cover, str)
    assert audiobook.original_series == ['The Lord of the Rings']
    assert isinstance(audiobook.original_series, list)
    assert audiobook.part == "Book 1"
    assert audiobook.volume == 1.0
    assert audiobook.format_ == "Unabridged Audiobook"
    assert audiobook.book_format == "AudiobookFormat"
    assert audiobook.sku == "BK_HCUK_006448"
    assert audiobook.product_id == "0008487278"
    assert audiobook.rating == 4.9
    assert audiobook.price == 14.95
    assert audiobook.currency == "USD"
    assert audiobook.genres == [
        'Action & Adventure',
        'Celebrity',
        'Classics',
        'Dragons & Mythical Creatures',
        'Epic',
        'Fairy Tales',
        'Fantasy'
    ]
    assert audiobook.categories == ['Literature & Fiction']

    assert audiobook.title
    assert "The Farseer: Assassin's Apprentice" in audiobook.title
    # assert audiobook.series == "Farseer"
    assert audiobook.volume == 1.0

    assert audiobook.genres_all == [
        'Action & Adventure',
        'Arthurian',
        'Assassin',
        'Epic',
        'Epic Fantasy',
        'Fantasy',
        'Fantasy Essentials',
        'Fiction',
        'Royalty',
        'Science Fiction & Fantasy',
        'Suspenseful'
    ]
    assert audiobook.duration_human == "17:18:00"

    assert audiobook.genres_list == (
        "Action & Adventure/Arthurian/Assassin/Epic/Epic Fantasy/Fantasy/"
        "Fantasy Essentials/Fiction/Royalty/Science Fiction & Fantasy/Suspenseful"
    )
    assert audiobook.authors_list == "Robin Hobb"
    assert audiobook.narrators_list == "Andy Serkis"
    assert audiobook.year == 2021


# L'œil d'Otolep from Audible.fr
# def test_otolep():
#     audible = Audible("2367627002")

#     assert audible.success is True
#     assert audible.audiobook.title == "L'œil d'Otolep"
#     assert audible.audiobook.subtitle == "Les mondes d'Ewilan 2"
#     assert audible.audiobook.series == "Les mondes d'Ewilan"
#     assert audible.audiobook.volume == 2.0


# # La bataille des Jedi from Audible.fr
# def test_jedi():
#     audible = Audible("B0D7D39LP5")

#     assert audible.success is True
#     assert audible.audiobook.title == "La bataille des Jedi"
#     assert audible.audiobook.series == "La croisade noire du jedi fou"
#     assert audible.audiobook.volume == 2.0
#     assert audible.audiobook.volume_int == 2
#     assert audible.audiobook.authors == ["Timothy Zahn"]


# # Assassin’s Apprentice (The Farseer Trilogy, Book 1) from Audible.com
# def test_farseer_com():
#     audible = Audible("B003AO3P5A")

#     assert audible.success is True
#     assert audible.fetch.json_duration.series_typed == "Farseer Trilogy"
#     assert audible.fetch.json_duration.part_typed == 1


# def test_author():
#     audible = Audible("B0DNMX6SSS")
#     audiobook = audible.audiobook

#     assert audiobook.asin == "B0DNMX6SSS"
#     assert audiobook.title == "Les Naufragés de Velloa"
#     assert audiobook.authors == ["Romain Benassaya"]
