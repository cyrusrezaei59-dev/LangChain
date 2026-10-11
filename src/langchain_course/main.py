import os

from dotenv import load_dotenv

load_dotenv()


def main() -> None:
    print("Hello, world!")
    print(os.environ.get("OPENAI_API_KEY"))
    print("**********************************")
    print("///////////////////////////////////////////")
    print(os.environ.get("GOOGLE_API_KEY"))
    


if __name__ == "__main__":
    main()
    