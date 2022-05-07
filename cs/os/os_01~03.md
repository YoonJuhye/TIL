# OS-01-Introduction

### 1. 운영체제(Operating System, OS)란?

- 컴퓨터 하드웨어 바로 위에 설치되어 사용자 및 다른 모든 소프트웨어와 하드웨어를 연결하는 소프트웨어 계층
- 협의의 운영체제 (커널) - *전공자 입장에서의 운영체제*: 운영체제의 핵심 부분으로 메모리에 상주하는 부분
- 광의의 운영체제: 커널 뿐 아니라 각종 주변 시스템 유틸리티를 포함한 개념
- *하드웨어(자원)를 효율적으로 관리하는 것이 운영체제의 가장 중요한 역할이자 목적*

### 2. 운영체제의 목표

- 컴퓨터 시스템을 편리하게 사용할 수 있는 환경을 제공
  - 운영 체제는 동시 사용자/프로그램들이 각각 독자적 컴퓨터에서 수행되는 것 같은 환상을 제공
  - 하드웨어를 직접 다루는 다른 복잡한 부분을 운영체제가 대행
- 컴퓨터 시스템의 자원을 효율적으로 관리
  - 프로세서, 기억장치, 입출력 장치(하드웨어 자원) 등의 효율적 관리
    - 사용자간의 형평성 있는 자원 분배 필요
    - 주어진 자원으로 최대한의 성능을 내도록 관리
    - 실행중인 프로그램들에게 짧은 시간씩 CPU를 번갈아 할당
    - 실행중인 프로그램들에 메모리 공간을 적절히 분배
  - 사용자 및 운영체제 자신의 보호
  - 프로세스, 파일, 메시지(소프트웨어 자원) 등을 관리

### 3. 운영체제의 분류 - 동시 작업 가능 여부

- 단일 작업 (single tasking)

  - 한 번에 하나의 작업만 처리

    예) MS-DOS 프롬포트 상에서는 한 명령의 수행을 끝내기 전에 다른 명령을 수행시킬 수 없음

- 다중 작업 (multi tasking)

  - 동시에 두 개 이상의 작업 처리

    예) UNIX, MS Windows 등에서는 한 명령의 수행이 끝나기 전에 다른 명령이나 프로그램을 수행할 수 없음

### 4. 운영체제의 분류 - 사용자의 수

- 단일 사용자 (single user)

  예) MS-DOS, MS Windows

- 다중 사용자 (multi user)

  예) UNIX, NT server

### 5. 운영체제의 분류 - 처리방식

- 일괄 처리 (batch processing)

  - 작업 요청의 일정량 모아서 한꺼번에 처리
  - 작업이 완전 종료될 때까지 기다려야 함

  예) 초기 Punch Card 처리 시스템

  - interactive 하지 않음 (역사적의 시스템)

- 사분할 (time sharing)

  - 여러 작업을 수행할 때 컴퓨터 처리 능력을 일정한 시간 단위로 분할하여 사용

  - 일괄 처리 시스템에 비해 짧은 응답 시간을 가짐

    예) UNIX

  - interactive한 방식

  - 범용적 사용

- 실시간 (Realtime OS)

  - 정해진 시간 안에 어떠한 일이 반드시 종료됨(데드라인)이 보장되어야 하는 실시간시스템을 위한 OS

  - 특수한 목적을 가진 시스템에서 사용

    예) 원자로/공장 제어, 미사일 제어, 반도체 장비, 로보트 제어 (한 공정이 멈추면 다른 공정도 밀려서 정전 시 문제 초래)

  - 실시간 시스템의 개념 확장

    - Hard realtime system (경성 실시간 시스템)
    - Soft realtime system (연성 실시간 시스템)

### *몇가지 용어

- Multitasking
- Multiprogramming
- Time sharing (멀티태스킹과 유사하지만 CPU를 좀 더 강조한 용어)
- Multiprocess
- 구분
  - 위의 용어들은 컴퓨터에서 여러 작업을 동시에 수행하는 것을 뜻한다
  - Multiprogramming은 여러 프로그램이 메모리에 올라가 있음을 강조
  - Time Sharing은 CPU의 시간을 분할하여 나누어 쓴다는 의미를 강조
