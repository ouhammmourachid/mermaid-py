import os
import shutil


def pytest_configure(config):
    """
    A pytest hook to customize the terminal summary.
    """
    # Get the environment variable
    mermaid_server = os.getenv("MERMAID_INK_SERVER", "Not Set")

    mermaid_server = (
        f"\033[92m{mermaid_server}\033[0m"
        if mermaid_server != "Not Set"
        else "\033[91mNot Set\033[0m"
    )
    # Print the environment variable at the start
    word = " Custom Environment Information "
    line = word.center(shutil.get_terminal_size(fallback=(80, 20))[0], "=")
    print(f"\033[1m{line}\033[0m")
    print(f"\033[92mMERMAID_INK_SERVER \033[0m: {mermaid_server}")
