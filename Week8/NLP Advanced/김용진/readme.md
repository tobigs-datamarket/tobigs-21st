# InstructGPT
논문: https://arxiv.org/pdf/2203.02155.pdf

Training language models to follow instructions with human feedback라는 논문으로 InstructGPT라고 많이 알려져 있는 논문입니다.  
ChatGPT 또한 InstructGPT에서 사용된 방법론을 이용했습니다. 획기적이면서도 OpenAI다운 방식으로 GPT 모델이 QA task에 적절하도록 성능을 향상시킨 방법을 제시했습니다.  

## Abstract
QA와 같은 task에서 LLM의 크기가 커져도 user의 의도를 따라 행동하지 않는 문제가 있었습니다. 이 때 User의 의도를 따라 행동하지 않는다는 것을 논문에서는
> generate outputs that are untruthful, toxic, or simply not helpful to the user  

라고 표현하고 있습니다. 이 문제를 크게 **Fine-tuning with human feedback** 과 **Reward Model** 두 가지 방식으로 해결합니다. 위의 방식을 줄여서 RLHF(Reinforcement Learning from Human Feedback)라고 많이 부르고 있습니다. 저자들은 RLHF방식을 통해 LLM과 user의 의도를 align했고, 이를 통해 InstructGPT 1.3B 모델이 GPT-3 175B 모델보다 선호(preferred)됐다고 주장했습니다.

## Defects of LM
LLM은 biased, toxic, not following user instructions와 같은 unintended behaviors를 한다고 합니다. 그 이유를 논문은 LLM이 internet webpage에서 가져온 data를 이용하여 next token prediction을 하기 때문이라고 주장합니다. Internet에서 긁어온 data들을 이용하여 학습을 진행했기 때문에 "follow the user's instruction helpfully and safely"라는 모델이 만들어진 원래의 의도대로 행동하지 않는다는 것입니다.

## Method
위의 문제를 해결하기 위해 본 논문에서는 RLHF 방식을 제안했습니다. 논문에서 제시한 방식은 간단하게 다음과 같습니다.  
1. Labeler를 고용하여 직접 promp에 적절한 output을 작성한다.(논문에서는 40명의 labeler를 고용)  
ex) prompt로 "Explain the moon landing to a 6 year old"가 주어지면, labeler는 직접 이 prompt에 알맞는 output을 서술
2. 1번에서 모은 data를 통해 GPT-3 모델을 supervised fine-tuning(SFT라고 지칭)
3. fine-tuning된 모델을 이용하여 하나의 prompt에 대한 다양한 답변 생성  
ex) prompt로 "Explain the moon landing to a 6 year old"를 SFT 모델에 여러번 넣으면 다양한 답변을 생성.(항상 똑같은 답변을 생성하지 않는다)
4. 3에서 생성된 여러 답변을 labeler가 선호도에 따라서 순위를 매김  
ex) "Explain the moon landing to a 6 year old"에 대해 A,B,C,D output이 존재할 때 labeler의 선호에 따라 D > C > A = B 와 같이 순위를 매김
5. 4에서 만든 순위 dataset을 이용해서 Reward Model을 학습. Reward Model은 SFT 모델의 마지막 단을 없애고 layer를 추가해서 scalar output을 return 할 수 있게 함. 이 때 선호도가 높은 답변에 대해서는 높은 reward 값(scalar)이 나올 수 있도록 loss를 설계  
ex) "Explain the moon landing to a 6 year old"에 대해 D > C > A = B 이면, prompt와 D가 Reward Model의 input으로 들어갔을 때는 높은 reward를, B가 들어갔을 때는 낮는 reward를 return

$$loss(\theta) = -\frac{1}{\begin{pmatrix} 
K \\ 2
\end{pmatrix}}E(x,y_w,y_l) \sim D\[log(\sigma(r_\theta(x,y_w) - r_\theta(x,y_l)))\]$$

7. SFT 모델을 PPO라는 Reinforcement Learning 알고리즘을 통해 fine-tuning.  
6-1. Random한 prompt가 주어지면, 원하는 output을 생성(next token prediction)  
6-2. 이 때 next token prediction을 Reinforcement Learning의 action으로 생각할 수 있고, 하나의 답변이 다 완성되는 것을 하나의 episode로 볼 수 있음  
6-3. 6-2에서 나온 답변과, input prompt를 Reward Model에 넣어서 Reward를 prediction  
6-4. Reward를 바탕으로 PPO모델을 학습시키면, 답변은 인간이 선호하는 답변을 하도록 training됌.(Reward Model이 인간의 선호대로 학습됐기 때문에 인간이 선호하는 답변에 대해서 큰 Reward를 return -> PPO는 큰 Reward를 얻는 방향으로 학습 -> 결국 인간이 선호하는 답변이 생성)  
ex) "Write a story about frogs"라는 Prompt를 PPO Model에 넣으면 어떤 답변을 생성. Prompt와 답변을 Reward Model에 넣으면 어떠한 reward를 얻을 수 있고 이를 바탕으로 PPO Model training.

## Conclusion & Limitation
기존에 단순히 모델의 크기를 키워서 최대한 user의 의도대로 모델이 행동할 수 있도록 했다면, 이 논문에서는 RLHF방식을 통해서 모델을 키우지 않고도 user의 의도대로 모델이 행동 할 수 있도록 만들었습니다. 해당 방식을 통해 GPT-3 175B모델보다 InstructGPT 1.3B모델의 output이 선호되었기 때문에 엄청난 computation resource를 아끼고, 효율적으로 모델을 만들 수 있었습니다. 하지만 다음과 같은 limitation이 존재한다고 저자들은 밝히고 있습니다.  
1. Need human labeling
2. No improvement in toxic, bias  

위의 방식을 사용하려면 SFT, Reward Model을 만들어야 하기 때문에 labeling을 위한 막대한 시간,비용이 들게 됩니다. 또한 toxic과 bias 측면에서는 개선되지 않았다고 주장하고 있습니다.

## Future Work
저자들은 RLHF에 focus를 두고 모델을 학습시켰지만 다른 많은 방법들이 존재할 수 있다고 주장합니다. 단순히 PPO가 아닌 다른 RL 알고리즘을 사용하여 모델을 학습시키거나, 인간이 직접 labeling한 dataset을 RL 방식이 아닌 다른 방식을 이용하여 모델을 학습시키는 등 많은 연구를 할 수 있을 것 같습니다.