- **Multiprocessor** : 위의 용어들과 다르게 하나의 컴퓨터에 CPU(processor)가 여러 개 붙어 있음을 의미

### 6. 운영 체제의 예

- 유닉스 (UNIX)
  - 코드의 대부분을 C언어로 작성
  - 높은 이식성 - Potable
  - 최소한의 커널(메모리 핵심 부분) 구조
  - 복잡한 시스템에 맞게 확장 용이
  - 소스 코드 공개 - 누구나 이용 가능, 학술적 사용 가능
  - 프로그램 개발에 용이
  - 다양한 버전
    - System V, FreeBSD, SunOS, Solaris
    - Linux
  - (안드로이드도 운영체제 커널은 리눅스를 사용하고 있음)
- DOS(Dist Operating System)
  - MS사에서 1981년 IBM-PC를 위해 개발
  - 단일 사용자용 운영체제, 메모리 관리 능력의 한계(주 기억장치 : 640KB)
- MS Windows
  - MS사의 다중 작업용 GUI 기반 운영 체제
  - Plug and Play, 네트워크 환경 강화
  - DOS용 응용 프로그램과 호환성 ㅈ공
  - 불안정성
  - 풍부한 자원 소프트웨어
- Handheld device를 위한 OS
  - PalmOS, Pocket PC (WinCE), Tiny OS

### 7. 운영체제의 구조

CPU 스케쥴링 - 누구에게 CPU를 줄까?

메모리 관리 - 한정된 메모리를 어떻게 쪼개어 쓰지?

파일 관리(Disk) - 디스크에 파일을 어떻게 보관하지?

입출력 관리(I/O device) - 각기 다른 입출력장치와 컴퓨터 간에 어떻게 정보를 주고 받게 하지?

프로세스 관리 - 프로세스의 생성과 삭제, 자원할당 및 반환, 프로세스 간 협력

그 외 - 보호 시스템, 네트워킹, 명령어해석기(command line interpreter)



# OS-02-System Structure & Program Execution

### 컴퓨터 시스템 구조

Computer - CPU, Memory

I/O device - Disk, 키보드, 마우스, 모니터, 프린터 등

device controller가 작업

------

### **CPU & Memory**

- Memory : CPU의 작업 공간. 프로그램이 실행되는 동안 명령어와 데이터를 저장한다.
- CPU는 메모리에서 명령어를 읽어서 실행
- 읽어오는 요청은 직접 디스크에 접근하는 것이 아님.
- CPU의 전체적인 통제를 OS가 담당. CPU는 지시된 것을 계속 실행하는 것



### Mode bit

- 사용자 프로그램의 잘못된 수행으로 다른 프로그램 및 운영체제에 피해가 가지 않도록 하기 위한 보호 장치 필요

- Mode bit을 통해 하드웨어적으로 두 가지 모드의 operation 지원

  1 사용자 모드: 사용자 프로그램 수행 (한정된 명령 수행 가능)

  0 모니터 모드(=커널 모드, 시스템 모드): OS 코드 수행

  - 보안을 해칠 수 있는 중요한 명령어는 모니터 모드에서만 수행 가능한 “**특권 명령**”으로 규정
  - interrupt나 Exception 발생시 하드웨어가 mode bit을 0으로 바꿈
  - 사용자 프로그램에게 CPU를 넘기기 전에 mode bit을 1로 셋팅

  

### **Timer (하드웨어)**

- 정해진 시간이 흐른 뒤 운영체제에게 제어권이 넘어가도록 인터럽트를 발생시킴
- CPU를 특정 프로그램이 독점하는 것으로부터 보호
- 매 클럭 틱 때마다 1감소
- 타이머 0이 되면 타이머 인터럽트 발생
  - 할당된 시간만큼 실행하고 끝나면 CPU에 타이머 인터럽트 발생
  - 정해진 시간 후 운영체제에게 제어권이 넘어감
- Time Sharing을 구현하기 위해 널리 이용됨
- 타이머는 현재 시간을 계산하기 위해서도 사용



### Device Controller

- **I/O Device Controller (하드웨어)**
  - 해당 I/O 장치유형을 관리하는 일종의 작은 CPU
    - CPU와 병렬로 실행되어 메모리 사이클을 놓고 경쟁한다. (누가 메모리에 접근할 것인가)
  - 제어 정보를 위해 control register, status register를 가짐
  - local buffer를 가짐 (일종의 data register)
