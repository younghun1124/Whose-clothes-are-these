
# Whose Clothes Are These?

This site uses the Residual Neural Network (ResNet) model to find the most similar clothing photos among pre-stored images.

## Problem Situation

### “Where are all my clothes?”
Clothes often get mixed up, leading to instances where they end up unused in a sibling's closet for months.
With children grown up, it becomes challenging to differentiate between the clothes of different family members when doing laundry, especially when not everyone is at home.

## Implementation Method

1. **Flask Python Server**: Allows all family members to use the service on their smartphones.
2. **Image Preprocessing**: Uses OpenCV for preprocessing and torchvision's pretrained resnet50 model to extract features from clothing photos.
3. **Feature Comparison**:
   Code for comparison: 
   ```python
   similarity = np.dot(target_features, features) / (np.linalg.norm(target_features) * np.linalg.norm(features))
   ```
   <img width="481" alt="image" src="https://github.com/younghun1124/Whose-clothes-are-these/assets/83543030/212e63c3-0848-4513-b9c0-8e48087cf917">

   
4. **Results Display**: Shows photos of clothes and their owners' information in order of similarity in an HTML list.

## How to Use

### Find the Owner of Your Clothes

1. From the Find Similar Clothes menu, select a file.
2. Click the “Whose clothes is this?” button to start the comparison.

