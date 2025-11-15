import os
from gitignore_parser import parse_gitignore
from rich.tree import Tree
from rich.console import Console


def is_binary(file_path):
    """A simple check to see if a file is binary or text."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            f.read(1024)  # Test read first 1KB
        return False
    except UnicodeDecodeError:
        return True
    except Exception:
        return False


def load_ignore_rules(root_dir, ignore_file_path=None):
    """
    Loads the specified ignore file, or auto-detects .wspromptignore or .gitignore.
    """
    if ignore_file_path:
        ignore_path = os.path.abspath(ignore_file_path)
    else:
        wsprompt_ignore = os.path.join(root_dir, ".wspromptignore")
        git_ignore = os.path.join(root_dir, ".gitignore")

        if os.path.exists(wsprompt_ignore):
            ignore_path = wsprompt_ignore
        elif os.path.exists(git_ignore):
            ignore_path = git_ignore
        else:
            # No ignore file found.
            # Return a simple matcher that only ignores the .git directory.
            git_dir_path = os.path.join(root_dir, ".git")

            def git_only_matcher(path):
                abs_path = os.path.abspath(path)
                # Check if the path IS the git dir or is INSIDE the git dir
                return abs_path == git_dir_path or abs_path.startswith(git_dir_path + os.path.sep)

            return git_only_matcher

    if not os.path.exists(ignore_path):
        raise FileNotFoundError(f"Ignore file not found: {ignore_path}")

    # The parser needs the *path* to the file, not its content.
    base_dir = os.path.dirname(ignore_path)

    # --- BUG FIX ---
    # Pass the file PATH (ignore_path) directly to the parser.
    # The 'parse_gitignore' function will handle opening and reading it.
    # It also inherently handles ignoring .git as part of standard gitignore behavior.
    return parse_gitignore(ignore_path, base_dir=base_dir)


def discover_files(root_dir, ignore_matcher, include_exts=None, silent=False):
    """
    Recursively discovers files in a directory, applying filter rules.
    Returns a list of (relative_path, absolute_path) tuples.
    """
    included_files = []

    if include_exts and not isinstance(include_exts, (list, set)):
        include_exts = None

    ext_set = set(include_exts) if include_exts else None

    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=True):
        # Filter out ignored directories
        excluded_dirs = []
        for d in dirnames:
            dir_abs_path = os.path.join(dirpath, d)
            if ignore_matcher(dir_abs_path):
                excluded_dirs.append(d)

        for d in excluded_dirs:
            dirnames.remove(d)

        for filename in filenames:
            file_abs_path = os.path.join(dirpath, filename)

            # 1. Check ignore rules
            if ignore_matcher(file_abs_path):
                continue

            # 2. Check include extensions
            if ext_set:
                file_ext = os.path.splitext(filename)[1]
                if file_ext not in ext_set:
                    continue

            # 3. Check for binary files
            if is_binary(file_abs_path):
                if not silent:
                    # Translated to English
                    print(f"Notice: Skipping binary file - {os.path.relpath(file_abs_path, root_dir)}")
                continue

            # File passed all filters
            relative_path = os.path.relpath(file_abs_path, root_dir)
            included_files.append((relative_path.replace(os.path.sep, "/"), file_abs_path))

    return sorted(included_files)


def build_tree_string(file_paths):
    """
    Builds a string representation of a directory tree from a list of file paths.
    """
    if not file_paths:
        return ""

    # Translated to English
    tree = Tree("📂 Project Structure")
    nodes = {"": tree}  # Dictionary to store nodes by path

    for path in file_paths:
        parts = path.split("/")
        current_path = ""
        parent_node = tree

        for i, part in enumerate(parts):
            current_path = "/".join(parts[: i + 1])

            if current_path not in nodes:
                is_last_part = i == len(parts) - 1
                icon = "📄" if is_last_part else "📁"
                new_node = parent_node.add(f"{icon} {part}")
                nodes[current_path] = new_node
                parent_node = new_node
            else:
                parent_node = nodes[current_path]

    # Capture the tree print output as a string
    console = Console(record=True, width=120)
    console.print(tree)
    return console.export_text()