- I/O는 실제 device와 local buffer 사이에서 일어남
- Deviece controller는 I/O가 끝났을 경우 인터럽트로 CPU에 그 사실을 알림
- device driver(장치구동기) : OS 코드 중 각 장치별 처리 루틴 -> Software
- device controller(장치제어기) : 각 장치를 통제하는 일종의 작은 CPU -> Hardware



### 입출력(**I/O)의 수행**

- 모든 입출력 명령은 특권 명령 (커널 모드에서만 할 수 있음)

- 사용자 프로그램은 어떻게 I/O하는가?

  - 시스템콜(system call) : 사용자 프로그램이 운영체제의 서비스를 받기 위해 커널 함수를 호출하는 것
    - 사용자 프로그램은 OS에게 I/O 요청
  - trap을 사용하여 인터럽트 벡터의 특정 위치로 이동
  - 제어권이 인터럽트 벡터가 가리키는 인터럽트 서비스 루틴으로 이동
  - 올바른 I/O 요청인지 확인 후 I/O 수행
  - I/O 완료 시 제어권을 시스템콜 다음 명령으로 옮김

  

### 인터럽트 (Interrupt)

- 인터럽트
  - 인터럽트 당한 시점의 레지스터와 Program Counter를 save한 후 CPU의 제어를 인터럽트 처리 루틴에 넘김
- Interrupt (넓은 의미)
  - Interrupt (하드웨어 인터럽트) : 하드웨어가 발생시킨 인터럽트
  - Trap (소프트웨어 인터럽트)
    - Exception : 프로그램이 오류를 범한 경우 (0으로 나누는 연산 등)
    - System call : 프로그램이 커널 함수를 호출하는 경우
- 인터럽트 관련 용어
  - 인터럽트 벡터
    - 해당 인터럽트의 처리 루틴 주소를 가지고 있음
  - 인터럽트 처리 루틴 (=Interrupt Service Routine, 인터럽트 핸들러 )
    - 해당 인터럽트를 처리하는 커널 함수
- 현대의 운영체제는 인터럽트에 의해 구동됨



### 동기식 입출력과 비동기식 입출력

- 동기식 입출력 (synchronous I/O)
  - I/O 요청 후 입출력 작업이 완료된 후에야 제어가 사용자 프로그램에 넘어감
  - 구현 방법 1
    - I/O 끝날 때까지 CPU를 낭비시킴 (완료까지 기다려야하므로)
    - 매 시점 하나의 I/O만 일어날 수 있음
  - 구현 방법 2 (CPU 낭비도 안되고 I/O 장치도 동시 실행 가능)
    - I/O 완료될 때까지 해당 프로그램에게서 CPU 빼앗음
    - I/O 처리를 기다리는 줄에 그 프로그램을 줄 세움
    - 다른 프로그램에게 CPU를 줌
- 비동기식 입출력 (Asynchronous I/O)
  - I/O 시작된 후 입출력 작업이 끝나기를 기다리지 않고 제어가 사용자 프로그램에 즉시 넘어감
- 두 경우 모두 I/O의 완료는 인터럽트로 알려줌

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/40a9a7ee-a17d-486f-b766-8898daeb3918/Untitled.png)



### **DMA(Direct Memory Access)**

- 메모리에 접근 가능한 장치
- I/O 장치가 매우 다양해서 CPU가 인터럽트를 너무 많이 당하므로 직접 메모리에 접근할 수 있게 만듦
- 빠른 입출력 장치를 메모리에 가까운 속도로 처리하기 위해 사용
- CPU의 중재 없이 device controller가 device의 buffer storage의 내용을 메모리에 block 단위로 직접 전송
- 바이트 단위가 아니라 **block 단위**로 인터럽트 발생시킴
- CPU는 DMA가 일을 다 하면 한번만 인터럽트 당함. CPU의 인터럽트 빈도가 줄고 효율적으로 가능



### 서로 다른 입출력 명령어

- I/O를 수행하는 special instruction에 의해

  - 메모리와 I/O가 별개의 어드레스 영역에 할당되는 것을 의미한다.

