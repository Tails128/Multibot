"""Test splitter class."""
from splitter import Splitter


def test_compactPriorities():
    """Test the compactPriorities function."""
    testSplitter = Splitter()
    values = {}
    values[3] = [{'priority': 3}]
    values[2] = [{'priority': 2}, {'priority': 2}]
    values[6] = [{'priority': 6}]
    values[1] = [{'priority': 1}]
    priorities = set()
    priorities.add(3)
    priorities.add(2)
    priorities.add(6)
    priorities.add(1)
    priorities.add(2)

    result = testSplitter.compactPriorities(values, priorities)
    assert result == [[{'priority': 1}], [{'priority': 2}, {'priority': 2}],
                      [{'priority': 3}], [{'priority': 6}]]


def test_SplitByPriorities():
    """Test the splitByPriorities function."""
    testSplitter = Splitter()
    values = []
    values.append({'priority': 3})
    values.append({'priority': 2})
    values.append({'priority': 6})
    values.append({'priority': 1})
    values.append({'priority': 2})

    result = testSplitter.splitByPriority(values)
    assert result == [[{'priority': 1}], [{'priority': 2}, {'priority': 2}],
                      [{'priority': 3}], [{'priority': 6}]]
