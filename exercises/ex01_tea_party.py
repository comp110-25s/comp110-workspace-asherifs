"""A program to help plan a tea party"""

__author__: str = "730577291"


def main_planner(guests: int) -> None:
    """This function calls and prints all the below functions to get us our program."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Calculate the number of tea bags for each guest attending"""
    return people * 2


def treats(people: int) -> int:
    """Calculate the number of treats per guest attending"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """To calculate the cost of tea bags and treats combined"""
    return float(tea_count * 0.50 + treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
