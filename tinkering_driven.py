def tinkering_driven(awesome):
    """Enjoy awesome with
    Tinkering-Driven Method
    """
    if awesome is familiar: return
    if awesome is not interesting: return
    if awesome is not affordable: return

    taste(awesome)

    new_awesomes = disassemble(awesome)
    for new_awesome in new_awesomes:
        tinkering_driven(new_awesome)

    reassemble(new_awesomes)


tinkering_driven(life)

