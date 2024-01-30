import pandas as pd

# json에서 필요한 정보만 추출하는 과정

def convert_bbox(bbox,width,height):
    dw = 1.0 / width
    dh = 1.0 / height
    x = bbox[0] + bbox[2] / 2.0
    y = bbox[1] + bbox[3] / 2.0
    w = bbox[2]
    h = bbox[3]
    return [x * dw, y * dh, w * dw, h * dh]

def open_optimized(filename, file_list):
    # 필요한 컬럼 정의
    keys = ['id', 'image_id', 'category_id', 'area', 'bbox']

    # 이미지와 어노테이션 데이터를 DataFrame으로 변환
    images_df = pd.DataFrame(filename["images"])
    annotations_df = pd.DataFrame(filename["annotations"])

    # file_list에 해당하는 이미지 ID 추출
    images_df = images_df[images_df["file_name"].isin(file_list)]
    image_ids = images_df["id"].tolist()

    # 해당하는 이미지 ID에 대한 어노테이션 필터링
    filtered_annotations1 = annotations_df[annotations_df["image_id"].isin(image_ids)]
    filtered_annotations1 = filtered_annotations1[keys]
    selected= images_df[['id', 'width', 'height']]
    # A와 selected_cols_B 데이터프레임을 "id"와 "id" 열을 기준으로 병합
    filtered_annotations = filtered_annotations1.merge(selected, left_on='image_id', right_on='id', how='inner')
    filtered_annotations["bbox"] = filtered_annotations.apply(lambda row: convert_bbox(row["bbox"], row["width"], row["height"]), axis=1)



    # bbox 컬럼을 분할
    bbox_df = pd.DataFrame(filtered_annotations["bbox"].tolist(), columns=['x', 'y', 'w', 'h'])
    filtered_annotations = pd.concat([filtered_annotations, bbox_df], axis=1)
    filtered_annotations.drop('bbox', axis=1, inplace=True)

    return filtered_annotations
