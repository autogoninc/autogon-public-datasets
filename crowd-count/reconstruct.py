import pandas as pd

def reconstruct_path(image_id: int) -> str:
    """Function transforms numerical image ID
    into a relative file path filling in leading zeros
    and adding file extension and directory.
    :param image_id: Image ID
    :return: Relative path to the image
    """
    image_id = str(image_id).rjust(6, '0')
    return f'frames/seq_{image_id}.jpg'

data = pd.read_csv('labels.csv')
data['path'] = data['id'].apply(reconstruct_path)

data.to_csv('data.csv')
