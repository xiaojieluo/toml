from toml.decoder import TomlDecoder
import pytest

@pytest.fixture
def decoder():
    return TomlDecoder()

@pytest.mark.parametrize('input,expected',[
    # Numbers
    ('3', (3, 'int')),
    ('+99', (99, 'int')),
    ('42', (42, 'int')),
    ('0', (0, 'int')),
    ('-17', (-17, 'int')),
    ('1_000', (1000, 'int')),
    ('5_349_221', (5349221, 'int')),
    ('1_2_3_4_5', (12345, 'int')),

    # Floats
    ('+1.0', (+1.0, 'float')),
    ('3.1415', (3.1415, 'float')),
    ('-0.01', (-0.01, 'float')),
    ('5e+22', (5e+22, 'float')),
    ('1e6', (1e6, 'float')),
    ('-2E-2', (-2E-2, 'float')),
    ('6.626e-34', (6.626e-34, 'float')),
])

def test_load_value_valid(decoder, input, expected):
    result = decoder._load_value(input)
    assert result == expected

# @pytest.mark.parametrize('input', [
#     '2..1',
#     '2__3',
#     '-+3'
# ])
# def test_load_value_invalid(decoder, input):
#     pass


def test_load_numeric(decoder, benchmark):
    result = benchmark(decoder._load_numeric, '5e+22', True)
    assert result == (5e+22, 'float')

