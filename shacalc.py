# Python program to find SHA256 hash string of a file
import hashlib


def split_sha_to_hex_pairs(hex_sha):
    """
    This function breaks 64 chars hex sha256 in to list of hex_pairs
    :param hex_sha:
    :return:
    """
    step = 2
    hex_pairs = [hex_sha[pos:pos + step] for pos in range(0, len(hex_sha), step)]
    return hex_pairs


def get_sha256(file_path):
    """
    This function calculates Sha 265 for files
    :param file_path:
    :return: list of HEX pairs[]
    """

    sha256_hash = hashlib.sha256()

    with open(file_path, "rb") as f:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)

    hex_sha = sha256_hash.hexdigest()
    hex_pairs = split_sha_to_hex_pairs(hex_sha)

    return hex_pairs
