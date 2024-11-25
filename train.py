import ultralytics
import itertools

ultralytics.checks()

from ultralytics import YOLO
import torch

model = YOLO('./yolov8n.pt')

# 파라미터 조합 정의
batch_sizes = [16, 32]
optimizers = ["SGD","AdamW"]
cos_lr_options = [True, False]
label_smoothing_options = [0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4]
mix_up_options = [0, 0.1, 0.5]

# 파라미터 조합 생성
parameter_combinations = list(itertools.product(batch_sizes, optimizers, cos_lr_options, label_smoothing_options, mix_up_options))

# 각 파라미터 조합에 대해 모델을 훈련
for batch_size, optimizer_, cos_lr_option, label_smoothing, mix_up in parameter_combinations:
    # 모델 이름 생성
    model_name = f"yolov8n_{batch_size}_{optimizer_}_coslr{cos_lr_option}_labelsmooth{label_smoothing}_mixup{mix_up}"
    MODEL = f"{model_name}"
    
    # 모델 초기화
    model_x1 = YOLO('./yolov8n.pt')
    
    # 모델 훈련
    results = model_x1.train(
        data="./sewer.yaml",
        imgsz=640,
        epochs=300,
        patience=5,
        batch=batch_size,
        workers=16,
        device=0,
        project="yolov8n",
        name=f"{MODEL}",
        seed=0,
        optimizer=optimizer_,
        lr0=1e-3,
        cos_lr=cos_lr_option,
        label_smoothing=label_smoothing,
        mixup=mix_up,
        save=True,
        exist_ok=True,
        verbose=True,
        plots=True
    )