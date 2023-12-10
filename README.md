# Whose-clothes-are-these  

미리 저장된 옷 사진 중 가장 비슷한 옷 사진을 찾아주는 소프트웨어입니다.  

## 문제상황  

### "이거 누구 옷이야?"  

자식들이 다 크고나니 엄마와 딸, 아빠와 아들, 딸과 아들의 옷이 헷갈릴 때가 있습니다.  
빨래를 갤 때마다 집에 가족이 모두 있는 것이 아니기 때문에 물어보기도 곤란합니다.  

### "내 옷은 다 어디갔지?"  

자꾸 섞이는 옷들 때문에 내 옷이 동생 방의 옷장에 수개월간 잠들어 있는 경우가 있습니다.  

## 구현방법  
1. flask 모듈을 이용해 가족 구성원 모두가 각자의 스마트폰으로 이용 할 수 있도록 python 서버를 구동합니다.
2. opencv로 이미지를 전처리하고 torchvision의 pretrained 된 resnet50 모델을 이용해 옷 사진의 특징을 추출합니다.
3. html /compare form 으로 서버에 전송받은 사진의 특징도 추출하여 등록되어있는 사진들의 특징과 비교합니다.
비교하는 코드는 다음과 같습니다. ```similarity = np.dot(target_features, features) / (np.linalg.norm(target_features) * np.linalg.norm(features))```
<img width="486" alt="image" src="https://github.com/younghun1124/Whose-clothes-are-these/assets/83543030/c9dec382-5a38-43d6-b2c6-730b858fe0fd"><br>  
4. 사용자에게 유사도 순서대로 옷의 사진과 옷의 주인정보를 html list 로 보내줍니다.

## 사용방법

### 옷의 주인 찾기
<img width="293" alt="image" src="https://github.com/younghun1124/Whose-clothes-are-these/assets/83543030/36708ac5-a6e1-4b9a-a3d5-cf23125face5">


비슷한 옷 찾기 메뉴에서 파일을 선택합니다.

- 선택한 파일의 이미지
![선택한 파일의 이미지](https://github.com/younghun1124/Whose-clothes-are-these/assets/83543030/64fc1062-5fbf-4b96-b0f3-75282348f12b)

그 뒤 "이거 누구 옷이야?: 버튼을 눌러 비교합니다.  

- 결과
<img width="367" alt="image" src="https://github.com/younghun1124/Whose-clothes-are-these/assets/83543030/38c4e97b-cde2-434b-a5d5-a347f6492152">  

- 가장 유사하다고 판별된 이미지
![image](https://github.com/younghun1124/Whose-clothes-are-these/assets/83543030/77aa238a-7c8b-4bae-826f-5b7446a5130d)

사진의 방향이 다르고 비슷한 색의 옷이 많음에도 불구하고 정확히 판별하였음을 알 수 있습니다.

### 옷 등록하기
<img width="273" alt="image" src="https://github.com/younghun1124/Whose-clothes-are-these/assets/83543030/0f93f18c-3f98-4bf4-82f2-7b6b220baf74">
1. 파일 선택버튼을 누르고 업로드할 옷 사진을 선택합니다.  
2. 옷의 주인을 선택합니다.
3. Upload image 버튼을 눌러 옷을 등록합니다. 이미지는 서버내 images2 폴더에 옷의 주인 이름으로 저장되고, 같은 이름의 이미지가 이미 저장되어있다면 {주인이름+number} 형태로 등록됩니다.

성공적으로 이미지가 저장되었다면 <img width="158" alt="image" src="https://github.com/younghun1124/Whose-clothes-are-these/assets/83543030/cca1cdda-4b28-4b9d-81a8-617a671d9681"> 메시지가 서버로부터 전송됩니다.

### 주의사항
서버 파일인 main.py 파일을 flask run 명령어로 실행하면 바로 실행되지 않습니다. main.py 파일의 이름을 app.py 로 수정하거나 set FLASK_APP=main 명령어를 입력한 뒤 실행해야합니다.

## 참조  

[opencv 한글경로 인식 안되는 문제](https://bskyvision.com/entry/python-cv2imread-%ED%95%9C%EA%B8%80-%ED%8C%8C%EC%9D%BC-%EA%B2%BD%EB%A1%9C-%EC%9D%B8%EC%8B%9D%EC%9D%84-%EB%AA%BB%ED%95%98%EB%8A%94-%EB%AC%B8%EC%A0%9C-%ED%95%B4%EA%B2%B0-%EB%B0%A9%EB%B2%95)
