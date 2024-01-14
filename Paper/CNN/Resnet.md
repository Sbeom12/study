# Deep Residual Learning for Image Recognition
---
* [관련논문](https://arxiv.org/pdf/1512.03385.pdf)
* ILSVRC(ImageNet Large Scale Visual Recognition Challenge) 2015 대회에서 1등을 차지한 모델.  
    <img src= "https://miro.medium.com/v2/resize:fit:720/format:webp/1*Io-I-fOM0jGftDb_nne4KQ.png" width='500' hegith = '400'>  
    [출처](https://medium.com/@Lidinwise/the-revolution-of-depth-facf174924f5)
    * layer의 수가 VGG의 8배 깊음.

</br>

## Intro.
* Resnet이라는 이전까지 `깊이를 깊게 쌓을 수록 성능이 좋아진다`라는 인식을 기반으로 수많은 연구진들이 연구를 해옴.
    * Going deeper with convolutions. In CVPR, 2015.
    * Very deep convolutional networks for large-scale image recognition. In ICLR, 2015.
 
 </br>
    
* `Gradient Vanishing/Exploding`로 인해서 깊게 쌓기만 하는것은 마냥 쉬운 일이 아니였음.
    * Gradient Vanishing(기울기 소실) 문제는 Backpropagation(역전파) 과정에서 Input layer로 갈수록 Gradient(기울기)가 점차적으로 작아지는 현상.
        * layer 수가 많을수록 즉 깊이가 깊어질수록 문제가 심해짐.
    * Gradient Exploding(기울기 폭주) 문제는 소실과는 다르게 Backpropagation(역전파) 과정에서 큰 값을 가지는 weight(가중치)들이 반복적으로 곱해져 weight(가중치)가 제대로 업데이트 되지 않는 현상.
 
 </br>
    
* 기존 구조에서 레이어 깊이에 따른 학습 비교  
    <img src= "https://i.imgur.com/HIbfAlP.png" width='600' hegith = '300'>  
    * 레이어 수가 높을수록 오히려 성능이 degradation(약화)됨.
    * 이때 레이어 수가 높다고 overfitting이 된것이 아님.
</br>

## Residual Learning
* 연구진들은 Layer의 수를 깊게 하면서 깊이에 따른 학습 효과를 얻을수 있도록 Residual Learning을 고안함.  
    <img src= "https://i.imgur.com/mHfZYPQ.png" width='400' hegith = '300'>  
    * 기존 방식에서 input으로 x가 들어가 2개의 layer를 거쳐 출력으로 H(x)가 나오는 구조.
        * 목표 : 학습을 통해서 최적의 출력인 H(x)를 구하는 것이 목표
        * layer들의 파라미터들도 최적의 H(x)를 위해 결정됨.
    
    </br>

    * 하지만 기존 방식에서 H(x)를 얻는 것이 아닌 H(x) - x, 즉 출력과 입력의 차(Residual)를 얻을 수 있도록 관점을 바꿈.
        * layer는 H(x) - x를 얻도록 학습. 
        * F(x) = H(x) -x 
        * 출력은 H(x) = F(x)+x 가 된다.
        * 그러면, 블록을 오른쪽처럼 바뀌게 된다.
    
    </br>

    * Residual 구조
        * 입력에서 바로 출력으로 연결되는 shortcut 연결이 생성.
        * 계산량도 이전 방법과 큰 차이가 없음.
            * 덧셈 추가
        * pre-conditioning(사전조건화)
            * Residual 구조에서 최적의 목표값은 F(x)가 0인경우.
            * H(x) = x로 mapping하는 것이 학습의 목표.
            * 학습할 방향이 미리 정해짐.
        * 입력의 작은 움직임 검출
            * F(x)가 0에 가깝게 학습되므로 조금만한 x값의 변화에 의해 영향을 받게 됨.
    
    </br>

    * 효과
        * Layer 수가 많은 깊은 망들도 최적화가 가능하다.(학습이 가능)
        * Layer 수가 늘어나 정확도가 개선된다.

## Identity Mapping by shortcuts
* ResNet은 깊은 신경망을 효과적으로 학습시키기 위한 아키텍처로, 그 중요한 부분 중 하나가 residual block이다.
* 기본적인 **residual block의 구조**는 다음과 같다
    1. 입력 x에 대한 **합성곱(Convolution) 연산**과 **활성화 함수**를 적용한다.
    2. 이를 또 다른 합성곱과 활성화 함수를 거친 **출력에 더한다**.

</br>

### Indentity shortcut
$$ y= F(x, {W_i})+x$$

* 위 식에서 x와 y는 각각 input, output을 나타낸다. 잔차 학습을 이용하여 output 값에 input값인 x를 더해주는 것을 확인할 수 있다.
* 첫 번째 term은 학습된 residual mapping이다
* F + x 연산이 shortcut connection을 의미하고 element-wise addition이다.
* 위 식은 $F = W_2 \sigma(W_1x)$ 을 간소화한 모양으로 활성함수인 ReLU를 한 번 통과하고 biases는 생략된 식이다.

### Projection shortcut
* 만약 입력과 출력의 차원이 다르다면 덧셈 연산이 불가능하여 이를 해결하기 위해 Projection Shortcut을 도입하였다. 

$$ y = F(x, {W_i}) + W_sx $$

</br>

* 단순히 identity shortcut에서 **linear함수**인 Ws를 x에 곱한 꼴로 표현된다.
* **x와 F의 차원을 동일하게 맞춰주기 위해** 위의 식을 사용한다. 이를 통해 **입력값의 차원을 변환**하여 덧셈 연산이 가능하게 해준다.
* 또한 gradient를 구하였을 때 Ws가 사라지지 않고 남기 때문에 **vanishing gradient 문제를 해결** 할 수 있다.

</br>

* 이러한 구조를 통해 ResNet은 매우 깊은 네트워크에서도 안정적으로 학습이 가능하며, 그 성능은 다양한 computer vision task에서 입증되었다.

</br>

## Architecture(VGG19 vs Plain vs ResNet)
* 본 논문에서는 다음과 같이 모델들을 비교하고 있다.  
![image](https://github.com/Sbeom12/study/blob/main/image/Resnet/architecture1.JPG?raw=true)


### VGG19
![image2](https://production-media.paperswithcode.com/methods/vgg_7mT4DML.png)

* VGG-19는 19개의 계층으로 이루어진 깊은 컨볼루션 신경망(CNN)으로, 2014년 ILSVRC에서 사용된 모델 중 하나 이다. 주로 이미지 분류 작업에 적용되며, 작은 3x3 필터를 사용한 깊은 구조를 통해 복잡한 이미지 특징을 학습한다.

</br>

* 구조
    1. **13 Convolution Layers + 3 Fully-connected Layers**
    2. **3x3 convolution filiters**
    3. **stride: 1 & padding: 1**
    4. **2x2 max pooling (stride: 2)**
    5. **ReLU**

</br>

### Plain Network 
* **VGG net을 참고**해서 만든 Network로 conv filter의 사이즈가 3 x 3이고, 다음 2가지 규칙에 기반하여 설계하였다. 
    1. feature map의 size가 같은 layer들은 **모두 같은 수의 conv filter**를 사용
    2. **feature map 사이즈가 절반이 되면 filter 수는 2배**가 되도록 설계되었다.

![Alt text](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fbp8rUK%2FbtqS9ZghSdh%2F0JZUWVEjQT8E7wkRRY1W41%2Fimg.png)

* downsampling시 pooling 대신 stride가 2인 conv filter를 사용.
* 모델 마지막에 Global Average Pooling을 사용.
* 최종 레이어는 34개로, VGG19와 비교했을 때 **비교적 적은 filter와 복잡도**를 가지는 것을 확인할 수 있다.

### Residual Network
* **Plain net을 바탕**으로 설계된 Network이다. Plain net에서 **shortcut connection**이 추가되었다고 볼 수 있다.
![Alt text1](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fdek2kD%2FbtqTfCx4XTn%2FkMHkA7Fv8vbW5Hkmg1x3a0%2Fimg.png
)
이 때 Identity Shorkcut은 input과 output을 **같은 차원**으로 맞춰줘야 한다. 차원을 맞추기 위해 **두 가지 방법**을 사용할 수 있다.

1. **Padding**
    - 차원을 조절하기 위해 0을 넣어서 맞춰준다.(zero-padding) → 추가 파라미터 없음.
2. **차원이 달라지는 점선 shortcut에만 1x1 convolution layer 적용**
    - 크기가 같은 실선의 identity shortcut은 그냥 더하고, **크기가 달라지는 점선 shortcut**에 대해서만 **1x1convolution layer**를 거쳐 크기를 맞춰준다.
3. **점선, 실선 상관 없이 모든 shortcut에 대해 1x1 convolution layer 적용**
    - **모든 shortcut**에 대해 **convolution layer**를 거쳐 크기를 맞춰준다.

![Alt text](https://github.com/Sbeom12/study/blob/main/image/Resnet/architecture2.JPG?raw=true)


||VGG19|Plain|Residual|
|:---|:------:|:---:|:---:|
|Parameter|19|34|34|
|FLOPs|19.6 billion|3.6 billion|3.6 billion|

</br>

## Results
* 18-layer와 34-layer에 대한 Plain network와 Residual network의 실험결과를 살펴보면 다음과 같다.
![결과1.JPG](https://github.com/Sbeom12/study/blob/main/image/Resnet/%EA%B2%B0%EA%B3%BC1.JPG?raw=true)
- Plain network이 경우는 18-layer가 결과가 좋고 Residual Network의 경우 34-layer가 더 좋다는 것을 볼 수 있다.
- **Convergence(수렴) 속도가 Residual Net의 수렴 속도가 더 빠르다는 것을 볼 수 있다.**

## Bottleneck
* 학습에 걸리는 시간을 고려하여 Layer 수가 50이 넘는 구조들에 대해 Residual Network를 아래와 같이 변경했다.
![](https://github.com/Sbeom12/study/blob/main/image/Resnet/%EA%B2%B0%EA%B3%BC2.JPG?raw=true)
- 기본적으로 차원을 줄였다고 나중에 다시 늘리는 구조.
    - 연산 시간 감소를 위해 사용.
    - 계산량을 줄이기 위해 사용.

|| Residual Network  | Bottlenet Network |
|---| :---: | :---: |
|파라미터 수| 3x3x64x2 = 1152|1x1x64+3x3x64+1x1x256 = 896|
* 파라미터 수가 22% 감소  

</br>

![](https://github.com/Sbeom12/study/blob/main/image/Resnet/%EA%B2%B0%EA%B3%BC3.JPG?raw=true)

- 위의 표는 single model에 대한 실험 표로 B와 C에서 B는 차원을 증가시키는 경우에만 projection shorcut을  나머지 shortcut에는 identity를 사용했고, C는 모든 shortcut에 projection shortcut을 사용한 경우이다.
- Resnet의 34만 사용해도 다른 모델들과 비교해도 될 정도로 강력했지만, 152-layer의 모델 2개 등 총 6개의 모델로 결합하여 최종적으로 3.57%의 오차율로 대회 1위를 달성했다.

</br>

## CIFAR-10의 데이터의 결과
- ILRSVRC 대회와는 다르게 이미지의 크기가 32x32라서 초기 7x7 conv를 3x3 conv연산으로 바꾸어 학습을 진행했고, 아래 그림과 같이 비슷한 경향을 가지는 결과를 얻었다.  
![](https://github.com/Sbeom12/study/blob/main/image/Resnet/%EA%B2%B0%EA%B3%BC4.JPG?raw=true)  
![](https://github.com/Sbeom12/study/blob/main/image/Resnet/%EA%B2%B0%EA%B3%BC5.JPG?raw=true)  

- Plain은 일정 layer의 수를 넘으면 그 이후의 layer부터는 성능이 좋지 않고, Residual은 layer의 수가 증가하더라도 결과가 더 좋아 지는 것을 확인할 수 있지만, 너무 크게 증가한 경우에는 더 좋지 않았다.
- 1202-layer의 결과
    - 학습을 진행할 때 최적화에 별 다른 어려움이 없음.
    - CIFAR-10의 데이터가 많지 않음.
    - maxout/dropout을 사용하지 않았음.
    - overfitting이 발생했다고 해석할 수 있다.

</br>

- 이에 Identity Mappings in Deep Residual Networks 2016년에 추가 연구 진행 및 발표.
- Pre-activation을 통해 개선.  
![](https://github.com/Sbeom12/study/blob/main/image/Resnet/%EA%B2%B0%EA%B3%BC6.JPG?raw=true)
    - 일반화 성능 향상.
    - 최적화가 쉬워짐.
- Residual 망이 layer-1000이 넘어가도 효과적으로 작동한다.


## 의문점.

### Residual Networks Behave Like Ensembles of Relatively Shallow Networks
    - Residual의 구조는 Ensemble(앙상블) 모델 처럼 작동한다.  

![](https://github.com/Sbeom12/study/blob/main/image/Resnet/%EC%95%99%EC%83%81%EB%B8%94.JPG?raw=true)
- 3개의 Convolution layer에 대한 구조를 다른 시점에서 바라본것.

#### Lesion Study(손상 연구)
* 학습된 ResNet에서 skip connection과  downsampling projection을 제외한 블록을 제거시키고 실험.
<img src= "https://github.com/Sbeom12/study/blob/main/image/Resnet/%EC%86%90%EC%8B%A4.JPG?raw=true" width='400' hegith = '200'>   
<img src= "https://github.com/Sbeom12/study/blob/main/image/Resnet/%EC%B6%94%EA%B0%80%EA%B2%B0%EA%B3%BC1.JPG?raw=true" width='400' hegith = '200'>     
- VGG과 Resnet을 비교하면, VGG는 layer의 손실이 Error에 크게 영향주지만, Resnet는 Downsampling layer를 제외하고는 크게 영향을 주지 않음.
- 이는 VGG는 layer들간의 길이 unique하여 하나라도 지워지면 정보 손실이 심각해지지만, Resnet은 Unraveled의 관점에서 봤을 때 가능한 Path가 절반으로 감소하는 효과.
- Path들이 서로 Independent(독립적).
- Ensemble(앙상블)의 특징
    - 모델의 output은 ensemble된 model의 개수에 ‘smooth’하게 dependent.
- Residual network=  Ensenble?
    - Resnet의 layer를 감소 및 순서를 섞은 경우.   

<img src= "https://github.com/Sbeom12/study/blob/main/image/Resnet/%EC%86%90%EC%8B%A42.JPG?raw=true" width='500' hegith = '200'>   

- layer의 수가 감소할수록 Error는 smooth하게 증가.
- layer의 순서를 많이 바꿀수록  Error가 smooth하게 증가.
- 즉, Residual network은 Ensenble(앙상블)로 볼 수 있다.

</br>

#### Path
- 95% 이상의 path가 19~35개의 모듈을 지남.
- path의 길이가 질수록 input의 영향을 적게 받게됨.
- 20개 보다 긴 경로들은 학습에 영향을 주기엔 너무 깊음.
- 즉, Residual network에서 학습에 영향을 주는 path들은 상대적으로 얕다.
- 또한, 역전파 과정에서 gradient 업데이트가 대부분 5개에서 17개의 길이에서 나옴.(전체의 약 45%정도로 effective path로 정의.)

#### Result
- Effective path만 학습 시킨 결과로 5.96%의 에러이지만, 전체를 학습 시킨 결과는 6.10의 에러.
- 오히려 더 좋은 결과.  

<img src= "https://github.com/Sbeom12/study/blob/main/image/Resnet/%EA%B8%B8%EC%9D%B42.JPG?raw=true" width='500' hegith = '200'>   

- Resnet에서 residual block을 제거했을 때 path length들이 얼마나 남아 있는지 진행한 실험.
- block을 제거하면 대부분 long-path들에 영향을 주고, layer을 제거했을 때는 여전히 effective path들이 남아있어서 error가 크게 증가하지 않지만, 20개를 제거했을 때는 effective path가 많이 지워져 error가 크게 증가하는 것을 볼 수 있다.
- 결론
    - Resnet은 이전 모델들에 비해 깊지만, 단일한 깊은 네트위크가 아닌 많은 경로들의 집합으로 볼 수 있음.
    - Backpropagation 중에 gradient에 기여하는 네트워크의 경로는 생각보다 얕다.
    - 즉, Vanishing gradient를 완전히 해결할 수 없다.

</br>

## BottleNet의 단점
- 1x1의 Convolution 사용
    - 구글의 Inception에서 사용되면서 주목.
    - 채널 수 조절, 계산량 감소, 비선형성 추가.
- 1x1의 convolution의 단점.
    - 강제로 채널을 줄여 정보 손실이 방생하여 정확도가 떨어진다.
    <img src= "https://i.imgur.com/aXiDwaK.png" width='500' hegith = '200'>   
        
</br>

## Related Works