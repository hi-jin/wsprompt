import os
import pyperclip
from wsprompt.cli import parse_arguments
from wsprompt.utils import load_ignore_rules, discover_files, build_tree_string


def format_file_content(relative_path, content, no_delimiters):
    """Formats the file content with standard delimiters."""
    if no_delimiters:
        return content + "\n\n"

    header = f"--- START OF {relative_path} ---\n"
    footer = f"\n--- END OF {relative_path} ---\n\n"
    return header + content + footer


def main():
    args = parse_arguments()
    root_dir = os.path.abspath(args.directory)

    if not os.path.isdir(root_dir):
        print(f"Error: Invalid directory not found: {root_dir}")
        return

    try:
        # 1. Load Ignore Rules
        ignore_matcher = load_ignore_rules(root_dir, args.ignore_file)
        if not args.silent:
            print(f"Scanning directory: '{root_dir}'...")

        # 2. Discover & Filter Files
        files_to_process = discover_files(root_dir, ignore_matcher, args.include, args.silent)

        if not files_to_process:
            print("Error: No files found to process. (Check ignore settings or --include options)")
            return

        # 3. Build Tree (Optional)
        tree_str = ""
        if args.tree:
            relative_paths = [r for r, a in files_to_process]
            tree_str = build_tree_string(relative_paths) + "\n\n"

        # 4. Build single output string (Token counting and chunking removed)
        full_output_string = tree_str
        total_files = len(files_to_process)

        for idx, (relative_path, absolute_path) in enumerate(files_to_process, 1):
            if not args.silent:
                print(f"[{idx}/{total_files}] Processing: {relative_path}")

            try:
                with open(absolute_path, "r", encoding="utf-8") as f:
                    content = f.read()
            except Exception as e:
                if not args.silent:
                    print(f"Warning: Could not read file. Skipping - {relative_path} (Error: {e})")
                continue

            formatted_file = format_file_content(relative_path, content, args.no_delimiters)
            full_output_string += formatted_file

        # 5. Output results
        if not full_output_string.strip():
            print("\n🤔 No content processed.")
            return

        if args.output:
            # Save to file
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(full_output_string)
            print(f"\n✅ Success! Content from {total_files} files saved to '{args.output}'.")

        else:
            # Copy to clipboard
            pyperclip.copy(full_output_string)
            print(f"\n✅ Success! Content from {total_files} files copied to clipboard.")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
