import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="officepy",
    version="0.0.1",
    author="liujuanjuan1984",
    author_email="qiaoanlu@163.com",
    description="common python code for office use. like dir,file,etc.",
    keywords=["office"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/liujuanjuan1984/officepy",
    project_urls={
        "Github Repo": "https://github.com/liujuanjuan1984/officepy",
        "Bug Tracker": "https://github.com/liujuanjuan1984/officepy/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=[
        "pandas",
        "selenium",
        "pytesseract",
        "black",
        "pillow",
        "pytest",
        "numpy",
        "html2text",
        "zipfile",
    ],
)