- Memory Mapped I/O에 의해

  - 메모리와 I/O가 **하나의 연속된 address 영역에 할당**된다

  

### 저장장치 계층 구조

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1dc2b4ea-4a8b-4796-9e55-bf7afdec50d3/Untitled.png)

- 위로 갈수록 속도가 빠르나 비용 높고 용량이 적음, 휘발성,
- Primary: 휘발성
- Secondary: 비휘발성
- 캐싱: 어떤 것을 쫓아낼 것인가가 중요한 이슈 ( 뒤에서 자세히 설명)



### 프로그램의 실행 (메모리 load)

- File System: 비휘발성(전원이 나가도 유지됨)
- Vitual Memory: 각 프로그램마다 독자적으로 가지고 있는 메모리 공간
- Physical Memory: 당장 필요한 부분만 올리고 나머지는 Swap area(전원이 내려가면 의미가 사라짐)에 내려 놓음
- 주소변환: 하드웨어의 지원을 받아 가상메모리 주소를 물리적메모리 주소로 바꿈



### 커널 주소 공간의 내용

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2065bacc-19b0-47e7-a5e8-50641381bd70/Untitled.png)

- 하드웨어를 관리하기 위해 자료구조를 만들어둠
- PCB: 프로그램마다 관리하기 위한 자료구조
- stack: 함수를 리턴하기 위해 사용



### 사용자 프로그램이 사용하는 함수

- 함수 (function)
  - 사용자 정의 함수
    - 내 프로그램에서 정의한 함수
  - 라이브러리 함수
    - 내 프로그램에서 정의하지 않고 갖다 쓴 함수
    - 자신의 프로그램의 실행 파일에 포함되어 있음
  - 커널 함수
    - 운영체제 프로그램의 함수
    - 커널 함수의 호출 = 시스템 콜

### 프로그램의 실행

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4cd834ec-538a-4b37-b74c-c0c3da06ba29/Untitled.png)

- 유저모드-커널모드 반복



# OS-03-Process

### 프로세스의 개념

- “Process is a program in execution” : 실행 중인 프로그램
- 프로세스의 문맥 (context) : 프로세스의 현재 상태를 나타내는데 필요한 모든 요소
  - CPU 수행 상태를 나타내는 하드웨어 문맥 : 현재 시점에 프로세스를 어디까지 실행했는지 확인
    - Program counter
    - 각종 register
  - 프로세스의 주소 공간
    - code, data, stack
  - 프로세스 관련 커널 자료 구조 (관리)
    - PCB(Process Control Block)
    - Kernel stack (프로세스 별로 별도로 커널 스택을 두고 있음)

→ 번갈아가면서 프로그램이 실행되기 때문에 문맥을 알아야 instruction 순서를 제대로 실행 가능함



### **프로세스의 상태 (Process State)**

- 프로세스는 상태(state)가 변경되며 수행된다.
  - Running
    - CPU를 잡고 instruction을 수행중인 상태
  - Ready
    - CPU를 기다리는 상태 (메모리 등 다른 조건을 모두 만족하는 상태)
  - Blocked (wait, sleep)
    - CPU를 주어도 당장 instruction을 수행할 수 없는 상태
    - process 자신이 요청한 event(예: I/O)가 즉시 만족되지 않아 이를 기다리는 상태
    - 예) 디스크에서 file을 읽어와야 하는 경우
    - 자신이 요청한 event가 만족되면 Ready
  - Suspended (stopped)
    - 외부적인 이유로 프로세스의 수행이 정지된 상태
    - 프로세스는 통째로 디스크에 swap out 된다
    - 예) 사용자가 프로그램을 일시 정지 시킨 경우(break key) 시스템이 여러 이유로 프로세스를 잠시 중단시킴 (메모리에 너무 많은 프로세스가 올라와 있을 때=Medium-term Scheduler)
    - 외부에서 resume해 주어야 Active
- New : 프로세스가 생성 중인 상태 (보통 프로세스의 상태로 포함되지 않음)
- Terminated : 수행이 끝난 상태 (보통 프로세스의 상태로 포함되지 않음)



### Process Control Block (PCB)

- PCB (Process Control Block)

  - 운영체제가 각 프로세스를 관리하기 위해 프로세스당 유지하는 정보

