"""Shared terminal UI styling for vocalyx."""

from colorama import init, Fore, Style

init()


def info(msg: str) -> str:
    return f"{Fore.CYAN}{msg}{Style.RESET_ALL}"


def success(msg: str) -> str:
    return f"{Fore.GREEN}{msg}{Style.RESET_ALL}"


def warn(msg: str) -> str:
    return f"{Fore.YELLOW}{msg}{Style.RESET_ALL}"


def error(msg: str) -> str:
    return f"{Fore.RED}{msg}{Style.RESET_ALL}"


def highlight(msg: str) -> str:
    return f"{Fore.CYAN}{msg}{Style.RESET_ALL}"
