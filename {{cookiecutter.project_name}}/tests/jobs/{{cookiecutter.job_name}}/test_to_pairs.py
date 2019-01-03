from jobs.{{ cookiecutter.job_name }} import to_pairs
from mock import MagicMock


def test_to_pairs():
    context = MagicMock()
    result = to_pairs(context, 'foo')
    context.inc_counter.assert_called_with('words')
    assert result[0] == 'foo'
    assert result[1] == 1
