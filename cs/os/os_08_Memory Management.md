# Chapter 8. Memory Management

### 1. Logical Address vs Physical Address

- Logical Address (=Virtual Address) (논리주소=가상주소)

  - 프로세스마다 독립적으로 가지는 주소 공간

  - 각 프로세스마다 0번지부터 시작

  - **CPU가 보는 주소는 Logical Addrss**

- Physical Address (물리적 주소)
  - 메모리에 실제 올라가는 위치

\* 주소 바인딩 :  (어디로 올라갈 지) 주소를 결정하는 것 (주소 변환)

​	Symbolic Address -> Logical Address -> Physical Address

- Symbolic Address : 프로그래머는 숫자로 된 주소를 사용하지 않고 심볼로된 주소를 사용한다. => 컴파일 되면 숫자인 Logical Address => 실행되려면 물리적 메모리에 올라가야하므로 주소변환이 이루어져야한다. (주소결정 = Address Binding) => Physical Address

\* 각 프로그램마다 가지고 있는 논리적 주소가 물리적 주소로 언제 결정되는가? => 총 3가지 시점으로 나눌 수 있다.



### 2. 주소 바인딩 (Address Binding)

- Compile Time Binding (컴파일 시)

  - 물리적 메모리 주소(Physical Address)가 컴파일 시 알려짐

  - 시작 위치 변경시 재컴파일
  - 컴파일러는 절대 코드(Absolute Code) 생성 ( = 컴파일시 주소가 Fixed 된다.)

- Load Time Binding (실행이 시작될 시)

  - Loader의 책임하에 물리적 메모리 주소 부여

  - 컴파일러가 재배치가능코드(Relocatable Code)를 생성한 경우 가능 ( = 정해져 있는 것이 아니라 실행시 비어있는 곳 어디든 올라간다.)

- Execution Time Binding (=Run Time Binding) (실행도중)

  - 수행이 시작된 이후에도 프로세스의 메모리 상 위치를 옮길 수 있음.

  - CPU가 주소를 참조할 때마다 Binding을 점검 (Address Mapping Table)

  - **하드웨어적인 지원이 필요** (ex. base and limit registers, MMU) - 주소 변환을 도와줌
  - 주소가 계속 바뀔 수 있음

![image-20220516113052244](os_08_Memory Management.assets/image-20220516113052244.png)



### 3. Memory Management Unit (MMU)

- MMU (Memory Management Unit)
  - Logical Address를 Physical Address로 매핑해주는 Hardware Device

- MMU Scheme

  사용자 프로세스가 CPU에서 수행되며 생성해내는 모든 주소 값에 대해 Base Register (=Relocation Register)의 값을 더한다.

- User Program

  - Logical Address만을 다룬다.

  - 실제 Physical Address를 볼 수 없으며 알 필요가 없다.

    ### Dynamic Relocation
    
    ![image-20220516114046306](os_08_Memory Management.assets/image-20220516114046306.png)
    
    
    
    P1 프로세스 실행 중 상황 (논리주소: 0-3000번지, 물리 주소: ~14000번지) 346번지를 달라고 할 때, 
    
    시작 위치 14000번지와 논리주소를 더해주면 됨 (요청한 논리주소+시작 위치=물리주소)
    
    리미트 레지스터를 체크해줌. 프로그램의 크기를 담고 있음(3000). 프로그램이 악의적이어서 3000번지까지밖에 없는데 메모리4000번지를 달라고 하면 시작위치를 4000에 더해주면 18000번지. 다른 프로그램이 존재하는 메모리위치가 됨. 이걸 막아야 하므로 limit register를 넘는 주소를 요청하면 trap이 걸림
    
    ### hardware Support for Address Translation
    
    ![image-20220516114657665](os_08_Memory Management.assets/image-20220516114657665.png)
    
    운영체제 및 사용자 프로세스 간의 메모리 보호를 위해 사용하는 레지스터
    
    - Relocation register : 접근할 수 있는 물리적 메모리 주소의 최소값 (=base register)
    - Limit register : 논리적 주소의 범위
    
    


### 4. Some Terminologies

- Dynamic Loading
- Dynamic Linking
- Overlays
- swapping



### 1) Dynamic Loading

프로그램을 메모리에 동적으로 올린다 =그때그때 필요할 때마다 루틴을 메모리에 올린다 

- 프로세스 전체를 메모리에 미리 다 올리는 것이 아니라 해당 루틴이 불려질 때 메모리에 load

