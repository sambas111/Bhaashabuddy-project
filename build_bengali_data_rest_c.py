# Chapters 597–662: vocabulary + conversation


def add_chapters_597_662(out):
    """597-619: curated vocabulary tables; 620-662: curated conversation lines."""
    from build_bengali_vocab_597_619 import add_chapters_597_619
    from build_bengali_conversations_620_662 import add_chapters_620_662

    add_chapters_597_619(out)
    add_chapters_620_662(out)

