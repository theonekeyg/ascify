ascii_tokens = {
    "@": 200,
    "#": 155,
    "&": 100,
    "*": 50,
    ".": 0
}

def default_rendition(img_slice):
    for char, threshold in ascii_tokens.items():
        if (img_slice.mean() >= threshold):
            return char

def colorwise_rendition(img_slice):
    for char, threshold in ascii_tokens.items():
        if (img_slice.max() >= threshold):
            return char
