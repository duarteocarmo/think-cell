import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="thinkcell",
    version="20.3.1",
    author="Duarte O.Carmo",
    author_email="duarteocarmo@gmail.com",
    description="Small utility to automate the generation of think-cell graphs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="automation powerpoint thinkcell ppttc business consulting",
    licence="MIT",
    url="https://github.com/duarteocarmo/think-cell",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    project_urls={
        "Bug Reports": "https://github.com/duarteocarmo/think-cell/issues",
        "Say Thanks!": "https://duarteocarmo.com",
        "Source": "https://github.com/duarteocarmo/think-cell",
    },
)
