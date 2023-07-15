from enum import Enum


class AssertionTypes(str, Enum):
    EQUAL = '=='
    NOT_EQUAL = '!='
    LENGTH = 'is length'
    IN_ = 'is in'
    VALID = 'VALID FOR'
    MATCH = 'MATCH'
    TYPEOF = 'TYPE OF'
