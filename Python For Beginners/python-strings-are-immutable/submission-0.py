def remove_fourth_character(word: str) -> str:
    part1 = word[:3]
    part2 = word[4:]
    return part1 + part2


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