#### Selected File Image
![Selected File Image](https://github.com/younghun1124/Whose-clothes-are-these/assets/83543030/64fc1062-5fbf-4b96-b0f3-75282348f12b)

#### Results
![Comparison Results](https://github.com/younghun1124/Whose-clothes-are-these/assets/83543030/81356ea7-b02b-45ea-9b94-b32e66dc83f1)

#### Most Similar Images
![Most Similar Images](https://github.com/younghun1124/Whose-clothes-are-these/assets/83543030/77aa238a-7c8b-4bae-826f-5b7446a5130d)

### Register Clothes

1. Click the file selection button and choose the photo you want to upload.
2. Select the owner of the clothes.
3. Click the Upload Image button to register the clothes.

#### Successful Upload Message
![Upload Success](https://github.com/younghun1124/Whose-clothes-are-these/assets/83543030/cca1cdda-4b28-4b9d-81a8-617a671d9681)

### Caution
To run the server, rename `main.py` to `app.py` or use the command `set FLASK_APP=main` before running.

### File Description

- `templates/results.html`: Shows clothes images based on similarity.
- `main.py`: Flask server file for image feature extraction and similarity comparison.
- `index.html`: User interface for uploading and comparing clothes photos.
- `script.js`: JavaScript for previewing uploaded clothes photos.
- `styles.css`: CSS for the web page.

## Reference
- He, Kaiming, et al. (10 Dec 2015). "Deep Residual Learning for Image Recognition." arXiv: [1512.03385](https://arxiv.org/abs/1512.03385)
- [Problem with OpenCV not recognizing Korean path](https://bskyvision.com/entry/python-cv2imread-%ED%95%9C%EA%B8%80-%ED%8C%8C%EC%9D%BC-% EA%B2%BD%EB%A1%9C-%EC%9D%B8%EC%8B%9D%EC%9D%84-%EB%AA%BB%ED%95%98%EB%8A%94- %EB%AC%B8%EC%A0%9C-%ED%95%B4%EA%B2%B0-%EB%B0%A9%EB%B2%95)

## License
This Project is MIT licensed, as found in the LICENSE file.

<hr>
# 아래는 한글 버전의 README 입니다


# 이거 누구 옷이야?  

미리 저장된 옷 사진 중 가장 비슷한 옷 사진을 Residual Neural Network (a.k.a. Residual Network, ResNet) 모델을 이용해 찾아주는 사이트 입니다.  

## 문제상황  

### "내 옷은 다 어디갔지?"  

자꾸 섞이는 옷들 때문에 내 옷이 동생 방의 옷장에 수개월간 잠들어 있는 경우가 있습니다.  
자식들이 다 크고나니 빨래를 갤 때 엄마와 딸, 아빠와 아들, 딸과 아들의 옷이 헷갈릴 때가 있습니다.  
빨래를 갤 때마다 집에 가족이 모두 있는 것이 아니기 때문에 물어보기도 곤란합니다.  



## 구현방법  
1. flask 모듈을 이용해 가족 구성원 모두가 각자의 스마트폰으로 이용 할 수 있도록 python 서버를 구동합니다.
2. opencv로 이미지를 전처리하고 torchvision의 pretrained 된 resnet50 모델을 이용해 옷 사진의 특징을 추출합니다.
3. html /compare form 으로 서버에 전송받은 사진의 특징도 추출하여 등록되어있는 사진들의 특징과 비교합니다.
비교하는 코드는 다음과 같습니다. ```similarity = np.dot(target_features, features) / (np.linalg.norm(target_features) * np.linalg.norm(features))```
<img width="486" alt="image" src="https://github.com/younghun1124/Whose-clothes-are-these/assets/83543030/c9dec382-5a38-43d6-b2c6-730b858fe0fd"><br>  
4. 사용자에게 유사도 순서대로 옷의 사진과 옷의 주인정보를 html list 로 보내줍니다.

## 사용방법

### 옷의 주인 찾기
<img width="480" alt="image" src="https://github.com/younghun1124/Whose-clothes-are-these/assets/83543030/32959e58-291c-44e8-a948-cdf1efef40d3">


비슷한 옷 찾기 메뉴에서 파일을 선택합니다.

- 선택한 파일의 이미지
![선택한 파일의 이미지](https://github.com/younghun1124/Whose-clothes-are-these/assets/83543030/64fc1062-5fbf-4b96-b0f3-75282348f12b)

그 뒤 "이거 누구 옷이야?: 버튼을 눌러 비교합니다.  

- 결과
<img width="513" alt="image" src="https://github.com/younghun1124/Whose-clothes-are-these/assets/83543030/81356ea7-b02b-45ea-9b94-b32e66dc83f1">



- 가장 유사하다고 판별된 이미지
![image](https://github.com/younghun1124/Whose-clothes-are-these/assets/83543030/77aa238a-7c8b-4bae-826f-5b7446a5130d)

사진의 방향이 다르고 비슷한 색의 옷이 많음에도 불구하고 정확히 판별하였음을 알 수 있습니다.

### 옷 등록하기
<img width="413" alt="image" src="https://github.com/younghun1124/Whose-clothes-are-these/assets/83543030/e40eb6e4-3362-4f33-bcef-cc3defae66ec">

1. 파일 선택버튼을 누르고 업로드할 옷 사진을 선택합니다.  
2. 옷의 주인을 선택합니다.
3. Upload image 버튼을 눌러 옷을 등록합니다. 이미지는 서버내 images2 폴더에 옷의 주인 이름으로 저장되고, 같은 이름의 이미지가 이미 저장되어있다면 {주인이름+number} 형태로 등록됩니다.

성공적으로 이미지가 저장되었다면 <img width="158" alt="image" src="https://github.com/younghun1124/Whose-clothes-are-these/assets/83543030/cca1cdda-4b28-4b9d-81a8-617a671d9681"> 메시지가 서버로부터 전송됩니다.

### 주의사항
서버 파일인 main.py 파일을 flask run 명령어로 실행하면 바로 실행되지 않습니다. main.py 파일의 이름을 app.py 로 수정하거나 set FLASK_APP=main 명령어를 입력한 뒤 실행해야합니다.

### 파일 설명
```templates/results.html```:이미지가 유사한 정도에 따라 images2 폴더 내에 있는 옷 이미지를 보여주는 html 문서입니다.

```main.py```:이미지의 특징을 추출하여 유사도를 비교한뒤 사용자의 http 요청에 따라 결과를 반환해주는 flask 서버 파일입니다. 사용자가 새로 이미지를 업로드 하면 images2 폴더에 저장하는 기능도 포함합니다.

```index.html```:사용자가 옷 사진을 업로드하고 비교할 수 있는 html 인터페이스입니다.

```script.js```:index.html에서 사용자가 업로드한 옷 사진을 미리보기 할수 있게 하는 자바스크립트 파일입니다.  

```styles.css```:웹페이지 전반에 이용되는 css 파일입니다.
## 참조  
- He, Kaiming; Zhang, Xiangyu; Ren, Shaoqing; Sun, Jian (10 Dec 2015). Deep Residual Learning for Image Recognition. arXiv:[1512.03385](https://arxiv.org/abs/1512.03385)  
- [opencv 한글경로 인식 안되는 문제](https://bskyvision.com/entry/python-cv2imread-%ED%95%9C%EA%B8%80-%ED%8C%8C%EC%9D%BC-%EA%B2%BD%EB%A1%9C-%EC%9D%B8%EC%8B%9D%EC%9D%84-%EB%AA%BB%ED%95%98%EB%8A%94-%EB%AC%B8%EC%A0%9C-%ED%95%B4%EA%B2%B0-%EB%B0%A9%EB%B2%95)

## License
This Project is MIT licensed, as found in the LICENSE file.

