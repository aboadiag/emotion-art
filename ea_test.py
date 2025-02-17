import pandas as pd
import numpy as np

from PIL import Image
import requests
from io import BytesIO
import matplotlib.pyplot as plt

artemis_csv_fn = "./artemis_official_data/official_data/artemis_dataset_release_v0.csv"
df = pd.read_csv(artemis_csv_fn)

wikiart_url = "https://uploads7.wikiart.org/images/"

# print(len(df))
# df.head()


mode_df = df.groupby('painting')['emotion'].apply(lambda x: x.mode()[0]).reset_index()
df = mode_df
df.head()


def get_random_painting_by_emotion(emotion):
    df_subset = df[df['emotion'] == emotion].reset_index()
#     print(df_subset.head())
    ind = np.random.randint(0, len(df_subset))
#     print(ind)
    artemis_painting_name = df_subset.loc[ind, 'painting']
#     print(artemis_painting_name)
    artist_name, painting_name = artemis_painting_name.split('_')
#     print(artist_name, painting_name)
    painting_url = '{}{}/{}.jpg'.format(wikiart_url, artist_name, painting_name)
#     print(painting_url)


    response = requests.get(painting_url)
    img = Image.open(BytesIO(response.content))
    return img

#dictionary
img_dict = df['emotion'].unique()
dict_len = type(img_dict)
print(dict_len)
# print(len(dict_len))
# f, axarr = plt.subplots(nrows = 1, n)
# print(f"Number of rows {f}")
# print(f"Number of cols {axarr}")


# for emotion in dict_len:
#     try:
#         img = get_random_painting_by_emotion(emotion)
#         print(emotion)
#         # axarr[f, emotion].imshow(emotion)

#         # img.show()
#         # display(img)
#     except Exception as e:
#         print(e)