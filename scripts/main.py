import os
import argparse

root_folder = "./src"


def get_packages() -> list[str]:
    return [
        f"src.{name}"
        for name in os.listdir(root_folder)
        if os.path.isdir(os.path.join(root_folder, name)) and name != "__pycache__"
    ]


def add_challenge(name: list[str]) -> None:
    formatted_name = "_".join(name).lower()

    challenge_file = f"src/{formatted_name}/solution.py"
    test_file = f"tests/test_{formatted_name}.py"

    # create challenge folder
    os.makedirs(os.path.dirname(challenge_file), exist_ok=True)
    open(challenge_file, "w")

    print(f"File {challenge_file} created")

    # create test folder
    os.makedirs(os.path.dirname(test_file), exist_ok=True)
    open(test_file, "w")

    print(f"File {test_file} created")


# CLI
my_parser = argparse.ArgumentParser()
my_parser.add_argument(
    "--name",
    action="store",
    help="Name of the challenge",
    type=str,
    required=True,
    nargs="+",
)

args = my_parser.parse_args()

if args.name:
    add_challenge(name=args.name)
