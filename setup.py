from setuptools import setup, find_packages

setup(
    name="operato",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],  # Add dependencies here, e.g., ["numpy"]
    author="P. Weißinger",
    author_email="philippa.weissinger@gmail.de",
    description="Input deck creation tool for (Open-)Radioss",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/PhRoWe/operato",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    test_suite="tests",
)
