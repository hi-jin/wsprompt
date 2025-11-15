from setuptools import setup, find_packages

setup(
    name="wsprompt",
    version="0.2.0",
    packages=find_packages(),
    author="hi-jin",
    author_email="sudwlsdks@gmail.com",
    description="Easily summarize your codebase for use with large language models",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/hi-jin/wsprompt",
    install_requires=[
        "pyperclip",
        "gitignore-parser",
        "rich",
    ],
    entry_points={
        "console_scripts": [
            "wsprompt = wsprompt.__main__:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
