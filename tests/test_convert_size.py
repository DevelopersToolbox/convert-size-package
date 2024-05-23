"""
This test module provides unit tests for the File Size Converter module using pytest.
It includes tests for versioning, name retrieval, and size conversion functions.
"""

from typing import Optional
import importlib.metadata
import pytest
import wolfsoftware.convert_size as fsc


def test_version() -> None:
    """
    Test that a version is defined.

    Should return the version of the package.
    """
    version: Optional[str] = None

    try:
        version = importlib.metadata.version('wolfsoftware.convert_size')
    except importlib.metadata.PackageNotFoundError:
        version = None

    assert version is not None, "Version should be set"  # nosec: B101
    assert version != 'unknown', f"Expected version, but got {version}"  # nosec: B101


def test_get_name_from_code_iec() -> None:
    """
    Test the retrieval of IEC unit names from their abbreviations.
    """
    assert fsc.get_name_from_code_iec('KiB') == 'Kibibyte'  # nosec: B101
    assert fsc.get_name_from_code_iec('MiB') == 'Mebibyte'  # nosec: B101
    with pytest.raises(ValueError):
        fsc.get_name_from_code_iec('Invalid')


def test_get_name_from_code_si() -> None:
    """
    Test the retrieval of SI unit names from their abbreviations.
    """
    assert fsc.get_name_from_code_si('KB') == 'Kilobyte'  # nosec: B101
    assert fsc.get_name_from_code_si('MB') == 'Megabyte'  # nosec: B101
    with pytest.raises(ValueError):
        fsc.get_name_from_code_si('Invalid')


def test_get_name_from_code() -> None:
    """
    Test the retrieval of unit names from their abbreviations with optional SI units.
    """
    assert fsc.get_name_from_code('KiB') == 'Kibibyte'  # nosec: B101
    assert fsc.get_name_from_code('KB', si_units=True) == 'Kilobyte'  # nosec: B101
    with pytest.raises(ValueError):
        fsc.get_name_from_code('Invalid')


def test_convert_size_iec() -> None:
    """
    Test the conversion of sizes between IEC units.
    """
    assert fsc.convert_size_iec(1024, 'MiB', 'GiB') == 1.0  # nosec: B101
    assert fsc.convert_size_iec(1, 'GiB', 'MiB') == 1024.0  # nosec: B101
    assert fsc.convert_size_iec(0, 'B', 'KiB') == 0.0  # nosec: B101
    with pytest.raises(ValueError):
        fsc.convert_size_iec(1024, 'Invalid', 'GiB')
    with pytest.raises(ValueError):
        fsc.convert_size_iec(1024, 'MiB', 'Invalid')


def test_convert_size_si() -> None:
    """
    Test the conversion of sizes between SI units.
    """
    assert fsc.convert_size_si(1000, 'MB', 'GB') == 1.0  # nosec: B101
    assert fsc.convert_size_si(1, 'GB', 'MB') == 1000.0  # nosec: B101
    assert fsc.convert_size_si(0, 'B', 'KB') == 0.0  # nosec: B101
    with pytest.raises(ValueError):
        fsc.convert_size_si(1000, 'Invalid', 'GB')
    with pytest.raises(ValueError):
        fsc.convert_size_si(1000, 'MB', 'Invalid')


def test_convert_size() -> None:
    """
    Test the conversion of sizes between units with optional SI units.
    """
    assert fsc.convert_size(1024, 'MiB', 'GiB') == 1.0  # nosec: B101
    assert fsc.convert_size(1000, 'MB', 'GB', si_units=True) == 1.0  # nosec: B101
    assert fsc.convert_size(0, 'B', 'KiB') == 0.0  # nosec: B101
    assert fsc.convert_size(0, 'B', 'KB', si_units=True) == 0.0  # nosec: B101
    with pytest.raises(ValueError):
        fsc.convert_size(1024, 'Invalid', 'GiB')
    with pytest.raises(ValueError):
        fsc.convert_size(1000, 'MB', 'Invalid', si_units=True)
