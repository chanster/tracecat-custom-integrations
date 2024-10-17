from typing import Annotated
from pydantic import Field
from tracecat_registry import registry


NUM_MAP = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


@registry.register(
    default_title="Map Number",
    display_group="Mapping",
    description="Performs a mapping of a word to a number",
    namespace="tracecat.examples.mapping",
)
def map_number(word: Annotated[str, Field(description="The word to map to a number")]):
    if word not in NUM_MAP:
        raise ValueError(f"Word {word} not found in mapping")
    return NUM_MAP[word]
