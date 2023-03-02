#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

requirements = [
    "gcsa>=2.0.1",
]

test_requirements = [
    "pytest>=3",
]

setup(
    name="gcsa-slots",
    description="Simple API for Google Calendar management with slots extension (dates and times available for scheduling)",
    long_description=readme,
    author="Leandro César Cassimiro",
    author_email="ccleandroc@gmail.com",
    url="https://github.com/leandcesar/google-calendar-simple-api-slots",
    version="0.1.0",
    license="MIT",
    python_requires=">=3.7",
    packages=find_packages(include=["gcsa_slots", "gcsa_slots.*"]),
    include_package_data=True,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords=[
        "python",
        "conference",
        "calendar",
        "hangouts",
        "python-library",
        "event",
        "conferences",
        "google-calendar",
        "pip",
        "recurrence",
        "google-calendar-api",
        "attendee",
        "gcsa",
        "gcsa-slots",
        "slots",
        "scheduling",
    ],
    zip_safe=False,
    install_requires=requirements,
    tests_require=test_requirements,
    test_suite="tests",
)
