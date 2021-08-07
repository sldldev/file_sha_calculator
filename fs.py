import os

SAFE_LOC = r"..\Safe_Path"


def create_path(hex_list):
    """
    This function responsible to create path in SAFE_LOC
    :param hex_list: list of hex_pairs
    :return: path to created folder
    """
    # Combine list in to string
    hex_path = "\\".join(hex_list[0: len(hex_list) - 1])

    # Make path
    save_path = os.path.join(SAFE_LOC, hex_path)

    # Log
    print(save_path)

    # Create all subdirs
    try:
        os.makedirs(save_path)
    except FileExistsError:
        pass

    return save_path
