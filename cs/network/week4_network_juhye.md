---

### IEEE 803.11 MAC Protocol: CSMA/CA



### Collision Avoidance: RTS-CTS exchange

- 충돌은 결국 피할 수 없는 현상인데, 데이터에서의 큰 충돌보다는 RTS, CTS에서의 충돌 테스트를 해보고 충돌이 나지 않으면 안전한 채널에서 예약된 데이터를 전송



### 802.11 frame: addressing

- wifi에서 사용하는 프레임 구조

- address 1(이 무선프레임을 직접적으로 받는 인터페이스), address 2(이 프레임을 전송하는 인터페이스 어드레스), address 3(IP패킷을 처리하는 라우터 인터페이스), address 4(무시해도 됨)

- AP (라우터 입장에서는 H1만 보이고 AP는 보이지 않음) - 스위치와 다르게 mac address가 존재

- DHCP를 통해 내 IP address, subnet mask, Gateway Router IP, local Name Server IP를 알아냄



### 802.11  frame: more



### 802.11 : mobility within same subnet

- H1 remains in same IP subnet: IP address can remain same
- switch: which AP is associated with H1?
  - self-learning (Ch.5): switch will see frame from H1 and "remember" which switch port can be used to reach H1
- 같은 스위치 내에서 이동하면서 AP를 사용할 때, 커넥션이 유지될까 끊길까.

- client - TCP - server (socket이 연결되어 있음)
- TCP connection : 네가지 인덱스가 유지되는가에 따라 커넥션 유지가 결정됨 / 어떻게 인덱싱할 것인가? -> Source IP/port(송신), destination IP/port(수신)

- AP간 이동일 경우에는, 같은 서브넷을 공유하므로 TCP connection이 유지됨, server의 IP와 port는 영원히 변하지 않음 / 내 IP와 Port가 변할리 없으므로 연결이 유지됨. 

- 트래픽이 새로운 방향으로 흘러가기 위해서는 switch table을 바꾸면 됨. -> 셀프러닝이라는 기능을 사용해서 업데이트함. 



### 802.11: advanced capabilities

- Rate adaption: 채널 환경에 따라 데이터 rate를 조절

  - Base station, mobile dynamically change transmission rate(physical layer modulation technique) as mobile moves, SNR varis

  - 조금 더 많은 데이터를 심을 수 있고, 적은 데이터를 심을 수 있는데 이는 우리가 결정할 것. 

  - BER 한 비트당 에러가 발생할 확률

  - SNR decrease, BER increase -> 노이즈에 취약함



- Power management
  - 많은 전력을 절약함



### Cellular networks: the first hop

- 셀 안에서 무선통신과 기지국 간 어떤 통신이 이루어지는가

- 채널 파티셔닝 방식을 사용함

- Two techniques for sharing mobile-to-BS radio spectrum

  - Combined FDMA/TDMA:

    Divide spectrum in frequency channels, divide each channel into time slots

  - CDMA: code division multiple access 



### Multiple access techniques

- x축: time, y축: frequency
- FDMA : 유저들을 frequency를 따로 배분해여 충돌이 나지 않게 함
- TDMA : 유저들을 time을 따로 배분하여 충돌이 나지 않게 함
- CDMA : 각 사용자들에게 각기 다른 코드를 줘서 해당하는 데이터에만 증폭, 다른 데이터는 노이즈 처리. 



### Cellular evolution

2G-3G-4G(데이터가 1Gbps 이상인 경우)

- LTE-A 기술이 실제로 4G에 해당하는 기술 
- 상용화되기 위해서는 실제로 몇년 전부터 학계에서 개발중. (시장 오픈 전 기술 선점을 위해)
- LTE-A vs WiBro



### 3G (vocie+data) network architecture

key insight : new cellular data network operates in parallel (except at edge) with existing cellular voice network

- voice network unchanged in core
- data network operates in parallel



### Mobility Principles: addressing and routing to mobile users



### What is mobility?

- spectrum of mobility, from the network perspective

  - no mobility : mobile wireless user, using same access point

    이동 없이 한 곳에서 인터넷 사용

  - mobile user, connecting/disconnecting from network using DHCP.

    이동은 하지만 TCP 연결을 끊고 이동 후, 새로 연결. TCP 연결 유지 x

  - High mobility : mobile user, passing through multiple access point while maintaining ongoing connections (like cell phone) TCP 연결 유지하는 상황에서 다른 네트워크 이동하는 상황

