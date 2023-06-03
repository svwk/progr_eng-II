import sys
sys.path.append('.')

import unittest
import tests.params_t as pt
from generator import Generator

generator = Generator()

if __name__ == '__main__':
    unittest.main()

def test_generate_text_with_error_precision_negative():
    """Generate text with negative precision"""
    a = generator.generate_text(pt.st.text, -1)
    assert "Error" in a.keys()
    assert a.get('Error').startswith('Precision is not valid')

def test_generate_text_with_error_precision_big():
    """Generate text with big precision"""
    a = generator.generate_text(pt.st.text, 2)
    assert "Error" in a.keys()
    assert a.get('Error').startswith('Precision is not valid')

def test_generate_text_with_error_empty_text():
    """Generate text with empty text string"""
    a = generator.generate_text('', 1)
    assert "Error" in a.keys()
    assert a.get('Error').startswith('Text is not valid')

def test_generate_text_with_error_none_text():
    """Generate text with None text"""
    a = generator.generate_text(None, 1)
    assert "Error" in a.keys()
    assert a.get('Error').startswith('Text is not valid')