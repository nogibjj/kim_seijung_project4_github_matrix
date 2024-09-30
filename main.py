import random


def generate_sentence():
    """Function to generate a simple 6-word sentence"""
    # Word lists for different parts of speech
    articles = ["the", "a"]
    nouns = ["dog", "cat", "fox", "boy", "girl", "bird", "park", "car"]
    verbs = ["jumps", "runs", "flies", "eats", "drinks", "sings", "drives"]
    adjectives = ["kind", "lazy", "brown", "happy", "hungry", "small"]

    # Constructing a sentence
    # Use article + adjective + noun + verb + article + noun
    sentence = (
        f"{random.choice(articles).capitalize()} {random.choice(adjectives)} "
        f"{random.choice(nouns)} {random.choice(verbs)} {random.choice(articles)} "
        f"{random.choice(nouns)}."
    )
    return sentence


if __name__ == "__main__":
    print(generate_sentence())
