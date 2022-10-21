def what_to_do(instructions: str):
    simon = "Simon says"
    if instructions.startswith(simon):
        return "I " + instructions[len(simon) + 1:]
    if instructions.endswith(simon):
        return "I " + instructions[:instructions.rindex(simon)]
    return "I won't do it!"