- 다음의 구성 요소를 가진다 (구조체로 유지)

  - (1) OS가 관리상 사용하는 정보

    - Process state, Process ID
    - Scheduling information, Priority

  - (2) CPU 수행 관련 하드웨어 값

    - Program Counter, registers

  - (3) 메모리 관련

    - Code, Data, Stack의 위치정보

  - (4) 파일 관련

    - Open File Descriptors

      

### **문맥 교환 (Context Switch) - 중요**

- CPU를 한 프로세스에서 다른 프로세스로 넘겨주는 과정

- CPU가 다른 프로세스에게 넘어갈 때 운영체제는 다음을 수행

  - CPU를 내어주는 프로세스의 상태를 그 프로세스의 PCB에 저장
  - CPU를 새롭게 얻는 프로세스의 상태를 PCB에서 읽어옴

- System call 이나 Interrupt 발생시 반드시 context switch가 일어나는 것은 아님

  (1) User mode →           kernel mode          → User mode

  프로세스A       ISR or system call 함수      프로세스 A

  (2) User mode →          kernel mode                  →               User mode

  프로세스A                                        문맥교환 일어남       프로세스B



### **프로세스 스케줄링하기 위한 큐**

- 프로세스들은 각 큐들을 오가며 수행된다.
- Job Queue
  - 현재 시스템 내에 있는 모든 프로세스의 집합 (Ready Queue + Device Queues)
- Ready Queue
  - 현재 메모리 내에 있으면서 CPU를 잡아서 실행되기를 기다리는 프로세스 집합 (Device Queue와 베타관계)
- Device Queues
  - I/O device 의 처리를 기다리는 프로세스 집합 (Ready Queue와 베타적 관계)

### **스케줄러 (Scheduler)**

자원 별로 순서를 정해주는 것.

- Long-term Scheduler (장기 스케줄러 or Job scheduler)

  - 시작 프로세스 중 어떤 것들을 ready queue로 보낼지 결정

    (프로그램 시작할 때 new 상태에서 메모리를 줘서 ready 상태로 갈 프로세스를 결정)

  - 프로세스에 memory(및 각종 자원)을 주는 문제

  - degree of Multiprogramming을 제어 (메모리에 올라갈 프로세스 수)

    (메모리에 올라간 프로그램이 너무 적거나 많으면 CPU 효율, 성능이 좋지 않음)

  - Time sharing system 에서는 보통 장기 스케줄러가 없음

    (무조건 ready 상태 - 결정 단계 없이 바로 메모리에 올라감)

- Short-term Scheduler (단기 스케줄러 or CPU scheduler)

  - 어떤 프로세스를 다음번에 running 시킬지 결정
  - 프로세스에 CPU를 주는 문제
  - millisecond 단위로 충분히 빨라야 함

- Medium-term Scheduler (중기 스케줄러 or Swapper)

  - 메모리 여유 공간 마련을 위해 프로세스를 통째로 메모리에서 디스크로 쫓아냄
  - 프로세스에게서 memory를 뺏는 문제 → 시스템 입장에서 더 효과적
  - degree of Multiprogramming을 제어



### Thread

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/975e2130-1f6d-4253-a7d5-197010538e1b/Untitled.png)

- Thread : 프로세스 하나에 CPU 수행 단위만 여러 개 두고 있는 것

- "A thread (or lightweight process) is a basic unit of CPU utilication"

  프로세스(heavyweight process) 내부에 CPU 수행 단위가 여러개 존재하는 경우, CPU를 수행하는 단위

- thread 의 구성

  - Program Counter
  - register set
  - stack space

- Task = Thread가 동료 Thread 와 공유하는 부분

  thread가 여러 개 있으면 task는 하나만 있음

  - code section
  - data section
  - os resources

- 전통적인 개념의 heavyweight process는 하나의 thread를 가지고 있는 task로 볼 수 있다.

장점

- 다중 스레드로 구성된 태스크 구조에서는 하나의 서버 스레드가 blocked(waiting) 상태인 동안에도 동일한 태스크 내의 다른 스레드가 실행(running)되어 빠른 처리를 할 수 있음.
  - 사용자에게 빠른 응답성을 보여줄 수 있음
