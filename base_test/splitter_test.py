"""Test splitter class."""
from base import splitter


def test_sort_priorities():
    """Test the sortPriorities function."""
    test_splitter = splitter.Splitter()
    values = {}
    values[3] = [{'priority': 3}]
    values[2] = [{'priority': 2}, {'priority': 2}]
    values[6] = [{'priority': 6}]
    values[1] = [{'priority': 1}]

    result = test_splitter.sort_priorities(values)
    assert result == [[{'priority': 1, 'answer': []}],
                      [{'priority': 2, 'answer': []},
                       {'priority': 2, 'answer': []}],
                      [{'priority': 3, 'answer': []}],
                      [{'priority': 6, 'answer': []}]]


def test_split_by_priorities():
    """Test the splitByPriorities function."""
    test_splitter = splitter.Splitter()
    values = []
    values.append({'priority': 3})
    values.append({'priority': 2})
    values.append({'priority': 6})
    values.append({'priority': 1})
    values.append({'priority': 2})

    result = test_splitter.split_by_priority(values)
    assert result == [[{'priority': 1, 'answer': []}],
                      [{'priority': 2, 'answer': []},
                       {'priority': 2, 'answer': []}],
                      [{'priority': 3, 'answer': []}],
                      [{'priority': 6, 'answer': []}]]
