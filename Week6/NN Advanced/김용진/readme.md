# Learning rate scheduler

## ReduceLROnPlateau
성능 향상이 없을 때 learning rate를 감소시킨다. 따라서 validation loss를 필수적으로 파라미터에 넣어주어야 한다.  
직관적으로 타당하고 가장 많이 쓰이는 scheduler 중 하나이다.

## StepLR
step size마다 gamma의 비율로 learning rate를 감소시킨다. 즉, 특정 step size마다 learning rate에 gamma를 곱한다.  
편리한 방법 중 하나이다.

## MultiStep LR
step size가 아니라 learning rate를 감소시킬 epoch를 지정해준다.

# Training Error와 Generalization Error 사이 간극을 줄이는 방안 소개하기

## Dataset 늘리기
가장 간단하면서도 어려운 방법이다. Dataset이 증가하면 over-fitting이 줄어들게 되고 general한 모델을 만들 수 있다.  
하지만 dataset 구축비용이 많이 든다는 단점이 있다.

## General한 model 사용하기
Transformer와 같이 기존 model들 보다 general한 model을 사용하여 error의 간극을 줄일 수 있다.  
하지만 모델이 크기 때문에 많은 데이터와 training 시간이 필요하다. 또한 데이터가 적을 경우에는 성능이 좋지 않다.
