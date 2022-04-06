import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="notionpy",
    version="1.0.0",
    description="integrate notion api with your workflow",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/kareemmahlees/NotionPy.git",
    author="Kareem Ebrahim",
    author_email="kareemmahlees@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
    packages=["reader"],
    include_package_data=True,
    install_requires=["feedparser", "html2text"],
    entry_points={
        "console_scripts": [
            "realpython=reader.__main__:main",
        ]
    },
)
