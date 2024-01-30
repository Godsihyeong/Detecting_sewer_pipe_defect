import os
import pandas as pd
from tqdm import tqdm

def df2txt(df, data, file_class, class_number):
    df.reset_index(drop=True, inplace=True)                              # index 재설정하고 기존 index 제거

    folder_path = '{}_folder'.format(file_class)
    current_directory = 'D:/sewer detect/folder'                         # annotations 정보를 담은 txt 파일 저장할 경로 설정

    # 폴더 생성
    folder_path_full = os.path.join(current_directory, folder_path)
    os.makedirs(folder_path_full, exist_ok=True)

    data1 = pd.DataFrame(data["images"])

    current_img_id = df.iloc[0]["image_id"]
    file_path = os.path.join(folder_path_full, data1[data1["id"] == current_img_id]["file_name"].values[0].split('.')[0] + ".txt")

    with tqdm(total=len(df), desc="Processing") as pbar:
        with open(file_path, "w", encoding="utf8") as file:
            for i, row in df.iterrows():
                img_id = row["image_id"]
                file_name = data1[data1["id"] == img_id]["file_name"].values[0]

                if img_id != current_img_id:
                    file.close()

                    # 새로운 파일 경로 설정
                    file_path = os.path.join(folder_path_full, file_name.split('.')[0] + ".txt")
                    file = open(file_path, "w", encoding="utf8")

                row_content = str(class_number) + ' ' + ' '.join(str(row[z]) for z in ["x", "y", "w", "h"])
                file.write(row_content + '\n')

                current_img_id = img_id
                pbar.update(1)

            
