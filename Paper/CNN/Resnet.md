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


## Architecture

</br>
## Related Works