<!-- markdownlint-disable -->
<p align="center">
    <a href="https://github.com/DevelopersToolbox/">
        <img src="https://cdn.wolfsoftware.com/assets/images/github/organisations/developerstoolbox/black-and-white-circle-256.png" alt="DevelopersToolbox logo" />
    </a>
    <br />
    <a href="https://github.com/DevelopersToolbox/convert-size-package/actions/workflows/cicd.yml">
        <img src="https://img.shields.io/github/actions/workflow/status/DevelopersToolbox/convert-size-package/cicd.yml?branch=master&label=build%20status&style=for-the-badge" alt="Github Build Status" />
    </a>
    <a href="https://github.com/DevelopersToolbox/convert-size-package/blob/master/LICENSE.md">
        <img src="https://img.shields.io/github/license/DevelopersToolbox/convert-size-package?color=blue&label=License&style=for-the-badge" alt="License">
    </a>
    <a href="https://github.com/DevelopersToolbox/convert-size-package">
        <img src="https://img.shields.io/github/created-at/DevelopersToolbox/convert-size-package?color=blue&label=Created&style=for-the-badge" alt="Created">
    </a>
    <br />
    <a href="https://github.com/DevelopersToolbox/convert-size-package/releases/latest">
        <img src="https://img.shields.io/github/v/release/DevelopersToolbox/convert-size-package?color=blue&label=Latest%20Release&style=for-the-badge" alt="Release">
    </a>
    <a href="https://github.com/DevelopersToolbox/convert-size-package/releases/latest">
        <img src="https://img.shields.io/github/release-date/DevelopersToolbox/convert-size-package?color=blue&label=Released&style=for-the-badge" alt="Released">
    </a>
    <a href="https://github.com/DevelopersToolbox/convert-size-package/releases/latest">
        <img src="https://img.shields.io/github/commits-since/DevelopersToolbox/convert-size-package/latest.svg?color=blue&style=for-the-badge" alt="Commits since release">
    </a>
    <br />
    <a href="https://github.com/DevelopersToolbox/convert-size-package/blob/master/.github/CODE_OF_CONDUCT.md">
        <img src="https://img.shields.io/badge/Code%20of%20Conduct-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/DevelopersToolbox/convert-size-package/blob/master/.github/CONTRIBUTING.md">
        <img src="https://img.shields.io/badge/Contributing-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/DevelopersToolbox/convert-size-package/blob/master/.github/SECURITY.md">
        <img src="https://img.shields.io/badge/Report%20Security%20Concern-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/DevelopersToolbox/convert-size-package/issues">
        <img src="https://img.shields.io/badge/Get%20Support-blue?style=for-the-badge" />
    </a>
</p>

## Overview

The File Size Converter module provides functions for converting file sizes between different units in both IEC (binary)
and SI (decimal) formats. It includes functionality for getting the full name of a unit from its abbreviation and
converting sizes between units.

## Features

- Convert sizes between different IEC units (e.g., Bytes to Kibibytes).
- Convert sizes between different SI units (e.g., Bytes to Kilobytes).
- Retrieve the full name of a unit from its abbreviation.
- Support for both IEC (binary) and SI (decimal) unit systems.

## Installation

```shell
pip install wolfsoftware.convert-size
```

## Usage

### Importing the Module

```python
import wolfsoftware.convert_size as fsc
```

### Converting Sizes

To convert a size between different units, use the `convert_size` function. You can specify whether to use SI units by setting the `si_units` parameter.

```python
# IEC conversion example
size_in_gib = fsc.convert_size(1024, 'MiB', 'GiB')
print(size_in_gib)  # Output: 1.0

# SI conversion example
size_in_gb = fsc.convert_size(1000, 'MB', 'GB', si_units=True)
print(size_in_gb)  # Output: 1.0
```

### Getting the Full Name of a Unit

To get the full name of a unit from its abbreviation, use the `get_name_from_code` function.

```python
# IEC unit name example
unit_name = fsc.get_name_from_code('KiB')
print(unit_name)  # Output: Kibibyte

# SI unit name example
unit_name = fsc.get_name_from_code('KB', si_units=True)
print(unit_name)  # Output: Kilobyte
```

## Functions

##### `convert_size(size: float, start_unit: str, end_unit: str, si_units: bool = False) -> float`

Convert a size between units, either IEC or SI.

- `size` (float): The original size.
- `start_unit` (str): The starting unit abbreviation.
- `end_unit` (str): The ending unit abbreviation.
- `si_units` (bool): If True, use SI units; otherwise, use IEC units.
- Returns (float): The converted size.
- Raises `ValueError`: If the unit abbreviations are not valid.

##### `get_name_from_code(unit: str, si_units: bool = False) -> str`

Get the full name of a unit from its abbreviation.

- `unit` (str): The unit abbreviation.
- `si_units` (bool): If True, use SI units; otherwise, use IEC units.
- Returns (str): The full name of the unit.
- Raises `ValueError`: If the unit abbreviation is not valid.

##### `get_name_from_code_iec(unit: str) -> str`

Get the full name of an IEC unit from its abbreviation.

- `unit` (str): The IEC unit abbreviation.
- Returns (str): The full name of the IEC unit.
- Raises `ValueError`: If the unit abbreviation is not valid.

##### `get_name_from_code_si(unit: str) -> str`

Get the full name of an SI unit from its abbreviation.

- `unit` (str): The SI unit abbreviation.
- Returns (str): The full name of the SI unit.
- Raises `ValueError`: If the unit abbreviation is not valid.

## Error Handling

The module raises `ValueError` exceptions for invalid unit abbreviations. Ensure that you handle these exceptions in your code:

```python
try:
    size_in_gib = fsc.convert_size(1024, 'MiB', 'GiB')
except ValueError as e:
    print(e)
```
<br />
<p align="right"><a href="https://wolfsoftware.com/"><img src="https://img.shields.io/badge/Created%20by%20Wolf%20on%20behalf%20of%20Wolf%20Software-blue?style=for-the-badge" /></a></p>