- Memory Utilization의 향상
- 가끔씩 사용되는 많은 양의 코드의 경우 유용 
  - 예) 오류 처리 루틴

- 운영체제의 특별한 지원 없이 프로그램 자체에서 구현 가능 ( 운영체제가 라이브러리를 제공해주며 그걸 이용하여 구현)
- Loading : 메모리에 올리는 것을 의미

- 현재 컴퓨터 시스템도 필요한 부분만 메모리에 올라가고 필요 없는 부분은 다시 내림 => Dynamic Loading(프로그래머가 관리)이 아니라 운영체제가 직접 관리해주는 Paging System에 해당(지금은 이 용어를 섞어 쓰기도 함)



### 2) Overlays 

- 메모리에 프로세스의 부분 중 실제 필요한 정보만을 올림
- 프로세스의 크기가 메모리보다 클 때 유용
- 운영체제의 지원없이 사용자에 의해 구현
- 작은 공간의 메모리를 사용하던 초창기 시스템에서 수작업으로 프로그래머가 구현
  - Manual Overlay
  - 프로그래밍이 매우 복잡
- 프로그래머가 큰 프로그램을 쪼개서 올리고 내리는 것을 직접 코딩 해야 함. Dynamic Loading은 라이브러리 이용



### 3) Swapping

- Swapping
  - 프로세스를 일시적으로 메모리에서 backing store로 쫓아내는 것
- Backing store (=swap area)
  - 디스크
    - 많은 사용자의 프로세스 이미지를 담을 만큼 충분히 빠르고 큰 저장 공간

- Swap In / Swap Out

  - 일반적으로 중기 스케줄러(swapper)에 의해 Swap Out 시킬 프로세스 선정

  - Priority-Based CPU Scheduling Algorithm
    - Priority가 낮은 프로세스를 Swapped Out 시킴 (쫓아냄)
    - Priority가 높은 프로세스를 메모리에 올려 놓음

  - Compile Time 혹은 Load Time Binding에서는 원래 메모리 위치로 Swap In 해야 함
  - Execution time binding에서는 추후 빈 메모리 영역 아무 곳에나 올릴 수 있음

  - Swap Time은 대부분 Transfer Time (Swap 되는 양에 비례하는 시간)임




	### Schematic View of Swapping

![image-20220516115836339](os_08_Memory Management.assets/image-20220516115836339.png)



Swap Time? 보통 디스크를 접근하는 시간은 Seek Time(디스크 헤더가 이동하는 시간)이 대부분을 차지하고 Transfer Time(데이터 전송 시간)은 미미하다. 그런데, 용량이 방대한 *Swapping에서는 파일입출력과는 다르게 디스크 접근 시간 대부분이 Swap 되는 데이터 양에 비례하는 Transfer Time이 차지한다.

1. Swap Out : Main Memory-> Swap Area
2. Swap In : Swap Area -> Main Memory



### 4) Dynamic Linking

프로그램 작성 후 컴파일하고 링크에서 실행파일을 만듬. 링킹이란 여려 곳에 존재하는 컴파일된 파일들을 하나로 묶어서 실행파일로 만드는 과정

- Linking을 실행 시간(execution time)까지 미루는 기법

- Static Linking

  - 라이브러리가 프로그램의 실행 파일 코드에 포함됨

  - 실행 파일의 크기가 커짐

  - 동일한 라이브러리를 각각의 프로세스가 메모리에 올리므로 메모리 낭비 (eg. printf 함수의 라이브러리 코드)

- Dynamic Linking (=shared Library, 리눅스-Shared Object, 윈도우-DLL (Dynamic Linking Library))

  - 라이브러리가 실행시 연결(link)됨

  - 라이브러리 호출 부분에 라이브러리 루틴의 위치를 찾기 위한 stub이라는 작은 코드를 둠

  - 라이브러리가 이미 메모리에 있으면 그 루틴의 주소로 가고(가서 실행), 없으면 디스크에서 읽어옴

  - 운영체제의 도움이 필요
  - eg. printf의 라이브러리 위치를 찾는 코드만 프로그램 안에 집어 넣어두는 것



### 5. Allocation of Physical Memory (물리적 메모리의 할당)

- 메모리는 일반적으로 두 영역으로 나누어 사용
  - **OS 상주영역** 
    - Interrupt Vector와 함께 낮은 주소 영역 사용
  - **사용자 프로세스 영역**
    - 높은 주소 영역 사용

