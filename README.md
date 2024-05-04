# wsprompt: Workspace Summarizer for Chat Models

`wsprompt` is a sophisticated shell script designed to generate a concise and prompt-friendly representation of your workspace. It is particularly useful for sharing workspace details with large language models (LLMs) like ChatGPT. The script efficiently scans your project directory, concatenating file contents while respecting filters set through whitelist and blacklist configurations.

> [!warning]
> This repository is still under active development.

## 🚀 Demo Overview 🔥🔥
This section provides a walkthrough of using `wsprompt` with a hypothetical project structure. Our goal is to demonstrate how you can include important source code files in the prompt, while excluding directories like build artifacts and log files.

### 1. Project Structure

Let's imagine our project directory looks like this:

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
└── .wspromptconfig
```

In this example, you want to include source code from the `src/` and `tests/` directories but exclude the `build/` directory and any `.log` files scattered throughout.

### 2. blacklist/whitelist Configuration

To configure `wsprompt` to meet the above requirements, you would create a `.wspromptconfig` file in the root of your workspace:

```plaintext
blacklist:
build/
*.log
```

### 3. Running wsprompt

After setting up the `.wspromptconfig` file, run the `wsprompt` script:

```bash
wsprompt path/to/my_project
```

or 

```bash
cd path/to/my_project
wsprompt
```

### 4. Get output and ask ChatGPT❗❗

When `wsprompt` processes the given project with the specified configurations, it will skip the `build/` directory and all `.log` files, only including the contents from the `src/` and `tests/` directories.  
The script would output the contents of `main.cpp`, `utils.h`, `utils.cpp`, and `test_main.cpp`, and this data would be copied to the clipboard, ready for use in sharing with LLMs!

```bash
Starting wsprompt in directory: /Users/hi-jin/Developer/wsprompt

Processing:
  Temporary file created at: /var/folders/c7/jxqvj2ts20j3jr3d6ckyhhr40000gn/T/tmp.sFg3WfUsLD
  Processing directory: /Users/hi-jin/Developer/wsprompt
    Adding file content from: /Users/hi-jin/Developer/wsprompt/LICENSE
    Adding file content from: /Users/hi-jin/Developer/wsprompt/wsprompt
    Adding file content from: /Users/hi-jin/Developer/wsprompt/README.md
    Skipping hidden entry: /Users/hi-jin/Developer/wsprompt/.git
  Processing directory: /Users/hi-jin/Developer/wsprompt

Results:
  Processed 3 files and 1 directories
  Included 3 files/directories
  Excluded 1 files/directories
  Content copied to clipboard using pbcopy

Workspace prompt is copied to clipboard.
```

## Features

- **Directory Scanning**: Traverse directories recursively to compile file contents.
- **Configurable Filtering**: Utilize whitelist and blacklist configurations to selectively include or exclude files and directories.
- **Clipboard Integration**: Automatically copies the combined data to the clipboard, making it easy to share or use elsewhere.

## Requirements

- Unix-like environment (Linux, macOS)
- `pbcopy` on macOS or `xclip` on Linux for clipboard functionality

## 🛠️ Installation

`wsprompt` can be installed using `git`. Here are the instructions:

### Using Git

If you prefer to use Git, which is ideal for receiving updates and contributing to the project:

1. Clone the repository:
   ```bash
   git clone https://github.com/hi-jin/wsprompt.git
   ```
2. Navigate to the script directory:
   ```bash
   cd wsprompt
   ```
3. (Optional) Register PATH
   ```bash
   echo "export PATH=\"\$PATH:$(pwd)\"" >> ~/.zshrc
   source ~/.zshrc
   ```
> [!Note]
> Change .zshrc to your shell's one.

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

Create a `.wspromptconfig` file in the root of your workspace to control which files and directories are processed. Here's how you can structure this file:

```plaintext
# Whitelist
whitelist:
path/to/include1
path/to/include2

# Blacklist
blacklist:
path/to/exclude1
path/to/exclude2
```

- **Whitelist**: Only the paths listed here will be included in the scan.
- **Blacklist**: Paths listed here will be excluded from the scan.

## Contributing

Contributions are what make the open-source community thrive. Here’s how you can contribute:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
