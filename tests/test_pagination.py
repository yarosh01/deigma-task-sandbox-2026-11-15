from app.pagination import paginate

ITEMS = list(range(1, 31))


def test_second_page_follows_the_first():
    assert paginate(ITEMS, 2, per_page=10) == list(range(11, 21))


def test_second_page_can_be_short():
    assert paginate(ITEMS[:15], 2, per_page=10) == [11, 12, 13, 14, 15]


def test_every_item_is_on_exactly_one_page():
    items = list(range(1, 46))
    pages = [paginate(items, p, per_page=10) for p in range(1, 6)]
    assert [len(p) for p in pages] == [10, 10, 10, 10, 5]
    assert [x for p in pages for x in p] == items


def test_third_page_starts_right_after_the_second():
    assert paginate(ITEMS, 3, per_page=10) == list(range(21, 31))
