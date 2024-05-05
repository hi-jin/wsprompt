import os
import sys
import gitmatch
import clipboard

from utils import (
    normalize_path,
    get_children,
    is_directory,
    print_ignored_message,
    print_matched_message,
    print_result_summary,
    read_file,
    read_ignore_patterns_if_exist,
)


def main():
    # -----Configure-----
    print("Do you want to use .gitignore for ignore patterns?\nIf you enter n, it will use .wspromptignore.")
    answer = input("use .gitignore? [y/N]: ").lower()
    if answer == "y":
        ignore_file_name = ".gitignore"
    else:
        ignore_file_name = ".wspromptignore"

    workspace_directory = normalize_path(sys.argv[1] if len(sys.argv) > 1 else ".")
    os.chdir(workspace_directory)
    workspace_directory = "."

    ignore_patterns: gitmatch.Gitignore = read_ignore_patterns_if_exist(
        workspace_directory=workspace_directory,
        ignore_file_name=ignore_file_name,
    )
    files_to_be_added = []

    # -----BFS------
    buffer = []
    buffer.append(workspace_directory)
    while buffer:
        file_or_directory = buffer.pop(0)
        should_ignore = bool(ignore_patterns.match(file_or_directory))
        if should_ignore:
            print_ignored_message(file_or_directory)
            continue
        if is_directory(file_or_directory):
            buffer.extend(get_children(file_or_directory))
        else:
            print_matched_message(file_or_directory)
            files_to_be_added.append(file_or_directory)

    # -----Export-----
    output = ""
    for file in files_to_be_added:
        output += f"-----File: {file}-----\n"
        output += f"Content:\n{read_file(file)}\n"
        output += "\n"
    clipboard.copy(output)
    print_result_summary(len(files_to_be_added))


if __name__ == "__main__":
    main()