- 사용자 프로세스 영역의 할당 방법 (관리 방법)

  - **Contiguous Allocation(연속 할당)**
    - 각각의 프로세스가 메모리의 연속적인 공간에 적재도록 하는 것
      - Fixed Partition Allocatoin (고정 분할)
      - Variable Partition Allocation (가변 분할)

  - **NonContiguous Allocation(불연속 할당)**
    - 하나의 프로세스가 메모리의 여러 영역에 분산되어 올라가도록 하는 것
      - Paging
      - Segmentation
      - Paged Segmentation

#### 1) Contiguous Allocation(연속 할당)

- Contiguous Allocation

  - 고정 분할 방식 : 프로그램이 들어갈 사용자 영역을 미리 파티션으로 나누어 두는 것.

    - 물리적 메모리를 몇 개의 영구적인 분할로 나눔
    - 분할의 크기가 모두 동일한 방시과 서로 다른 방식이 존재
    - 분할당 하나의 프로그램 적재
    - 융통성이 없음
        - 동시에 메모리에 load되는 프로그램의 수가 고정됨.
        - 최대 수행 가능 프로그램 크기 제한
      - Internal fragmentation (내부 단편화) 발생 (external fragmentation(외부 단편화)도 발생)
  
  
    - 가변 분할 방식: 미리 나눠두지 않는 것.
  
      - 프로그램의 크기를 고려해서 할당
      - 분할의 크기, 개수가 동적으로 변함
      - 기술적 관리 기법 필요
      - external fragmentation(외부 단편화) 발생
  

​	![image-20220516135557982](os_08_Memory Management.assets/image-20220516135557982.png)

- 프로그램 A는 분할 1에 넣으면 됨. 

  프로그램 B는 분할 2에 들어갈 수 없음(분할 2가 크기가 더 작기 때문에) 분할 3에 들어감=> 낭비되는 조각이 발생(외부 조각-프로그램을 올리려고 하는데, 올리려는 프로그램보다 메모리 조각이 작은 경우/내부 조각-프로그램의 크기가 공간보다 작아서 할당 되었지만 사용되지 않아 남는 공간)

- 굳이 분할의 크기를 나눠놓을 필요가 있는가? -> 가변분할 방식: 프로그램이 실행될 때마다 차곡차곡 메모리에 올려놓는 방법 (가변 분할 방식으로 쓰더라도 프로그램 크기가 균일하지 않기 때문에 외부조각은 생길 수 있음 (내부조각은 생기지 않음))
  
- Hole

  - 가용 메모리 공간

  - 다양한 크기의 Hole들이 메모리 여러 곳에 흩어져 있음


- 프로세스가 도착하면 수용가능한 Hole을 할당

  - 운영체제는 다음의 정보를 유지

    - a) 할당 공간
    - b) 가용 공간 (hole)

    ![image-20220516140032943](os_08_Memory Management.assets/image-20220516140032943.png)

    프로그램을 실행할 때 가용곤간 어디에 프로그램을 할당할 것인지? Dynamic Storage-Allocation Problem

- **Dynamic Storage-Allocation Problem**

  : 가변 분할 방식에서 size n인 요청을 만족하는 가장 적절한 hole을 찾는 문제

  - First-Fit
    - Size가 n 이상인 것 중 최초로 찾아지는 Hole에 할당 (제일 처음 발견되는 홀)

  - Best-Fit

    - Size가 n 이상인 가장 작은 Hole을 찾아서 할당 (가장 적합한 Hole에 할당)

    - Hole들의 리스트가 크기순으로 정렬되지 않은 경우 모든 Hole의 리스트를 탐색해야함 (전체 홀을 탐색해야하므로 시간 부담)

    - 많은 수의 아주 작은 Hole들이 생성됨

  - Worst-Fit

    - 가장 큰 Hole에 할당

    - 역시 모든 리스트를 탐색해야함

    - 상대적으로 아주 큰 Hole들이 생성됨
    - 지금 적합한 홀이 있을텐데 제일 큰 홀을 써서 작은 홀로 만들어버리기 때문에 좋은 방법은 아님

  - First-fit과 best-fit이 worst-fit보다 속도와 공간 이용률 측면에서 효과적인 것으로 알려짐(실험적인 결과)



- **Compaction**

  - external fragmentation (외부 단편화) 문제를 해결하는 한 가지 방법

  - 사용 중인 메모리 영역을 한군데로 몰고 Hole들을 다른 한 곳으로 몰아 큰 Block을 만드는 것

  - 매우 비용이 많이 드는 방법 (전체 프로그램의 binding에 관련된 문제여서)

  - 최소한의 메모리 이동으로 Compaction하는 방법 (매우 복잡한 문제)

  - Compaction은 프로세스의 주소가 실행 시간에 동적으로 재배치가 가능한 경우에만 수행될 수 있다
  - Runtime Binding이 지원되야지만 사용할 수 있다.




