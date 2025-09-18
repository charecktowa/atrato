import random

import pandas as pd


def random_note(num_students: int) -> list[int]:
    return [random.randint(1, 10) for _ in range(num_students)]


def create_students_df(ids: list[int], names: list[str]) -> pd.DataFrame:

    data = {
        "id": ids,
        "name": names,
        "note1": random_note(len(ids)),
        "note2": random_note(len(ids)),
        "note3": random_note(len(ids)),
    }

    return pd.DataFrame(data)


def add_average_column(df: pd.DataFrame) -> pd.DataFrame:
    df["average"] = df[["note1", "note2", "note3"]].mean(axis=1)
    return df


def main():
    ids = [1, 2, 3, 4, 5, 6]
    names = ["Juan", "Carlos", "Elias", "Saúl", "Adrian", "Raúl"]

    students = create_students_df(ids, names)

    print(students)

    # Since it asks to create a new column with the average of the notes
    new_students = add_average_column(students)

    print(new_students)


if __name__ == "__main__":
    main()
