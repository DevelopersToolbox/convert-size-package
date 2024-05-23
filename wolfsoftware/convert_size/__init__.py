"""
A simple Python package to convert file sizes between different units in both IEC (binary) and SI (decimal) formats.

It includes functionality for getting the full name of a unit from its abbreviation and converting sizes between units.

Modules:
--------
convert_size.py : Contains the primary functions for converting sizes and retrieving unit names.

Functions:
----------
convert_size(size: float, start_unit: str, end_unit: str, si_units: bool = False) -> float:
    Convert a size between units, either IEC or SI.

convert_size_iec(size: float, start_unit: str, end_unit: str) -> float:
    Convert a size between IEC units.

convert_size_si(size: float, start_unit: str, end_unit: str) -> float:
    Convert a size between SI units.

get_name_from_code(unit: str, si_units: bool = False) -> str:
    Get the full name of a unit from its abbreviation.

get_name_from_code_iec(unit: str) -> str:
    Get the full name of an IEC unit from its abbreviation.

get_name_from_code_si(unit: str) -> str:
    Get the full name of an SI unit from its abbreviation.

Example Usage:
--------------
>>> from wolfsoftware.convert_size import convert_size, get_name_from_code
>>> size_in_gb = convert_size(1024, 'MiB', 'GiB')
>>> print(size_in_gb)
1.0
>>> unit_name = get_name_from_code('KiB')
>>> print(unit_name)
Kibibyte
"""

import importlib.metadata
from .convert_size import (
    convert_size,
    convert_size_iec,
    convert_size_si,
    get_name_from_code,
    get_name_from_code_iec,
    get_name_from_code_si
)

try:
    __version__: str = importlib.metadata.version('wolfsoftware.convert_size')
except importlib.metadata.PackageNotFoundError:
    __version__ = 'unknown'

__all__: list[str] = [
    'convert_size',
    'convert_size_iec',
    'convert_size_si',
    'get_name_from_code',
    'get_name_from_code_iec',
    'get_name_from_code_si'
]