### Paging

- Paging
  - Process의 virtual memory를 동일한 사이즈의 page 단위로 나눔
  - Virtual memory의 내용이 page 단위로 .noncontiguous하게 저장됨
  - 일부는 backing storage에, 일부는 physical memory에 저장
- Basic Method
  - physical memory를 동일한 크기의 frame으로 나눔
  - logical memory를 동일 크기의 page로 나눔 (frame과 같은 크기)
  - 모든 가용 frame들을 관리
  - page table을 사용하여 logical address를 physical address로 변환
  - External fragmentation(외부 단편화) 발생 안함
  - Internal fragmentation(내부 단편화) 발생 가능

![image-20220516164017911](os_08_Memory Management.assets/image-20220516164017911.png)

=> 프로그램을 구성하는 논리적 메모리를 동일한 크기의 Page로 잘라서 각각의 페이지별로 물리적 메모리 어디든 비어있는 위치에 올라갈 수 있게 해줌. 

각각의 논리적 메모리에 있는 Page들이 물리적 메모리 어디에 올라가 있는가를 알려줌

Page Table : Page 갯수만큼 엔트리가 존재함

인덱스를 통해 곧바로 접근 가능한 자료구조.



### Adress Translation Scheme

- CPU는 다음 두 가지로 구성된 virtual address를 사용
  - Page number (p)
    - page table의 index로 사용
    - 해당 index에는 그 페이지의 물리적 메모리 상의 base address가 저장됨



### Address Translation Architecture

![image-20220516195836189](os_08_Memory Management.assets/image-20220516195836189.png)

내부에서 상대적 위치는 똑같기 때문에 페이지 내의 offset은 주소 변환에 영향이 없고, 페이지 번호만 바뀜

4kb, 프로그램 하나의 주소 공간이 백만개로 짤림- 많은 용량이 필요함 -> 레지스터에 넣을 수도 없고 하드디스크에 저장할 수도 없음. -> 메모리에 집어넣게 됨

메모리에 접근하기 위해 주소변환, 주소변환 후 데이터를 실제로 접근하기 위해



### Implementation of Page Table

- Page Table은 Main Memory에 상주
- Page-Table Base Register(PTBR)가 Page Table을 가리킴
- Page-Table Length Register(PTLR)가 테이블 크기를 보관
- 모든 메모리 접근 연산에는 2번의 Memory Access 필요
- Page Table 접근 1번, Data/Instruction 접근 1번
- 속도 향상을 위해 Associative Register 혹은 Translation Look-aside Buffer(TLB)(주소변환 계층) 라 불리는 고속의 Lookup Hardware Cache 사용 (별도의 하드웨어(일종의 캐쉬-주소 변환을 위한 캐쉬메모리)를 사용함)



### Paging Hardware with TLB

![image-20220516200415447](os_08_Memory Management.assets/image-20220516200415447.png)

page table로 가기 전 먼저 TLB를 체크해서 주소변환이 가능한지 확인해서 접근 한 번을 줄임

프로세스마다 TLB의 정보도 다름. 



### Effective Access Time

- Associative register lookup time = ￡ (TLB를 접근하는 시간)
- memory cycle time = 1 
- Hit ratio = ∂
  - associative register에서 찾아지는 비율
- Effective Access Time (EAT)
  - EAT = (1+￡)∂  \<hit> + (2+￡)(1-∂)\<miss> = 2+￡-∂



### Two-Level Page Table (2단계 페이지 테이블)

속도는 줄어들지 않으나 page table 공간이 줄어드는 것이 목적임.

- 현대의 컴퓨터는 Address Space가 매우 큰 프로그램 지원
  - 32 bit Address 사용시 : 2^32 (4GB)의 주소 공간 (2^10 = K, 2^20=M)
    - Page Size가 4K시 1M개의 Page Table Entry가 필요 (4gb 페이지를 4kb로 쪼개려면 1M개)
    - 각 Page Entry가 4B시 프로세스당 4M의 Page Table 필요
    - 그러나, 대부분의 프로그램은 4G의 주소 공간 중 지극히 일부분만 사용하므로 Page Table 공간이 심하게 낭비됨 -> 2단계 페이지 사용 이유


