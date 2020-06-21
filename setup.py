from setuptools import setup, find_packages
setup(
    name="tse_data",
    version="0.1",
    packages=find_packages(),
    scripts=["results.py"],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=["pandas", "numpy", "requests", "zipfile", "os"],

    package_data={
        # If any package contains *.txt or *.rst files, include them:
        "": ["*.txt", "*.rst"],
        # And include any *.msg files found in the "hello" package, too:
        "hello": ["*.msg"],
    },

    # metadata to display on PyPI
    author="Helson Gomes de Souza",
    author_email="helson@alu.ufc.br",
    description="Download and clean data on brazilian elections",
    keywords="elections, tse, data, Brazil",
    project_urls={
        "Bug Tracker": "https://github.com/Helson-Gomes"
    },
    classifiers=[
        "License :: OSI Approved :: Python Software Foundation License"
    ]

    # could also include long_description, download_url, etc.
)
