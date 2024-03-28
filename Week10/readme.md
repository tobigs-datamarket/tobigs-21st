# Week10. Generative Advanced, Speech

Update(2024.03.35.): Speech 과제 제출 기한 ~3/31(일)로 변경

## Part 1. Generative Advanced

과제 1, 2 중 하나를 선택해, 본인의 블로그나 노션, word 파일, PDF 등 원하는 방식으로 작성해주세요!

### 과제 1

대표적인 이미지 생성 모델들

1. GAN
2. VAE
3. Flow-base model
4. Diffusion

각각의 개념, 구조, 차이점을 정리해서 작성하기

### 과제 2

아래 References List에서 논문 하나를 선택하여 리뷰하기

- [2015] [Deep Unsupervised Learning using Nonequilibrium Thermodynamics](https://arxiv.org/abs/1503.03585)
- [2019] [Generative Modeling by Estimating Gradients of the Data Distribution(score-based generative modeling)](https://arxiv.org/abs/1907.05600)
- [2020] [Denoising Diffusion Probabilistic Models(DDPM)](https://proceedings.neurips.cc/paper/2020/hash/4c5bcfec8584af0d967f1ab10179ca4b-Abstract.html)
- [2021] [Denoising Diffusion Implicit Models(DDIM)](https://arxiv.org/abs/2010.02502)
- [2021] [Diffusion Models Beat GANs on Image Synthesis](https://arxiv.org/abs/2105.05233)
  - [2021] [Learning Transferable Visual Models From Natural Language Supervision(CLIP)](https://arxiv.org/abs/2103.00020)
  - [2019] [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer(T5)](https://arxiv.org/abs/1910.10683)
- [2021] [GLIDE: Towards Photorealistic Image Generation and Editing with Text-Guided Diffusion Models](https://arxiv.org/abs/2112.10741)
- [2021] [Score-Based Generative Modeling through Stochastic Differential Equations](https://arxiv.org/abs/2011.13456)
- [2021] [Variational Diffusion Models](https://arxiv.org/abs/2107.00630)
- [2022] [High-Resolution Image Synthesis with Latent Diffusion Models](https://arxiv.org/abs/2112.10752)
- [2022] [Elucidating the Design Space of Diffusion-Based Generative Models](https://arxiv.org/abs/2206.00364)
- [2022] [Classifier-Free Diffusion Guidance](https://arxiv.org/abs/2207.12598)
- [2022] [Tackling the Generative Learning Trilemma with Denoising Diffusion GANs](https://arxiv.org/abs/2112.07804)
- [2022] [Towards Practical Plug-and-Play Diffusion Models](https://arxiv.org/abs/2212.05973)
- [2023] [Consistency Models](https://arxiv.org/abs/2303.01469)

## Part 2. Speech

`Week10_Assignment.ipynb`에 과제 1, 2를 수행해주세요!

### 과제 1
- [ ] 5개의 질문에 대한 정답을 단답형으로 답하기

### 과제 2
아래 두 가지 조건
- [ ] 제공된 train dataset만을 활용하여 학습하기
- [ ] Pre-trained model은 사용하지 않기

을 지켜,
- [ ] 0 - 9 숫자 음원 데이터 2,000개를 이용하여 음성 분류 모델 만들기
- [ ] Test 폴더 내 300개의 음원 분류하기
  - [ ] 마지막에 test 음원 300개의 분류 결과를 모두 출력하기 e.g.) 3 1 4 1 5 9 2 6 ...

데이터셋 구성:
- Train
  - 화자 1명
  - 각 숫자당 200개의 음원, 총 2,000개의 음원 (348MB)
  - 한국어 발음 (영, 일, 이, 삼, 사, 오, 육, 칠, 팔, 구)
  - 각 음원 제목의 일의 자리가 label에 해당함
  - Stereo / Signed 16-bit PCM / Sampling rate: 44,100Hz
- Test
  - 화자 1명
  - 총 300개의 음원 (62MB)
  - 한국어 발음 (영, 일, 이, 삼, 사, 오, 육, 칠, 팔, 구)
  - Label 공개 ❌
  - Stereo / Signed 16-bit PCM / Sampling rate: 44,100Hz

### 필독: 당부사항

1. 데이터는 절대 외부로 유출해서는 안됩니다. 과제를 수행한 뒤 데이터셋을 완전히 삭제해주세요.
2. 데이터셋 공유 경로는 정규세션을 통해 안내해드렸습니다. 유출 방지를 위해 리포지토리에는 업로드되어있지 않습니다.
3. **반드시 commit에 데이터셋이 포함되지 않은 것을 확인하고 과제를 제출해주시기 바랍니다. 개인 리포지토리에서 수행한 commit은 관리자가 삭제할 수 없습니다.**

## 제출 방법
1. 본인의 이름으로 branch를 생성합니다.
2. `main`을 본인의 branch로 pull합니다.
3. **본인의 branch에서** 과제 디렉토리에 본인의 이름으로 디렉토리를 생성합니다.
4. 과제를 수행합니다. 디렉토리 구조:
   ```
   tobigs-21st
   └── Week1
       ├── EDA
       │   └── 김투빅
       │       └── example.md # 과제 파일
       └── Framework
           └── 김투빅
               └── example.md # 과제 파일
   ```
5. 변경된 본인의 branch를 commit, push합니다.
6. `이름(기수) - n주차 과제`라는 타이틀로 `Pull Request`를 등록합니다. 예) 김투빅(21기) - 1주차 과제

## 제출 기한
⏰ ~ 3/31(일) 23:59
