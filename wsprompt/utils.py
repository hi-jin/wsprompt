import os
import gitmatch


def normalize_path(path: str) -> str:
    return os.path.normpath(path)


def get_children(directory: str):
    # on Error, pass it
    result = []
    try:
        list_dir = os.listdir(directory)
    except Exception as e:
        print(e)
        return result

    for child in list_dir:
        try:
            result.append(normalize_path(os.path.join(directory, child)))
        except Exception as e:
            print(e)
            pass
    return result


def is_directory(file_or_directory: str) -> bool:
    return os.path.isdir(file_or_directory)


def print_ignored_message(file_or_directory: str):
    # Colored output (red)
    print(f"\033[91mIgnored {file_or_directory}\033[0m")


def print_matched_message(file_or_directory: str):
    # Colored output (green)
    print(f"\033[92mMatched {file_or_directory}\033[0m")


def print_result_summary(count: int):
    print(f"Matched {count} files")


def read_file(file: str) -> str:
    with open(file, "r", errors="ignore") as f:
        return f.read()


def read_ignore_patterns_if_exist(
    workspace_directory: str,
    ignore_file_name=".wspromptignore",
):
    ignore_file = os.path.join(workspace_directory, ignore_file_name)
    if not os.path.exists(ignore_file):
        return gitmatch.compile([])
    return gitmatch.compile(open(ignore_file).readlines())
