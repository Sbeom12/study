# LLM이란?
* LLM은 Large Language Model의 약자로 말 그대로 방대한 데이터를 기반으로 pre-trained된 초대형 딥러닝 모델이다.
* 일반적은 LLM은 `Transformer` 아키텍커 기반으로, `Self-attention`의 매커니즘(Encoder-Decoder)을 사용하여 문장 내 단어 간의 상관 관계를 이해한다.
    * `Transformer`구조는 순환 신경망들과는 다르게 전체 Sequence를 병렬로 처리한다.
    * 또한, 비지도 학습 중 자기주도학습(Self-supervised learning)으로 학습을 진행한다.
* `Self-attention` 상관 관계를 이해하여, 문맥을 이해하고 다음 단어를 예측하는 데 뛰어난 성능을 발휘.
* LLM은 보통 수억 개의 매개변수를 지니며, 방대한 양의 텍스트 데이터를 학습하여 인간과 유사한 수준의 언어 생성과 이해 능력을 보여준다.(특히 최근24년 3월 4일에 발표된 Claude3는 최초로 IQ 테스트 결과로 101를 달성했다.)


## Gain Attention
* 2012년에 AlexNet을 통해서 열린 딥러닝 시대가 10년이 자나서야 LLM이 각광받았다 이에 대한 요인으로 다음 3가지가 있다.

1. 연산 능력의 한계. 
  	* AlexNet도 gpu의 메모리 부족으로 인해 2개의 gpu를 병렬처리하여 학습을 진행했듯이 10년전과 현재의 gpu의 연산 능력의 차이는 매우 크다. 
2. 데이터의 부족.
	* 당시에 [깃허브](https://github.com/)(2008), [스택 오버플로우](https://stackoverflow.com/)(2008), [레딧](https://www.reddit.com/)(2005)으로 다양한 커뮤니티와 관련된 텍스트 데이터는 존재했으나, 이를 효과적으로 수집하고 정제하는 것이 어려웠다.
    * 데이터의 양도 당시에도 많았지만, 현재엔는 훨씬 많고 더 좋은 품질의 데이터가 많다.(IDC 발표 기준으로 2010년과 2020년의 데이터량은 약 49배 차이)
3. 모델 아키텍쳐의 발전.
	* `Transformer`의 등장.
    * RNN의 재귀 기반의 모델의 한계를 해결함.
      * 장기 의존성 문제 (Long-term Dependency Problem)
      * 기울기 소실과 폭주 문제 (Vanishing and Exploding Gradients)
      * 병렬 연산의 어려움.   
      * 저장할 수 있는 context의 길이가 짧음.
      * LSTM(Long-shot-Term-Memory)와 GRU(Gated Recurrent Unit)등이 등장했지만, 근본적인 한계를 극복하지 못함.


## 현재 LLM을 활용하기 위해 필요한 지식.
1. RAG(Retrieval-Augmented Generation):
	* RAG는 LLM을 활용한 생성 모델로, 외부 지식을 검색하여 활용함으로써 보다 풍부하고 정확한 텍스트 생성이 가능합니다. 
2. 프롬프트 엔지니어링(Prompt Engineering):
	* 프롬프트 엔지니어링은 LLM에 입력하는 프롬프트(지시문)를 최적화하여 원하는 출력을 유도하는 기술입니다.
3. 랭체인(LangChain):
	* LLM을 활용하여 애플리케이션을 구축하기 위한 프레임워크입니다.
4. JAX/Flax:
	* JAX는 Google에서 개발한 고성능 머신러닝 라이브러리로, NumPy와 유사한 API를 제공하면서 GPU/TPU에서 효율적으로 실행된다.
    * Flax는 JAX 기반의 신경망 라이브러리로, Transformer 같은 모델을 쉽게 구현하고 학습할 수 있도록 도와준다.
5. Knowledge Distillation
	* 대규모 LLM의 지식을 작은 모델로 전달하여 효율성을 높이는 기술.


6.
* Transformer와 Self-Attention은 자연어 처리 분야에서 중요한 개념으로, 2017년 Google의 연구팀이 발표한 "Attention Is All You Need" 논문에서 소개되었다.