- Page Table 자체를 Page로 구성
- 사용되지 않는 주소 공간에 대한 Outer Page Table의 엔트리 값은 NULL (대응하는 inner page Table이 없음)

![image-20220516201247980](os_08_Memory Management.assets/image-20220516201247980.png)

- logical address (on 32-bit machine with 4K page size)의 구성
  - 20 bit의 page number
  - 12 bit의 page offset 

- page table 자체가 page로 구성되기 때문에 page number는 다음과 같이 나뉜다(각 page table entry가 4B)

  - 10-bit의 page number
  - 10-bit의 page offset

- 따라서, logical address는 다음과 같다

  ![image-20220516202014473](os_08_Memory Management.assets/image-20220516202014473.png)

- P1은 outer page table의 index이고

- P2는 outer page table의 page에서의 변위(displacement)



### Address-Translation Scheme

- 2단계 페이징에서의 Address-translation scheme

  ![image-20220516202124401](os_08_Memory Management.assets/image-20220516202124401.png)



### Multilevel Paging

- Address Space가 더 커지면 다단계 페이지 테이블 필요

- 각 단계의 페이지 테이블이 메모리에 존재하므로 Logical Address의 Physical Address 변환에 더 많은 메모리 접근 필요

- TLB를 통해 메모리 접근 시간을 줄일 수 있음

- 4단계 페이지 테이블을 사용하는 경우

  - 메모리 접근 시간이 100ns, TLB 접근시간이 20ns이고 

  - TLB hit ratio가 98%인 경우

    Effective Memory Access Time = 0.98 x 120 + 0.02 x 520 

    ​														= 128 nanoseconds. 

    결과적으로 주소변환을 위해 28ns만 소요

- TLB 덕분에 다단계 Page Table이 크게 오버헤드가 되지 않는다.



### Valid(v) / Invalid (i) Bit in a page Table

페이지 갯수만큼 엔트리가 존재하고 페이지 프레임 주소 변환 정보가 들어 있음. 추가로 bit가 들어 있음.

사용되지 않는 영역도 엔트리가 만들어져야 함 (6번, 7번) - 사용되지 않기 때문에 invalid로 표시

![image-20220516203559085](os_08_Memory Management.assets/image-20220516203559085.png)



### Memory Protection

- Page Table의 각 Entry 마다 아래의 bit를 둔다.

  - Protection bit
    - Page에 대한 접근 권한(read / write / read-only)
      - 접근 권한 제어는 어떤 연산에 대한 권한이 있는가를 나타냄 (다른 프로세스가 이 페이지 접근하는 지에 대한 판단이 아님)

  - Valid-Invalid bit
    - Valid는 해당 주소의 frame에 그 프로세스를 구성하는 유요한 내용이 있음을 뜻함 (접근 허용)
    - Invalid는 해당 주소의 frame에 유효한 내용이 없음을 뜻함 (접근 불허)
      - 프로세스가 그 주소 부분을 사용하지 않는 경우
      - 해당 페이지가 메모리에 올라와 있지 않고 Swap Area에 있는 경우
        

### Inverted Page Table (역방향 페이지 테이블)

- Page Table이 매우 큰 이유

  - 모든 Process 별로 그 Logical Address에 대응하는 모든 Page에 대해 Page Table Entry가 존재
  - 대응하는 Page가 메모리에 있든 아니든 간에 Page Table에는 Entry로 존재

- Inverted Page Table

  - Page Frame 하나당 Page Table에 하나의 Entry를 둔 것 (System-Wide)

  - 각 Page Table Entry는 각각의 물리적 메모리의 Page Frame이 담고 있는 내용 표시 (Process-id, Process의 Logical Address) 페이지 프레임 갯수만큼 엔트리가 존재함

  - 페이지 테이블을 위한 공간을 줄일 수 있음. 

  - 단점

    - 테이블 전체를 탐색해야 함
    - 주소 변환은 physical address를 보고 logical address로 변환하는 것인데 이것은 반대임.

  - 조치

    -  Associative Register 사용 (expensive 비쌈)

    ![image-20220516204210805](os_08_Memory Management.assets/image-20220516204210805.png)



### Shared Page

- Shared 가능한 코드는 물리적 메모리에 하나만 올리는 방식
- 여러 프로세스가 공유 가능한 코드를 같은 물리적 메모리 프레임으로 mapping 해주는 기법
- 반드시 read-only로 셋팅해야 함 / 동일한 logical address에 위치해야 한다
- Shared code
  - Re-entrant Code (=Pure code) 재진입 가능 코드
  - read-only로 하여 프로세스 간에 하나의 code만 메모리에 올림 (eg. text editors, compliers, window systems)
  - Shared Code는 모든 프로세스의 Logical Address Space에서 동일한 위치에 있어야 함

