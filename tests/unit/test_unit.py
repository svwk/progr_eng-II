import unittest
import pytest

import sys
sys.path.append('.')

from unittest.mock import Mock
from generator import Generator


test_text = 'Hi Linda, How is it going? ' \
            'Sorry I haven not been in touch for such a long time but I have had exams so I have been studying every free minute. ' \
            'Anyway, I love to hear all your news and I am hoping we can get together soon to catch up. ' \
            'We just moved to a bigger flat so maybe you can come and visit one weekend? How is the new job? Looking forward to hearing from you! ' \
            'Helga'

if __name__ == '__main__':
    unittest.main()

def test_generate_text_with_exception_precision_negative():
    generator = Generator()
    generator_mock = Mock(side_effect=Exception)
    generator.generator = generator_mock

    a = generator.generate_text(test_text, -1)
    assert "Error" in a.keys()
    assert a.get('Error').startswith('Precision is not valid')

def test_generate_text_with_exception_precision_big():
    generator = Generator()
    generator_mock = Mock(side_effect=Exception)
    generator.generator = generator_mock

    a = generator.generate_text(test_text, -1)
    assert "Error" in a.keys()
    assert a.get('Error').startswith('Precision is not valid')

def test_generate_text_with_exception_empty_text():
    generator = Generator()
    generator_mock = Mock(side_effect=Exception)
    generator.generator = generator_mock

    a = generator.generate_text('', 1)
    assert "Error" in a.keys()
    assert a.get('Error').startswith('Text is not valid')

def test_generate_text_with_exception_none_text():
    generator = Generator()
    generator_mock = Mock(side_effect=Exception)
    generator.generator = generator_mock

    a = generator.generate_text(None, 1)
    assert "Error" in a.keys()
    assert a.get('Error').startswith('Text is not valid')

##Не нашел кейс при котором у нас выскакивает exception, если есть идеи, буду рад
def test_generate_text_with_exception():
    generator = Generator()
    generator_mock = Mock(side_effect=Exception)
    generator.generator = generator_mock

    a = generator.generate_text("..................................................................................", 1)
    assert "Exception" in a.keys()
    assert a.get('Exception').startswith('Parameters are not valid')