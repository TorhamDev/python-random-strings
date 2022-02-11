"""
This module can help you generate random strings of any kind.
"""
import random
import logging
import string

# logger setup
LOG_LEVEL = logging.INFO
my_logger = logging
my_logger.basicConfig(level=LOG_LEVEL)
logger = my_logger.getLogger('python random strings')

# Some strings for ctype-style character classification
ASCII_LOWERCASE = string.ascii_lowercase
ASCII_UPPERCASE = string.ascii_uppercase
ASCII_LETTERS = string.ascii_letters
DIGITS = string.digits
HEXDIGITS = string.hexdigits
OCTDIGITS = string.octdigits
PUNCTUATION = string.punctuation
PRINTABLE = DIGITS + ASCII_LETTERS + PUNCTUATION
WHITESPACE = string.whitespace


class random_strings():
    """
    return random strings with length optional.
    """

    @staticmethod
    def random_lowercase(length:int=1):
        """
        return random lower-case ascii letters
        """
        selected = ''
        try:
            if length > len(ASCII_LOWERCASE):
                while length > len(ASCII_LOWERCASE): # To avoid random.sample error
                    selected += ASCII_LOWERCASE

                return ''.join(random.sample(selected,length))
            else:
                return ''.join(random.sample(ASCII_LOWERCASE,length))
        except Exception as e:
            my_logger.error(e)
            return e

    @staticmethod  
    def random_uppercase(length:int=1):
        """
        return random upper-case ascii letters
        """
        selected = ''
        try:
            if length > len(ASCII_UPPERCASE):
                while length > len(ASCII_UPPERCASE): # To avoid random.sample error
                    selected += ASCII_UPPERCASE

                return ''.join(random.sample(selected,length))
            else:
                return ''.join(random.sample(ASCII_UPPERCASE,length))
        except Exception as e:
            my_logger.error('length should be an int not an %s'%type(length))
            raise TypeError('length should be an int not an %s'%type(length))

    @staticmethod
    def random_letters(length:int=1):
        """
        return random latters ascii case
        """
        selected = ''
        try:
            if length > len(ASCII_UPPERCASE): # To avoid random.sample error
                while length > len(ASCII_UPPERCASE):
                    selected += ASCII_UPPERCASE 

                return ''.join(random.sample(selected,length))
            else:
                return ''.join(random.sample(ASCII_LETTERS,length))
        except Exception as e:
            my_logger.error('length should be an int not an %s'%type(length))
            raise TypeError('length should be an int not an %s'%type(length))

    @staticmethod
    def random_digits(length:int=1):
        """
        return random digits
        """
        selected = ''
        try:
            if length > DIGITS: # To avoid random.sample error
                while length > len(DIGITS):
                    selected += DIGITS

                return int(''.join(random.sample(selected,length)))
            else:
                return int(''.join(random.sample(DIGITS,length)))
        except Exception as e:
            my_logger.error('length should be an int not an %s'%type(length))
            raise TypeError('length should be an int not an %s'%type(length))

    @staticmethod
    def random_hexdigits(length:int=1):
        """
        return random hex digits
        """
        selected = ''
        try:
            if length > HEXDIGITS: # To avoid random.sample error
                while length > len(HEXDIGITS):
                    selected += HEXDIGITS

                return ''.join(random.sample(selected,length))
            else:
                return ''.join(random.sample(HEXDIGITS,length))
        except Exception as e:
            my_logger.error('length should be an int not an %s'%type(length))
            raise TypeError('length should be an int not an %s'%type(length))

    @staticmethod
    def random_octdigits(length:int=1):
        """
        return random octal digits
        """
        selected = ''
        try:
            if length > OCTDIGITS: # To avoid random.sample error
                while length > len(OCTDIGITS):
                    selected += OCTDIGITS

                return int(''.join(random.sample(selected,length)))
            else:
                return int(''.join(random.sample(OCTDIGITS,length)))
        except Exception as e:
            my_logger.error('length should be an int not an %s'%type(length))
            raise TypeError('length should be an int not an %s'%type(length))

    @staticmethod
    def random_punctuation(length:int=1):
        """
        return random punctuation string
        """
        selected = ''
        try:
            if length > PUNCTUATION: # To avoid random.sample error
                while length > len(PUNCTUATION):
                    selected += PUNCTUATION

                return ''.join(random.sample(selected,length))
            else:
                return ''.join(random.sample(PUNCTUATION,length))
        except Exception as e:
            my_logger.error('length should be an int not an %s'%type(length))
            raise TypeError('length should be an int not an %s'%type(length))

    @staticmethod
    def random_printable(length:int=1):
        """
        return random printable string
        """
        
        selected = ''
        try:
            if length > PRINTABLE: # To avoid random.sample error
                while length > len(PRINTABLE):
                    selected += PRINTABLE

                return ''.join(random.sample(selected,length))
            else:
                return ''.join(random.sample(PRINTABLE,length))
        except Exception as e:
            my_logger.error('length should be an int not an %s'%type(length))
            raise TypeError('length should be an int not an %s'%type(length))

    @staticmethod
    def random_whitespace(length:int=1):
        """
        return random whitespace
        """
        
        selected = ''
        try:
            if length > WHITESPACE: # To avoid random.sample error
                while length > len(WHITESPACE):
                    selected += WHITESPACE

                return ''.join(random.sample(selected,length))
            else:
                return ''.join(random.sample(WHITESPACE,length))
        except Exception as e:
            my_logger.error('length should be an int not an %s'%type(length))
            raise TypeError('length should be an int not an %s'%type(length))