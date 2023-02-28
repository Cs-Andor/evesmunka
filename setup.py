setup(
    name="evesmunka-by-csete-andor",
    version="1.0.0",
    description="Évesmunka program 2022-23. Készítette Csete Andor",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/realpython/reader",
    author="Csete Andor",
    author_email="info@realpython.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    packages=["reader"],
    include_package_data=True,
    install_requires=[
        "feedparser", "html2text", "importlib_resources", "typing"
    ],
    entry_points={"console_scripts": ["realpython=reader.__main__:main"]},
)
