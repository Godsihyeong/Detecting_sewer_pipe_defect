# Development of a real-time sewer pipe defect detection algorithm using YOLO

<div aling="center">
  <img src="https://drive.google.com/uc?id=1imXeiCM30Tt7ayzGhTsozSrMdkZZ3OFm" width="500"/>
</div>

## Abstract

Sewer pipelines play a vital role in maintaining urban sanitation and public health, contributing to sustainable development. Early detection and maintenance of physical defects can reduce management costs and improve performance. Traditional CCTV inspections, consisting of two main stages: on-site video collection and office evaluation, face limitations such as technician fatigue and time consumption. To address these issues, a YOLO-based deep learning model for automated defect detection has been proposed. Using sewer pipeline interior images provided by AI Hub, this study classified eight defect types, including joint offsets, connector protrusions, and sediment deposits. The model achieved over 90% mAP accuracy (based on an IOU of 0.5) regardless of lighting and background noise. This technology is expected to enhance the efficiency of sewer maintenance, contributing to safer and more sustainable urban environments.

## Introduction

하수도 시스템은 도시화 및 인구 밀집 지역의 지속 가능한 발전에 있어 중대한 역할을 수행해왔다. 이와 같은 하수도 시스템의 중요성을 인지하고, 지방 정부 및 자치 단체는 하수 시스템의 효율적 관리와 유지를 위하여 2024년에 2조 7,692억 원의 예산을 책정하였고 2023년 대비 5,567억 원(25%) 증가하였다[(환경부, 2024)](https://korea.kr/common/download.do?fileId=197628336&tblKey=GMN). 하수도 시스템의 진단과 유지 보수는 구조물의 문제를 신속히 발견·해결하여 성능을 개선하고 관리 비용을 절감하며, 안정성과 최적의 서비스 제공을 목적으로 한다.

현재 CCTV 검사는 하수도 시스템의 진단 및 유지 보수 과정에서 필수적인 도구로 인식되고 있다. 레이저 기반 시스템, 초음파 센서, 적외선 열상 카메라 등 다른 기술적 접근법과 비교하였을 때, CCTV 검사는 분석에 용이한 시각적 자료를 제공한다는 장점을 갖는다. CCTV 검사 과정은 비디오 수집과 사무실에서 훈련된 기술자에 의한 비디오 분석으로, 두 주요 단계로 구성된다.

2022년 기준 총길이 16만 8,786km인 하수관로의 결함 발견을 위해 소요되는 시간과 기술자의 피로는 평가의 효율성에 부정적인 영향을 미칠 수 있다.[(환경부, 2024)](https://www.me.go.kr/home/web/policy_data/read.do?pagerOffset=0&maxPageItems=10&maxIndexPages=10&searchKey=title&searchValue=%ED%95%98%EC%88%98%EB%8F%84&menuId=10264&orgCd=&condition.toInpYmd=null&condition.fromInpYmd=null&condition.deleteYn=N&condition.deptNm=null&seq=8191). 최근 딥러닝 기술의 적용이 확대됨에 따라, 이러한 문제를 해결하기 위해 많은 연구자들이 컴퓨터 비전 기술을 이용한 자동화 접근 방식을 모색하고 있다[(임수현 et al., 2018)](https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002332399), [(Cheng et al., 2018)](https://www.sciencedirect.com/science/article/pii/S0926580518303273). 하지만 선행 연구의 경우는 Two stage detector로 추론 속도가 느려 실시간 탐지가 불가능하다는 한계가 존재한다.

특히, ‘You Only Look Once (YOLO)’ 알고리즘은 개체 감지 기술 중 하나로, 고속 처리와 높은 정확도를 겸비해 실시간 하수관로 결함 탐지에 특히 적합하다[(Redmon, J. et al., 2016)](https://arxiv.org/abs/1506.02640). 따라서, 본 논문에서는 YOLOv8을 활용하여 하수관로의 결함을 탐지하는 시스템을 제안한다. 본 시스템은 이미지를 다운사이징하여 기존보다 학습 및 추론 속도를 증가시키며, 실시간 탐지를 통해 기존의 수동 검사 방식의 한계를 극복하고, 하수도 관리의 효율성과 정확성을 개선하는 혁신적인 접근 방식을 제시한다.

## Workflow

<div aling="center">
  <img src="https://drive.google.com/uc?id=1vip5FNsdPhvMXYnOl3qEhkLUT1cMJFkw" width="500"/>
</div>

## Dataset
전체 이미지 다운로드 [클릭](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=&topMenu=&aihubDataSe=data&dataSetSn=139) 
```
Sewerpipe
├── Dataset
    ├── train
        ├── CC
        ├── CL
        ├── ...
        └── ...
    ├── val
    └── test
├── Dataset(+Background)
    ├── train
    ├── ...
    └── test
```

## Result
| mAP50 | Recall | Inference Time |
|:-----:|:-----:|:-----:|
| 0.7474 | 0.7001 | 11.1ms |

**Optimal Parameters**
| Batch size | Optimizer | Cos_lr | Pretrained | Background | Label Smoothing |
|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|
|     128    |    Adam    |    False   |    True    |      X     |     0.3    |

## Information
```bibtext
@inproceedings{title={Development of a real-time sewer pipe defect detection algorithm using YOLO},
author={Jo, Yeongjoo and Yeo, Sihyeong and Kim, Changwoo},
booktitle={2024 공동학술발표회}
year={2024},
month={March},
organization={Korean Society on Water Environment (한국물환경학회), Korean Society of Water & Wastewater (대한상하수도학회)},
}
```

## License
This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.
