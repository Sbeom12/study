# LLM이란?
* LLM은 Large Language Model의 약자로 말 그대로 방대한 데이터를 기반으로 pre-trained된 초대형 딥러닝 모델이다.
* 일반적은 LLM은 `Transformer` 아키텍커 기반으로, `Self-attention`의 매커니즘(Encoder-Decoder)을 사용하여 문장 내 단어 간의 상관 관계를 이해한다.
    * `Transformer`구조는 순환 신경망들과는 다르게 전체 Sequence를 병렬로 처리한다.
    * 또한, 비지도 학습 중 자기주도학습(Self-supervised learning)으로 학습을 진행한다.
* `Self-attention` 상관 관계를 이해하여, 문맥을 이해하고 다음 단어를 예측하는 데 뛰어난 성능을 발휘.
* LLM은 보통 수억 개의 매개변수를 지니며, 방대한 양의 텍스트 데이터를 학습하여 인간과 유사한 수준의 언어 생성과 이해 능력을 보여준다.(특히 최근24년 3월 4일에 발표된 Claude3는 최초로 IQ 테스트 결과로 101를 달성했다.)

* 2012년에 AlexNet을 통해서 열린 딥러닝 시대가 왜 10년이 자나서야 LLM이 각광받았을까?


## Transformer & Self-attention
* Transformer와 Self-Attention은 자연어 처리 분야에서 중요한 개념으로, 2017년 Google의 연구팀이 발표한 "Attention Is All You Need" 논문에서 소개되었다.

* RNN의 재귀 기반의 모델의 한계를 해결함.
    * 장기 의존성 문제 (Long-term Dependency Problem)
    * 기울기 소실과 폭주 문제 (Vanishing and Exploding Gradients)
    * 병렬 연산의 어려움.   
    * 저장할 수 있는 context의 길이가 짧음.
    * LSTM(Long-shot-Term-Memory)와 GRU(Gated Recurrent Unit)등이 등장했지만, 근본적인 한계를 극복하지 못함.

