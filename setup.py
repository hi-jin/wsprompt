from setuptools import setup, find_packages

setup(
    name="wsprompt",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "gitmatch",
        "clipboard",
    ],
    entry_points={
        "console_scripts": [
            "wsprompt = wsprompt.main:main",
        ],
    },
    python_requires=">=3.8",
    description="wsprompt: Easily summarize your codebase for use with large language models",
    author="Hyungjin Ahn",
    author_email="sudwlsdks@gmail.com",
    license="MIT",
)
