from setuptools import setup

setup(
    name = "Organ Donation",
    version = "1.0",
    description = "organ donation app",
    packages = ["organdonationwebapp","tests"],
    package_dir={'models': 'organdonationwebapp/models','API':'organdonationwebapp/API', 'Hospital':'organdonationwebapp/Hospital', 'User':'organdonationwebapp/User'}
)