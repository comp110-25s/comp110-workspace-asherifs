"""My first exercise in COMP110"""

__author__ = "730577291"


def greet(name: str) -> str:
    """A welcoming first function definition."""
    return "Hello, " + name + "!"


greet(name="Adam")
if __name__ == "__main__":
    print(greet(name=input("What is your name? ")))