- Private Code and Data

  - 각 프로세스들은 독자적으로 메모리에 올림
  - Private Data는 Logical Address Space의 아무 곳에 와도 무방

  ![image-20220516204732296](os_08_Memory Management.assets/image-20220516204732296.png)



### Segmentaion

- 프로그램은 의미 단위인 여러 개의 segment로 구성

  - 작게는 프로그램을 구성하는 함수 하나하나를 세그먼트로 정의
  - 크게는 프로그램 전체를 하나의 세그먼트로 정의 가능
  - 일반적으로는 code, data, stack 부분이 하나씩의 세그먼트로 정의됨

- Segment는 다음과 같은 logical unit 들임

  main (), function, global variables, stack, symbol table, arrays



### Segmentaion Architecture

- Logical Address는 다음의 두 가지로 구성

  <segment-number, offset> 세그먼트 번호와 얼마나 떨어져 있는지 offset

- Segment table

  - each table entry has:
    - base-starting physical address of the segment 시작 위치
    - limit-length of the segment 길이 (프로그램이 사용하는 segment의 개수(엔트리 수))

- Segment-table base register (STBR)

  - 물리적 메모리에서의 segment table의 위치

- Segment-table length register (STLR)

  - 프로그램이 사용하는 segment의 수

    segment number s is legal if s < STLR



### Segmentation Hardware

세그먼트 번호와 길이 체크

​	세그먼트의 시작 위치 체크

​	세그먼트 길이보다 요구가 크지 않은지 체크

![image-20220516205648641](os_08_Memory Management.assets/image-20220516205648641.png)



### Segmentation Architecture (Cont.)

- Protection

  - 각 세그먼트 별로 Protection bit가 있음
  - Each Entry:
    - Valid bit = 0 => illegal segment
    - Read / Write / Executrion 권한 bit

- Sharing

  - Shared Segment
  - Same Segment Number
    - segment는 의미 단위이기 때문에 공유(sharing)와 보안(protection)에 있어 paging 보다 훨씬 효과적이다

- Allocation

  - First Fit / Best Fit
  - external fragmentation (외부 단편화) 발생
    - segment의 길이가 동일하지 않으므로 가변분할 방식에서와 동일한 문제점들이 발생

  ![image-20220516210315114](os_08_Memory Management.assets/image-20220516210315114.png)

페이징은 개수가 많지만 세그먼트는 개수가 몇 개 안됨. 

테이블을 위한 메모리 낭비가 심한 것은 페이징, 세그먼트가 낭비가 더 적다



### Sharing of Segments

서로 다른 프로세스가 공유하는 것을 보여주는 예제

0번 세그먼트는 코드를 담고 있음. 같은 역할을 하는 코드이기 때문에 sharing함

두 개의 세그먼트는 같은 위치인 물리적 메모리에 위치하게 됨.

![image-20220516210505476](os_08_Memory Management.assets/image-20220516210505476.png)



### Segmentation with Paging (Paged Segmentation)

Paging 기법과 Segmetation 기법을 혼합하는 기법

- 세그먼트 하나를 여러개의 페이지로 구성하는 기법

- pure segmentation과의 차이점
  - segment-table entry가 segment의 base address를 가지고 있는 것이 아니라 segment를 구성하는 page table의 base address를 가지고 있음
- 세그먼트에 대한 주소 변환 -> s번째 엔트리에 가면 주소 변환 방법이 있음(시작 위치) -> 페이지 개수의 배수로 구성될 것.
- allocation 문제가 발생하지 않음. 의미나 보안 같은 경우는 세그먼트 테이블 레벨에서 시행 => 두 가지의 장점을 모두 누릴 수 있음.
- 세그먼트 당 페이지가 존재할 것. 세그먼트의 길이가 얼마인지를 보면 됨. 세그먼트길이와 요청한 offset을 비교해서 그 이내일 경우에만 주소 변환을 해줌. d(세그먼트 offset) / (p, d) = (페이지번호, 페이지 offset)
- 프레임번호, 오프셋 = 물리적 메모리 주소

![image-20220516210828248](os_08_Memory Management.assets/image-20220516210828248.png)



=> 운영체제의 역할은 없고 주소 변환은 하드웨어가 함

