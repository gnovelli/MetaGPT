from metagpt.software_company import generate_repo


def main() -> None:
    repo = generate_repo("Create a hello world script")
    print(repo)


if __name__ == "__main__":
    main()
