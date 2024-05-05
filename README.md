# wsprompt: Workspace Summarizer for Chat Models

`wsprompt` is a Python tool designed to generate a concise and prompt-friendly representation of your workspace. It is particularly useful for sharing workspace details with large language models (LLMs) like ChatGPT. The tool scans your project directory, concatenating file contents while respecting filters set through configurations like `.wspromptignore` or `.gitignore`.

> [!warning]
> This repository is still under active development.

## 🚀 Demo Overview 🔥🔥
This section provides a walkthrough of using `wsprompt` with a hypothetical project structure. Our goal is to demonstrate how you can include important source code files in the prompt, while excluding directories like build artifacts and log files.

### 1. Project Structure

Imagine a project directory like this:

```
my_project/
├── build/
│   └── output.o
├── logs/
│   ├── debug.log
│   └── error.log
├── src/
│   ├── main.cpp
│   ├── utils.h
│   └── utils.cpp
└── tests/
│   └── test_main.cpp
└── .wspromptignore
```

You want to include source code from the `src/` and `tests/` directories but exclude the `build/` directory and any `.log` files.

### 2. blacklist/whitelist Configuration

Configure `wsprompt` using the `.wspromptignore` file in the root of your workspace:
(Or, you can simply use existing .gitignore!)

```plaintext
build/
*.log
```

### 3. Running wsprompt

After setting up the ignore file, run the `wsprompt` script:

```bash
wsprompt path/to/my_project
```

or 

```bash
cd path/to/my_project
wsprompt
```

### 4. Get output and ask ChatGPT❗❗

The script will skip the `build/` directory and all `.log` files, only including the contents from the `src/` and `tests/` directories. The data is copied to the clipboard, ready for sharing with LLMs!

## Features

- **Directory Scanning**: Traverse directories recursively to compile file contents.
- **Configurable Filtering**: Utilize whitelist and blacklist configurations to selectively include or exclude files and directories.
- **Clipboard Integration**: Automatically copies the combined data to the clipboard, making it easy to share or use elsewhere.

## Requirements

- Unix-like environment (Linux, macOS)
- Python 3.8 or higher

## 🛠️ Installation

`wsprompt` can be installed using `pip` for easy updates and dependency management:

```bash
git clone https://github.com/hi-jin/wsprompt.git
cd wsprompt
pip install -e .
```

## Usage

To run `wsprompt` from your project directory:
```bash
wsprompt
```
You can also specify a directory explicitly if you wish to run it from somewhere else:
```bash
wsprompt path/to/your/project
```

## Configuration

Create a `.wspromptignore` or use `.gitignore` in the root of your workspace to control which files and directories are processed. You can choose which to use when prompted by the script. The pattern format is identical to that of `.gitignore`.

## Contributing

Contributions are what make the open-source community thrive. Here’s how you can contribute:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
