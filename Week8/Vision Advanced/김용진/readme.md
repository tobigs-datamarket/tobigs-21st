# InternImage
논문: https://arxiv.org/pdf/2211.05778.pdf

Vision 분야에서 Transformer 기반의 Foundation Model들이 많은 task에서 SOTA를 달성하고 있는데, CNN을 이용하여 Transformer를 잡아보자 라는 생각을 바탕으로 나온 논문입니다. CVPR2023에 accept된 논문으로 Transformer model 논문은 아니지만 Transformer의 장점을 분석하고 CNN을 통해서 그 장점을 만족할 수 있게 해주면 좋은 성능을 낼 수 있다 라는 점을 보여준 논문입니다.

논문이 나올 당시에는 ImageNet classification, semantic segmantation 등의 task에 대해 Transformer 기반의 모델들 사이에서 CNN을 이용하여 상위권에 존재했었고, COCO object detection 에서는 SOTA를 달성했습니다.

## Abstract
CNN에 기반한 LArge-scale모델 연구는 아직 초기단계라고 말하며, 현재의 CNN 연구는 large dense kernels(41x41 크기의 kernel)를 이용하는 것에 초점이 맞춰져 있다고 주장하고 있습니다. 하지만 본 논문에서는 Deformable convolution을 통해서 모델이 large effective receptive field뿐만 아니라 adaptive spatial aggregation을 갖고 있다고 주장합니다. 또한 parameter와 training data를 ViT만큼 증가시켰습니다. 이러한 방법을 통해 CNN이 성공했고, large model에서는 실패한 이유인 strict inductive bias를 줄여 robust한 pattern을 배울 수 있다고 주장하고 있습니다.

## Why Transformer?
이 논문에서는 Transformer가 성공한 이유를 세가지로 분석합니다.

1. Long-range dependence  
먼 거리에 있는 pixel도 영향을 끼칠 수 있는가
2. Adaptive spatial aggregation  
attention처럼 어떤 pixel에 대해 adaptive하게 weight를 변화시킬 수 있는가
3. Advanced components(Layer Nomalization, FFN, GELU)

위의 이유 중 1,2번은 Transformer에서 Multi-Head Self Attention(MHSA)를 통해 만들어 집니다. 따라서 CNN을 이용해서 최대한 MHSA의 효과를 내게하는 것이 논문이 목표가 됩니다.

## Deformable Convolution

Deformable Convolution V1: https://arxiv.org/pdf/1703.06211.pdf  
Deformable Convolution V2: https://arxiv.org/pdf/1811.11168.pdf


Deformable Convolution 또한 논문 한편이고 v2가 존재하기 때문에 간단히만 설명하겠습니다.  
기존 CNN같은 경우에는 어떤 pixel에 대해 3x3 kernel의 경우 9개의 pixel과 strict하게 convolution을 진행하는데, deformable convolution은 offset이라는 것을 정해 어떤 pixel과 가장 관련된 pixel을 예측하여 convolution을 진행합니다. 그림으로 보면 이해가 쉽습니다. 

<img width="599" alt="image" src="https://github.com/tobigs-datamarket/tobigs-21st/assets/76218918/9a408962-af68-4c74-b02a-dacf5d7d8ebc">

3x3 kernel이라면, deformable convolution은 어떤 pixel과 가장 관련된 pixel을 선정한 다음 convolution을 진행하게 됩니다. 이 때 pixel값을 꼭 float도 가능하며 이는 interpolation으로 처리합니다.

논문에서는 Deformable Convolution V3를 제시하는데, 다음과 같습니다.

1. Sharing weights among convolutional neurons  
Computational cost를 줄이기 위해 depth-wise, point-wise convolution으로 나눠 계산한다.

2. Introducing multi-group mechanism  
MHSA와 같이 Group convolution을 이용해서 풍푸함 representation sub-space의 정보를 효과적으로 학습한다.

<img width="1120" alt="image" src="https://github.com/tobigs-datamarket/tobigs-21st/assets/76218918/f306577d-6c3a-4e58-89f2-74644b5a7b05">

## Architecture
전체적인 구조에서는 CNN에서 흔히 쓰던 Bottle neck 구조에서 벗어나 LN,FFN,GELU를 사용했습니다. 또한 AABA구조에 맞춰서 stacking rules를 정해 search space를 효과적으로 줄였습니다. 추가로 Efficient Net에서 영감을 받아 모델 scaling에 사용할 rules도 만들어 모델을 효과적으로 scaling하였습니다.  
<img width="392" alt="image" src="https://github.com/tobigs-datamarket/tobigs-21st/assets/76218918/03060fd2-ce76-41fe-a278-4926ef180001">

## Conclusion & Limitation
CNN 또한 Large scale vision foundation model에서 생각해볼만한 선택지라는 것을 시사하는 연구였습니다. 하지만 저자들은 Deformable convolution이 high-speed가 필요한 task에 적용하는 것은 연구가 필요하다고 주장하고 있습니다.  

개인적으로는 이 논문이 트랜스포머가 왜 좋은가?에 대한 인사이트를 준 것 같아서 좋았습니다. long range dependency와 adaptive weight가 large foundation model에서는 중요한 요소였고, transformer는 단순히 이를 잘 만족하는 모델이였을 뿐이라는 생각을 갖게 해준 좋은 논문이였습니다.