- 동일한 일을 수행하는 다중 스레드가 협력하여 높은 처리율(throughput)과 성능 향상을 얻을 수 있다
  - 메모리 낭비를 줄일 수 있음.
- 스레드를 사용하면 병렬성을 높일 수 있다 (CPU가 여러개인 컴퓨터인 경우에만 가질 수 있는 장점) - 각 스레드들이 서로 다른 CPU에서 실행되고 pararell 하게 병렬적으로 실행되므로 결과를 빨리 얻을 수 있음

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fbd16f0d-cafd-42fc-a9cb-485e7c4b81e6/Untitled.png)

### Benefits of Threads

- Responsiveness (응답성)
  - 사용자 입장에서 빠름
  - eg) multi-threaded Web (여러 개의 스레드)
    - if one thread is blocked (eg network)
    - another thread continues (eg display) → 비동기식 입출력
- Resource Sharing (자원 공유)
  - 자원을 효율적으로 사용 가능
  - n threads can share binary code, data, resource of the process
- Economy (경제성)
  - creating & CPU switching thread (rather than a process)
    - 프로세스 하나를 생성하고 CPU를 스위치하는 것보다 스레드를 하나 생성하고 CPU를 스위치하는 것이 훨씬 overhead가 적음
  - Solaris의 경우 위 두 가지 overhead가 각각 30배, 5배
    - 같은 작업이라면 프로세스를 여러 개 만드는 것보다 스레드를 생성하는 것이 훨씬 경제적

→ CPU가 한 개 있는 경우의 장점

- Utilization of MP(Multi Processor) Architectures (CPU가 여러개 있는 경우의 장점)
  - each thread may be running in parallel on a different processor
  - 병렬적으로 작동할 수 있어서 효율적

### Implementation of Threads

- Some are supported by kernel ⇒ Kernel Threads
  - Windows 95/98/NT
  - Solaris
  - Digital UNIX, Mach
- Others are supported by library ⇒ User Threads
  - POSIX Pthreads
  - Mach C-threads
  - Solaris threads
- Some are real-time threads

<hr>



# OS-04-Process Management

### **프로세스 생성 (Process Creation)**

- 부모 프로세스(Parent process)가 자식 프로세스(children process)를 생성

  COW : Copy-On-Write = 자식은 부모 자원을 그대로 공유하여 사용하고 있다가 write 발생할 경우 복사

- 프로세스의 트리(계층 구조) 형성

- 프로세스는 자원을 필요로 함

  - 운영체제로부터 받는다
  - 부모와 공유한다

- 자원의 공유

  - 부모와 자식이 모든 자원을 공유하는 모델
  - 일부를 공유하는 모델
  - 전혀 공유하지 않는 모델

- 수행 (Execution)

  - 부모와 자식은 공존하며 수행되는 모델
  - 자식이 종료(terminate)될 때까지 부모가 기다리는(wait-블럭된 상태) 모델

- 주소 공간(Address space)

  - 자식은 부모의 공간을 복사함 (binary and OS data) -fork
  - 자식은 그 공간에 새로운 프로그램을 올림 (복제 생성 후 덮어 씌움-exec)

- UNIX의 예

  - fork()

     시스템 콜이 새로운 프로세스를 생성

    - 부모를 그대로 복사 (OS data except PID + binary)
    - 주소 공간 할당

  - fork 다음에 이어지는 **exec()** 시스템 콜을 통해 새로운 프로그램을 메모리에 올림

  

### **프로세스 종료 (Process Termination)**

- 프로세스가 마지막 명령을 수행한 후 운영체제에게 이를 알려줌 

  (exit)

  - 자식이 부모에게 output data를 보낸다 (via **wait**)
  - 프로세스의 각종 자원들이 운영체제에게 반납됨

- 부모 프로세스가 자식의 수행을 종료시킴 

  (abort)

  - 자식이 할당 자원의 한계치를 넘어설 때
  - 자식에게 할당된 테스크가 더 이상 필요하지 않을 때
  - 부모가 종료(exit) 하는 경우
    - 운영체제는 부모 프로세스가 종료하는 경우 자식이 더 이상 수행되도록 두지 않는다
    - 단계적인 종료 (딸려있는 모든 자식을 종료시킨 후 부모를 죽임)

