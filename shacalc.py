# Python program to find SHA256 hash string of a file
import hashlib


def get_sha256(file_path):
    """
    This function calculates Sha 265 for files
    :param file_path:
    :return: list of HEX pairs[]
    """
    step = 2
    sha256_hash = hashlib.sha256()

    with open(file_path, "rb") as f:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)

    hex_sha = sha256_hash.hexdigest()

    hex_pairs = [hex_sha[pos:pos + step] for pos in range(0, len(hex_sha), step)]

    return hex_pairs
