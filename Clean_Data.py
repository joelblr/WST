import re

## to remove any unwanted data like Emoji
def removeEmoji(text) :
    # Regular expression pattern to match emojis
    emoji_pattern = re.compile(
        "[\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F700-\U0001F77F"  # alchemical symbols
        "\U0001F780-\U0001F7FF"  # Geometric Shapes
        "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
        "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
        "\U0001FA00-\U0001FA6F"  # Chess symbols, etc.
        "\U0001FA70-\U0001FAFF"  # Symbols for legacy scripts
        "\U00002702-\U000027B0"  # Miscellaneous symbols (e.g., checkmarks, hearts)
        "\U000024C2-\U0001F251"  # Enclosed characters
        "]+", flags=re.UNICODE)

    # Remove all emojis from the text
    clean_text = emoji_pattern.sub("", text)
    return clean_text


## to convert multi-line comment to a single line
def removeBrTag(html) :

    # Get the text from the inner div
    comment_text = str(html.div.div.get_text(separator=". ", strip=True))

    # Replace multiple consecutive dots with a single dot
    cleaned_text = re.sub(r'\.+', '.', comment_text)

    # Replace multiple dots with a single dot
    cleaned_text = " ".join(cleaned_text.split())
    return cleaned_text