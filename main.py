"""The Worst App Idea Ever Pitched -- make.fun entry.

One line: a pitch for the worst app idea ever. Confidently terrible --
Napkin lets you pay your landlord in exposure and rate your own
eviction five stars. The program validates the entry, prints it, and
writes it to /output/entry.txt.

Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

LINE = (
    "Introducing Napkin, the app that lets you Venmo your landlord in "
    "exposure and rate your own eviction five stars."
)

LIMIT = 200
TARGET = "/output/entry.txt"


def check_entry(line):
    """Accept exactly one non-blank line within the limit."""
    if not isinstance(line, str):
        raise ValueError("entry must be text")
    if not line or line != line.strip():
        raise ValueError("entry must be a single non-blank line")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must not contain a newline")
    if len(line) > LIMIT:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(line), LIMIT)
        )
    return line


def check_shape(line):
    """The worst app pitch must name the app and close."""
    if "app" not in line.lower():
        raise ValueError("entry must mention the app")
    if not line.endswith("."):
        raise ValueError("pitch must end with a period")
    return line


def write_entry(line):
    """Print the line and store it in /output/entry.txt."""
    print(line)
    os.makedirs(os.path.dirname(TARGET), exist_ok=True)
    with open(TARGET, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


def run():
    # Only a well-formed entry is ever printed or stored.
    write_entry(check_shape(check_entry(LINE)))


if __name__ == "__main__":
    run()
