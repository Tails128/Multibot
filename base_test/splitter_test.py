"""Test splitter class."""
import sys
import os
sys.path.append(os.getcwd())
from base import splitter


def test_sortPriorities():
    """Test the sortPriorities function."""
    testSplitter = splitter.Splitter()
    values = {}
    values[3] = [{'priority': 3}]
    values[2] = [{'priority': 2}, {'priority': 2}]
    values[6] = [{'priority': 6}]
    values[1] = [{'priority': 1}]

    result = testSplitter.sortPriorities(values)
    assert result == [[{'priority': 1, 'answer': []}],
                      [{'priority': 2, 'answer': []},
                       {'priority': 2, 'answer': []}],
                      [{'priority': 3, 'answer': []}],
                      [{'priority': 6, 'answer': []}]]


def test_SplitByPriorities():
    """Test the splitByPriorities function."""
    testSplitter = splitter.Splitter()
    values = []
    values.append({'priority': 3})
    values.append({'priority': 2})
    values.append({'priority': 6})
    values.append({'priority': 1})
    values.append({'priority': 2})

    result = testSplitter.splitByPriority(values)
    assert result == [[{'priority': 1, 'answer': []}],
                      [{'priority': 2, 'answer': []},
                       {'priority': 2, 'answer': []}],
                      [{'priority': 3, 'answer': []}],
                      [{'priority': 6, 'answer': []}]]
