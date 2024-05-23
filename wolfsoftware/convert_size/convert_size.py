"""
This module provides functions for converting file sizes between different units.

It works with both IEC (binary) and SI (decimal) formats. It includes functionality for
getting the full name of a unit from its abbreviation and converting sizes between units.
"""

# IEC based values
size_codes_iec: tuple = ('B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB')
size_names_iec: tuple = ('Byte', 'Kibibyte', 'Mebibyte', 'Gibibyte', 'Tebibyte', 'Pebibyte', 'Exbibyte', 'Zebibyte', 'Yobibyte')

# SI based values
size_codes_si: tuple = ('B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')
size_names_si: tuple = ('Byte', 'Kilobyte', 'Megabyte', 'Gigabyte', 'Terabyte', 'Petabyte', 'Exabyte', 'Zettabyte', 'Yottabyte')


def __in_tuple(item: str, stuff: tuple) -> bool:
    """
    Check if an item exists in a tuple, case-insensitively.

    Arguments:
        item (str): The item to search for.
        stuff (tuple): The tuple to search in.

    Returns:
        bool: True if the item exists in the tuple, False otherwise.
    """
    return any(s.lower() == item.lower() for s in stuff)


def __get_tuple(item: str, stuff: tuple) -> int:
    """
    Get the index of an item in a tuple, case-insensitively.

    Arguments:
        item (str): The item to search for.
        stuff (tuple): The tuple to search in.

    Returns:
        int: The index of the item in the tuple.

    Raises:
        ValueError: If the item is not found in the tuple.
    """
    new_list: list = [s.lower() for s in stuff]

    try:
        return new_list.index(item.lower())
    except ValueError as err:
        raise ValueError(f'Item {item} not found in the provided tuple.') from err


def __get_index(unit: str, code_list: tuple) -> int:
    """
    Get the index of a unit in a list of codes, ensuring the unit is valid.

    Arguments:
        unit (str): The unit code to find.
        code_list (tuple): The list of valid unit codes.

    Returns:
        int: The index of the unit code in the list.

    Raises:
        ValueError: If the unit code is not valid.
    """
    if not __in_tuple(unit, code_list):
        valid_types: str = ', '.join(code_list)
        raise ValueError(f'Invalid unit type {unit}, valid options are: {valid_types}')
    return __get_tuple(unit, code_list)


def __calculate_new_size(size: float, scaler: int, start_index: int, end_index: int) -> float:
    """
    Calculate the new size after converting between units.

    Arguments:
        size (float): The original size.
        scaler (int): The scaling factor (1024 for IEC, 1000 for SI).
        start_index (int): The index of the starting unit.
        end_index (int): The index of the ending unit.

    Returns:
        float: The converted size.
    """
    if end_index > start_index:
        for _ in range(end_index - start_index):
            size /= scaler
    else:
        for _ in range(start_index - end_index):
            size *= scaler
    return size


def get_name_from_code_iec(unit: str) -> str:
    """
    Get the full name of an IEC unit from its abbreviation.

    Arguments:
        unit (str): The IEC unit abbreviation.

    Returns:
        str: The full name of the IEC unit.

    Raises:
        ValueError: If the unit abbreviation is not valid.
    """
    name_index: int = __get_index(unit, size_codes_iec)
    return size_names_iec[name_index]


def get_name_from_code_si(unit: str) -> str:
    """
    Get the full name of an SI unit from its abbreviation.

    Arguments:
        unit (str): The SI unit abbreviation.

    Returns:
        str: The full name of the SI unit.

    Raises:
        ValueError: If the unit abbreviation is not valid.
    """
    name_index: int = __get_index(unit, size_codes_si)
    return size_names_si[name_index]


def get_name_from_code(unit: str, si_units: bool = False) -> str:
    """
    Get the full name of a unit from its abbreviation.

    Arguments:
        unit (str): The unit abbreviation.
        si_units (bool): If True, use SI units; otherwise, use IEC units.

    Returns:
        str: The full name of the unit.

    Raises:
        ValueError: If the unit abbreviation is not valid.
    """
    if si_units:
        return get_name_from_code_si(unit)
    return get_name_from_code_iec(unit)


def convert_size_iec(size: float, start_unit: str, end_unit: str) -> float:
    """
    Convert a size between IEC units.

    Arguments:
        size (float): The original size.
        start_unit (str): The starting unit abbreviation.
        end_unit (str): The ending unit abbreviation.

    Returns:
        float: The converted size.

    Raises:
        ValueError: If the unit abbreviations are not valid.
    """
    if size == 0:
        return 0.0

    scaler = 1024

    start_index: int = __get_index(start_unit, size_codes_iec)
    end_index: int = __get_index(end_unit, size_codes_iec)

    return __calculate_new_size(size, scaler, start_index, end_index)


def convert_size_si(size: float, start_unit: str, end_unit: str) -> float:
    """
    Convert a size between SI units.

    Arguments:
        size (float): The original size.
        start_unit (str): The starting unit abbreviation.
        end_unit (str): The ending unit abbreviation.

    Returns:
        float: The converted size.

    Raises:
        ValueError: If the unit abbreviations are not valid.
    """
    if size == 0:
        return 0.0

    scaler = 1000

    start_index: int = __get_index(start_unit, size_codes_si)
    end_index: int = __get_index(end_unit, size_codes_si)

    return __calculate_new_size(size, scaler, start_index, end_index)


def convert_size(size: float, start_unit: str, end_unit: str, si_units: bool = False) -> float:
    """
    Convert a size between units, either IEC or SI.

    Args:
        size (float): The original size.
        start_unit (str): The starting unit abbreviation.
        end_unit (str): The ending unit abbreviation.
        si_units (bool): If True, use SI units; otherwise, use IEC units.

    Returns:
        float: The converted size.

    Raises:
        ValueError: If the unit abbreviations are not valid.
    """
    if size == 0:
        return 0.0

    if si_units:
        return convert_size_si(size, start_unit, end_unit)
    return convert_size_iec(size, start_unit, end_unit)
