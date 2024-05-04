# wsprompt: Workspace Summarizer for Chat Models

`wsprompt` is a sophisticated shell script designed to generate a concise and prompt-friendly representation of your workspace. It is particularly useful for sharing workspace details with large language models (LLMs) like ChatGPT. The script efficiently scans your project directory, concatenating file contents while respecting filters set through whitelist and blacklist configurations.

## Features

- **Directory Scanning**: Traverse directories recursively to compile file contents.
- **Configurable Filtering**: Utilize whitelist and blacklist configurations to selectively include or exclude files and directories.
- **Clipboard Integration**: Automatically copies the combined data to the clipboard, making it easy to share or use elsewhere.

## Requirements

- Unix-like environment (Linux, macOS)
- `pbcopy` on macOS or `xclip` on Linux for clipboard functionality

## Installation

`wsprompt` can be installed using either `git` or `wget`. Here are the instructions for both methods:

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

### Using wget

For a quick download without cloning the whole repository:

1. Download the script directly:
   ```bash
   wget https://github.com/hi-jin/wsprompt/raw/main/wsprompt -O wsprompt
   ```
2. Make the script executable:
   ```bash
   chmod +x wsprompt
   ```

## Usage

To run `wsprompt` from your project directory:
```bash
./wsprompt
```
You can also specify a directory explicitly if you wish to run it from somewhere else:
```bash
./wsprompt path/to/your/project
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