- 어떻게 TCP 연결을 유지시킬까?



### Mobility: registration

모바일 호스트가 어디로 이동하든지 perment address가 알고 있음. - 알아서 유지시켜줌

(상상의 indirect routing 방식)

편한 대신에 딜레이가 많이 생김.

- direct routing : 훨씬 direct한 connection이 되나 직접 모든걸 알아야 함



---



### Multimedia networking

어떻게 유튜브같은 멀티미디어 서비스가 동작하는가?

application layer



### Multimedia: AUDIO

- sampling: 아날로그 시그널을 디지털 시그널로 변환하는 작업. 연속적으로 작업할 수 있는 것이 아니기 때문에 주기적으로 판단. 항상 오차가 발생하므로 오차를 줄이기 위해서는 비트의 수가 크면 클수록, 주기가 짧을수록 에러가 줄고, 오리지널 원음에 가까워짐

- cd가 더 고음질



### Multimedia: video

- 이미지의 연속

- 이미지는 프레임. 픽셀에 어떤 색깔 밸류가 나타나는가. 이웃한 픽셀에는 비슷한 색

- 중복되는 픽셀을 압축시킴
- Coding rate가 높을수록 화질이 좋음



### Multimedia networking: 3 application types

- streaming, stored audio, video
  - Streaming: can begin playout before downloading entire file
  - Stored (at server): can transmit faster than audio/video will be renderred (implies storing/buffering at client)
  - 서버에 저장된 오디오와 비디오
  - e.g. YouTube, Netflix

- conversational
  - e.g. skype
- streaming live : 서버에 저장된 것이 아님



### Streaming stored video:

- 바로 플레이시키는게 아니라 기다렸다가 플레이 -> 버퍼링
- 버퍼링이 길면 길수록 안 끊기므로좋을까? -> 너무 길면 못 기다리므로 사람의 인내심 선에서...



### Client-side buffering, playout

1. Intial fill of buffer until playout begins at tp
2. playout begins at tp
3. buffer fill level varies over time as fill rate x(t) varies and playout rate r is constant



### Streaming multimedial: DASH

- DASH: Dynamic, Adaptive Streaming over HTTP
- Server:
  - divides video file into multiple chunks
  - Each chunk stored, encoded at different rates
- 2GB 영상 -> 통째로 저장하는 것이 아니라 2 Mbps 작은 단위(chunks)로 쪼개서 저장

- 128kbps, 256kbps, 512kbps, 1mbps, 2mbps, 5mbps...일 때 5mpbs가 가장 좋은 버전
- 각 chunks별 인코딩 된 url -> manifest file에 담아둠
- 처음 영상을 실행하면 128kbps부터 틀어주다가 네트워크 상황에 따라 인코딩 버전을 틀어주고, 네트워크가 안좋아지면 다시 낮춤
- 네트워크 상황에 따라 다이나믹하게 최대한의 화질을 서비스함

- 동시에 요청하는 전세계의 유튜브 사용자가 많으므로, 어디에 저장할 것인가? 한 곳에 저장하는 것이 아니라 전세계에 각각 저장하는 CDN 방식 사용함.



---



## Network Security

### What is network security 네트워크 보안의 4요소

- Confidentially 기밀성: sender와 receiver만 알아야 함
- authentication 인증: 상대방이라는 것을 확신할 수 있어야 함.
- message integrity 메시지 : 보내는 사람이 변하지 않고 받는 사람이 그대로 받아야 함. 중간에 누군가 변하게 하면 안됨.

- access and availability: 서비스를 제공하는 사람은 24시간 내내 사용자에게 서비스를 제공할 수 있어야 함. 공격자로부터 방어



### Public Key Cryptography

- symmetric key crypto
  - 암호화 하기 위해서는 암호화 하는 key와 해독하는 key 필요
- Public key crypto
  - 모든 사람에게 공개되는 public key와 자기 자신만 볼수 있는 private key 가짐
  - RSA78: 앨리스가 공개된 public key로 밥에게 메시지를 보냄-> 밥은 자기 자신만 볼수 있는 private key로 암호 해독
    - key의 순서가 상관 없음. 더 많은 시간 소요



### Authentication: yet another try

- Goal: avoid playback attack
- 신뢰할 수 있는 발신자에 대한 검증 필요



