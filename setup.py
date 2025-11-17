from setuptools import setup, find_packages
from pathlib import Path
# Determine project root directory
this_directory = Path(__file__).parent
try:
    # Read raw lines from requirements.txt
    raw_requirements = (this_directory / "requirements.txt").read_text().splitlines()
    # Filter out editable/local lines (e.g. '-e .'), comments, and VCS/URL installs
    requirements = [
        r.strip()
        for r in raw_requirements
        if r and r.strip() and not r.strip().startswith((
            "-e", "--editable", "#", "git+", "http:", "https:", "file:"
        ))
    ]
except Exception:
    # If requirements file is missing or unreadable, fall back to an empty list
    requirements = []

# Package metadata and configuration
setup(
    name="mlproject",
    version="0.1.0",
    description="Machine learning project",
    author="Jamalla Zawia",
    packages=find_packages(),
    include_package_data=True,
    # Install the packages listed in requirements.txt
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.8",
)
