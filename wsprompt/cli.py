import argparse
import os


def parse_arguments():
    """
    Parses CLI arguments.
    """
    parser = argparse.ArgumentParser(
        description="Workspace Summarizer for LLMs. Gathers, filters, and formats codebase files into a single prompt.",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument(
        "directory",
        nargs="?",
        default=os.getcwd(),
        help="The project directory to summarize (Default: current directory)",
    )

    # --- Filtering Options ---
    parser.add_argument(
        "-i",
        "--ignore-file",
        help="Path to the ignore file to use (Default: auto-detects .wspromptignore or .gitignore)",
    )
    parser.add_argument("--include", nargs="+", help="List of file extensions to include (e.g., --include .py .js .md)")

    # --- Output Options ---
    parser.add_argument(
        "-o", "--output", help="Save the result to a file instead of the clipboard (e.g., -o output.txt)"
    )
    parser.add_argument("--tree", action="store_true", help="Prepend a file structure tree to the output")
    parser.add_argument(
        "--no-delimiters", action="store_true", help="Remove the '--- START/END OF [filepath] ---' delimiters"
    )

    # --- Other Options ---
    parser.add_argument(
        "-s",
        "--silent",
        action="store_true",
        help="Suppress progress messages and warnings (e.g., skipping binary files)",
    )

    return parser.parse_args()
