# Chapter 09. Virtual Memory

### Demand Paging

- 실제로 필요할 때 page를 메모리에 올리는 것
  - I/O 양의 감소
  - Memory 사용량 감소
  - 빠른 응답 시간 (한정된 공간에 더 의미 있는 정보를 올리기 위해 사용)
  - 더 많은 사용자 수용
- Valid / Invalid bit의 사용 (페이징 기법)
  - Invalid의 의미
    - 사용되지 않는 주소 영역인 경우
    - 페이지가 물리적 메모리에 없는 경우 
  - 처음에는 모든 page entry가 invalid로 초기화
  - Address translation 시에 invalid bit이 set되어 있으면 => "page fault" (요청한 페이지에 메모리가 없다)

#### Memory에 없는 Page의 Page Table

- ![스크린샷 2022-05-22 오전 12.15.35](/Users/juhyeyoon/Library/Application Support/typora-user-images/스크린샷 2022-05-22 오전 12.15.35.png)



### Page Fault

- Invalid page를 접근하면 MMU가 trap을 발생시킴 (page fault trap)
- Kernel mode로 들어가서 page fault handler가 invoke됨
- 다음과 같은 순서로 page fault를 처리한다
  1. Invalid reference? (eg. Bad address, protection violation) => abort process.
  2. Get an empty page Frame. (없으면 뺏어온다: replace)
  3. 해당 페이지를 disk에서 memory로 읽어온다
     1. Disk I/O가 끝나기까지 이 프로세스는 CPU를 preempt당함 (block) (가지고 있어봐야 낭비가 되므로 뺏어서 블록상태로 만들어주고 넘겨줌)
     2. Disk read가 끝나면 page tables entry 기록, valid/invalid bit="valid"
     3. Ready queue에 process를 insert -> dispatch later
  4. 이 프로세스가 CPU를 잡고 다시 running
  5. 아까 중단되었던 instruction을 재개
- ![스크린샷 2022-05-22 오전 12.25.20](/Users/juhyeyoon/Library/Application Support/typora-user-images/스크린샷 2022-05-22 오전 12.25.20.png)



#### Performance of Demand Paging

- Page Fault Rate 0 <= p <= 1.0

  - if p=0 no page faults
  - if p=1, every reference is a fault

  page fault가 일어나면 엄청난 시간(overhead)이 소요됨

- Effective Access Time

  = (1-p)(page fault가 안 나는 비율) x memory access (메모리 접근 시간)

  +p (OS & HW page fault overhead + [swap page out if needed(메모리에 필요한 공간 마련을 위해 페이지 쫓아냄)] + swap page in + OS & HW restart overhead)



### Free Frame이 없는 경우

- Page replacement

  - 페이지를 메모리에서 쫓아내고 어떤 페이지를 새로 메모리에 올려놓을 것인지 결정하는 것
  - 어떤 frame을 빼앗아 올지 결정해야 함
  - 곧바로 사용되지 않을 page를 쫓아내는 것이 좋음
  - 동일한 페이지가 여러 번 메모리에서 쫓겨났다가 다시 들어올 수 있음

- Replacement Algorithm

  - Page-fault rate을 **최소화**하는 것이 목표 (0에 가깝도록)

  - 알고리즘의 평가

    - 주어진 page reference string에 대해 page fault를 얼마나 내는지 조사

  - reference string의 예

    1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5

    ![스크린샷 2022-05-22 오전 12.38.19](/Users/juhyeyoon/Library/Application Support/typora-user-images/스크린샷 2022-05-22 오전 12.38.19.png)



### Optimal Algorithm

- Page fault를 가장 적게 하는 좋은 알고리즘
- 미래의 페이지를 모두 안다고 가정함

- MIN (OPT): 가장 먼 미래에 참조되는 page를 replace
- 4 frames example
- ![스크린샷 2022-05-22 오전 12.41.47](/Users/juhyeyoon/Library/Application Support/typora-user-images/스크린샷 2022-05-22 오전 12.41.47.png)
  - 빨간색은 페이지 폴트가 난 것을 표시
- 미래의 참조를 어떻게 아는가?
  - Offline algorithm
- 다른 알고리즘의 성능에 대한 upper bound 제공
  - 아무리 좋은 알고리즘을 만들어도 이보다 좋은 알고리즘을 만들 수 없음
  - Belady's optimal algorithm, MIN, OPT 등으로 불림



### FIFO (First In First Out) Algorithm

- FIFO: 먼저 들어온 것을 먼저 내쫓음
- 미래의 페이지를 모르는 알고리즘
- ![스크린샷 2022-05-22 오전 12.47.02](/Users/juhyeyoon/Library/Application Support/typora-user-images/스크린샷 2022-05-22 오전 12.47.02.png)
  - 메모리를 크기를 늘려주면 보통 성능이 좋아져야 하는데, 오히려 성능이 나빠짐. => FIFO Anomaly
- FIFO Anomaly (Belady's Anomaly)
  - More frames => less page faults



### LRU (Least Recently Used) Algorithm

- LRU: 가장 오래 전에 참조된 것을 지움

- 가장 덜 최근에 사용된 것을 쫓아내는 알고리즘
- ![스크린샷 2022-05-22 오전 12.49.34](/Users/juhyeyoon/Library/Application Support/typora-user-images/스크린샷 2022-05-22 오전 12.49.34.png)
  - 가장 오래된 3번을 쫓아내고 그 자리에 5번을 집어 넣음
- 미래를 모르면 과거가 중요함 
- 최근에 참조된 페이지가 다시 참조될 가능성이 높음 -> 비교적 page faults를 줄일 수 있음



### LFU (Least Frequently Used) Algorithm

- LFU: 참조 횟수(reference count)가 가장 적은 페이지를 지움
  - 최저 참조 횟수인 page가 여럿 있는 경우
    - LFU 알고리즘 자체에서는 여러 page 중 임의로 선정한다
    - 성능 향상을 위해 가장 오래 전에 참조된 page를 지우게 구현할 수도 있다
  - 장단점
    - LRU처럼 직전 참조 시점만 보는 것이 아니라 장기적인 시간 규모를 보기 때문에 page의 인기도를 좀 더 정확히 반영할 수 있음
    - 참조 시점의 최근성을 반영하지 못함
    - LRU보다 구현이 복잡함



#### LRU와 LFU 알고리즘 예제

![스크린샷 2022-05-22 오전 1.00.33](/Users/juhyeyoon/Desktop/스크린샷 2022-05-22 오전 1.00.33.png)



#### LRU와 LFU 알고리즘의 구현

- LRU linked list n개의 페이지를 비교해보고 오래된 페이지를 지움
- LFU 한 줄로 줄세우기 불가능. 참조 횟수가 늘어났다고 해서 내려갈 수 있는게 아님. 점점 내려가야 함. 
- ![스크린샷 2022-05-22 오전 1.06.51](/Users/juhyeyoon/Desktop/스크린샷 2022-05-22 오전 1.06.51.png)



### 다양한 캐슁 환경

- 캐슁 기법

  - 한정된 빠른 공간(=캐쉬)에 요청된 데이터를 저장해 두었다가 후속 요청시 캐쉬로부터 직접 서비스하는 방식
  - paging system 외에도 cache memory, buffer caching, Web caching 등 다양한 분야에서 사용
- 캐쉬 운영의 시간 제약

  - 교체 알고리즘에서 삭제할 항목을 결정하는 일에 지나치게 많은 시간이 걸리는 경우 실제 시스템에서 사용할 수 없음
  - Buffer caching이나 Web caching의 경우
    - O(1)에서 O(log n) 정도까지 허용
  - Paging system인 경우
    - Page fault인 경우에만 OS가 관여함
    - 페이지가 이미 메모리에 존재하는 경우 참조시각 등의 정보를 OS가 알 수 없음
    - O(1)인 LRU의 list조작조차 불가능




#### Paging System에서 LRU, LFU 가능한가?

운영체제가 과연 가장 오래된 참조 페이지를 알 수 있는가?

운영체제가 가장 참조횟수가 적은 페이지를 알 수 있는가? -> 알 수 없음. 페이지폴트가 나면 운영체제가 메모리로 올라오는 시간을 알 수 있으나, 올라오지 않으면 모름. 

LRU, LFU 알고리즘은 페이징 시스템에서 사용 불가능함.

-> Clock Algorithm을 사용함

![스크린샷 2022-05-23 오전 1.41.05](/Users/juhyeyoon/Desktop/스크린샷 2022-05-23 오전 1.41.05.png)



### Clock Algorithm

- Clock Algorithm

  - LRU의 근사(approximation) 알고리즘
  - 여러 명칭으로 불림
    - Second chance algorithm
    - NUR (Not Used Recently) 또는 NRU(Not Recently Used) - 최종에 사용되지 않은 페이지를 쫓아냄
  - Reference bit을 사용해서 교체 대상 페이지 선정(circular list)
  - reference bit가 0인 것을 찾을 때까지 포인터를 하나씩 앞으로 이동
  - 포인터 이동하는 중에 reference bit 1은 모두 0으로 바꿈
  - Reference bit이 0인 것을 찾으면 그 페이지를 교체
  - 한 바퀴 되돌아와서도(=second chance) 0이면 그때에는 replace 당함
  - 자주 사용되는 페이지라면 second chance가 올 때 1

- Clock algorithm의 개선

  - reference bit과 modified bit (dirty bit)을 함께 사용
  - Reference bit = 1: 최근에 참조된 페이지 (운영체제가 아닌 하드웨어가 해줌)
  - Modified bit = 1: 최근에 변경된 페이지(I/O를 동반하는 페이지) - 수정된 내용을 반영한 뒤에 지워야 함 (더 일이 많아서 1인 것보다 0을 더 우선적으로 쫓아냄)

  ![스크린샷 2022-05-23 오전 1.48.55](/Users/juhyeyoon/Desktop/스크린샷 2022-05-23 오전 1.48.55.png)

  - 페이지 0으로 만들어두고 한바퀴 돌아왔을 때 1이 아닌 0 그대로면 최근에 참조가 안됐다는 것. 



### Page Frame의 Allocation

- Allocation problem: 각 process에 얼마만큼의 page frame을 할당할 것인가?
- Allocation의 필요성
  - 메모리 참조 명령어 수행시 명령어, 데이터 등 여러 페이지 동시 참조
    - 명령어 수행을 위해 최소한 할당되어야 하는 frame의 수가 있음
  - Loop를 구성하는 page들은 한꺼번에 allocate되는 것이 유리함
    - 최소한의 allocation이 없으면 매 loop마다 page fault
- Allocation Scheme
  - Equal allocation: 모든 프로세스에 똑 같은 갯수 할당
  - Proportional allocation: 프로세스 크기에 비례하여 할당
  - Priority allocation: 프로세스의 priority에 따라 다르게 할당



### Global vs. Local Replacement

- Global replacement
  - Replace 시 다른 process에 할당된 frame을 빼앗아 올 수 있다
  - Process별 할당량을 조절하는 또 다른 방법임
  - FIFO, LRU, LFU 등의 알고리즘을 global replacement로 사용시에 해당
  - Working set, PFF. 알고리즘 사용
- Local replacement
  - 자신에게 할당된 frame 내에서만 replacement
  - FIFO, LRU, LFU 등의 알고리즘을 process 별로 운영시



### Thrashing

- Thrashing
  - 프로세스의 원활한 수행에 필요한 최소한의 page. Frame 수를 할당받지 못한 경우 발생 (메모리 할당량이 너무 감소되면...)
  - Page fault rate이 매우 높아짐
  - CPU utilization이 낮아짐
  - OS는 MPD(Multiprogramming degree)를 높여야 한다고 판단
  - 또 다른 프로세스가 시스템에 추가됨 (higher MPD)
  - 프로세스 당 할당된 frame의 수가 더욱 감소
  - 프로세스는 page의 swap in / swap out으로 매우 바쁨
  - 대부분의 시간에 CPU는 한가함
  - low throughput
    - 무조건 page fault가 발생하고 CPU는 할일이 없어져서 비효율적이 됨



#### Thrashing Diagram

![스크린샷 2022-05-23 오전 1.59.13](/Users/juhyeyoon/Desktop/스크린샷 2022-05-23 오전 1.59.13.png)

- 프로그램이 어느정도는 메모리페이지 확보를 할 수 있게 해줘야 함



### Working-Set Model

- Locality of reference
  - 프로세스는 특정 시간 동안 일정 장소만을 집중적으로 참조한다
  - 집중적으로 참조되는 해당 page들의 집합을 locality set이라 함
- Working-set Model
  - Locality에 기반하여 프로세스가 일정 시간동안 원활하게 수행되기 위해 한꺼번에 메모리에 올라와 있어야 하는 page들의 집합을 Working Set이라 정의함
  - Working Set 모델에서는 process의 working set전체가 메모리에 올라와 있어야 수행되고 그렇지 않을 경우 모든 frame을 반납한 후 swap out(suspend)
  - Thrashing을 방지함
  - Multiprogramming degree를 결정함



### Working-Set Algorithm

- Working Set window를 통해 알아냄

- Window size가 delta(d)인 경우

  - 시각 ti에서의 working set WS (ti)
    - Tim interval[ti-d, ti] 사이에 참조된 서로 다른 페이지들의 집합
  - Working set에 속한 page는 메모리에 유지, 속하지 않은 것은 버림 (즉, 참조된 후 d시간 동안 해당 page를 메모리에 유지한 후 버림)

  ![스크린샷 2022-05-23 오전 2.07.00](/Users/juhyeyoon/Desktop/스크린샷 2022-05-23 오전 2.07.00.png)

- Working-Set Algorithm

  - Process들의 working set size의 합이 page frame의 수보다 큰 경우
    - 일부 process를 swap out시켜 남은 process의 working set을 우선적으로 충족시켜 준다 (MPD를 줄임)
  - Working set을 다 할당하고도 page frame이 남는 경우
    - Swap out되었던 프로세스에게 working set을 할당 (MPD를 키움)

- Window size delta

  - Working set을 제대로 탐지하기 위해서는 window size를 잘 결정해야 함
  - delta 값이 너무 작으면 locality set을 모두 수용하지 못할 우려
  - d 값이 크면 여러 규모의 locality set 수용
  - d 값이 무한대면 전체 프로그램을 구성하는 page를 working set으로 간주



### PFF (Page-Fault Frequency) Scheme

- Page-fault rate의 상한값과 하한값을 둔다
  - Page fault rate이 상한값을 넘으면 frame을 더 할당한다
  - Page fault rate이 하한값 이하이면 할당 frame 수를 줄인다
- 빈 frame이 없으면 일부 프로세스를 swap out
- ![스크린샷 2022-05-23 오전 2.12.43](/Users/juhyeyoon/Desktop/스크린샷 2022-05-23 오전 2.12.43.png)



### Page Size의 결정

- Page size를 감소시키면
  - 페이지 수 증가
  - 페이지 테이블 크기 증가
  - Internal fragmentation 감소
  - Disk transfer의 효율성 감소
    - Seek/rotation vs. transfer
  - 필요한 정보만 메모리에 올라와 메모리 이용이 효율적
    - Locality의 활용 측면에서는 좋지 않음
- Trend
  - Larger page size



# Chapter 10. File Systems

### File and File System

- file
  - A named collection of related Information
  - 일반적으로 비휘발성의 보조기억장치에 저장
  - 운영체제는 다양한 저장 장치를 file이라는 동일한 논리적 단위로 볼 수 있게 해 줌
  - Operation
    - Create, read, write, reposition(lseek), delete, open, close 등
- file attributes(혹은 파일의 metadata)
  - 파일 자체의 내용이 아니라 파일을 관리하기 위한 각종 정보들
    - 파일 이름, 유형, 저장된 위치, 파일 사이즈
    - 접근 권한 (읽기/쓰기/실행), 시간(생성/변경/사용). 소유자 등
- File system
  - 운영체제에서 파일을 관리하는 부분
  - 파일 및 파일의 메타데이터, 디렉토리 정보 등을 관리
  - 파일의 저장 방법 결정
  - 파일 보호 등



### Directory and Logical Disk

- Directory
  - 파일의 메타데이터 중 일부를 보관하고 있는 일종의 특별한 파일
  - 그 디렉토리에 속한 파일 이름 및 파일 attribute들
  - operation
    - search for a file, create a file, delete a file
    - list a directory, rename a file, traverse the file system
- Partition (=Logical Disk)
  - 하나의 (물리적) 디스크 안에 여러 파티션을 두는게 일반적
  - 여러 개의 물리적인 디스크를 하나의 파티션으로 구성하기도 함
  - (물리적) 디스크를 파티션으로 구성한 뒤 각각의 파티션에 file system을 깔거나 swapping등 다른 용도로 사용할 수 있음



#### open()

![스크린샷 2022-05-23 오전 2.21.34](/Users/juhyeyoon/Desktop/스크린샷 2022-05-23 오전 2.21.34.png)

- Open("/a/b/c")

  - 디스크로부터 파일 c의 메타데이터를 메모리로 가지고 옴
  - 이를 위하여 directory path를 search
    - 루트 디렉토리 "/"를 open 하고 그 안에서 파일 "a"의 위치 획득
    - 파일 "a"를 open한 후 read하여 그 안에서 파일 "b"의 위치 획득
    - 파일 "b"를 open한 후 read하여 그 안에서 파일 "c"의 위치 획득
    - 파일 "c"를 open한다
  - Directory path의 search에 너무 많은 시간 소요
    - Open을 read/write와 별도로 두는 이유임
    - 한번 open한 파일은 read/write시 directory search 불필요
  - Open file table
    - 현재 open된 파일들의 메타데이터 보관소(in memory)
    - 디스크의 메타데이터보다 몇 가지 정보가 추가
      - Open한 프로세스의 수
      - File offset: 파일 어느 위치 접근 중인지 표시(별도 테이블 필요)
  - File descriptor (file handel, file control block)
    - Open file table에 대한 위치 정보(프로세스 별)

  ![스크린샷 2022-05-23 오전 2.27.25](/Users/juhyeyoon/Desktop/스크린샷 2022-05-23 오전 2.27.25.png)



### File Protection

- 각 파일에 대해 누구에게 어떤 유형의 접근 (read/write/execution)을 허락할 것인가?
- Acess Control 방법
  - Access control Matrix
  - ![스크린샷 2022-05-23 오전 2.31.45](/Users/juhyeyoon/Desktop/스크린샷 2022-05-23 오전 2.31.45.png)
    - Acess control list: 파일 별로 누구에게 어떤 접근 권한이 있는지 표시
    - Capability: 사용자별로 자신이 접근 권한을 가진 파일 및 해당 권한 표시
  - Grouping
    - 전체 user를 owner, group, public의 세 그룹으로 구분
    - 각 파일에 대해 세 그룹의 접근 권한(rws)을 3비트씩으로 표시
    - 예) UNIX
  - Password
    - 파일마다 password를 두는 방법(디렉토리 파일에 두는 방법도 가능)
    - 모든 접근 권한에 대해 하나의 passwod: all-or-nothing
    - 접근 권한별 password: 암기 문제, 관리 문제



#### File System의 Mounting

![스크린샷 2022-05-23 오전 2.33.16](/Users/juhyeyoon/Desktop/스크린샷 2022-05-23 오전 2.33.16.png)

![스크린샷 2022-05-23 오전 2.33.44](/Users/juhyeyoon/Desktop/스크린샷 2022-05-23 오전 2.33.44.png)



### Access Methods

- 시스템이 제공하는 파일 정보의 접근 방식
  - 순차 접근 (sequential access)
    - 카세트 테이프를 사용하는 방식처럼 접근
    - 읽거나 쓰면 offset은 자동적으로 증가
  - 직접 접근 (direct access, random access)
    - LP 레코드 판과 같이 접근하도록 함
    - 파일을 구성하는 레코드를 임의의 순서로 접근할 수 있음



# Chapter 11. File Systems Implementation



### Allocation of File Data in Disk

- 디스크에 파일을 저장할 때의 방법

- Contiguous Allocation
- Linked Allocation
- Indexed Allocation



### Contiguous Allocation

![image-20220523205627293](C:/Users/YoonJuhye/TIL/cs/os/os_11_File Systems Implementation.assets/image-20220523205627293.png)

- 연속적인 메모리에 올리는 방법
- 단점
  - external fragmentation (외부 단편화 발생)
  - File grow가 어려움 (수정 등으로 인해 파일의 크기가 변하는 것)
    - file 생성시 얼만큼의 hole를 배당할 것인가?
    - grow 가능 vs 낭비 (Internal fragmentation)
- 장점
  - Fast I/O
    - 한 번의 seek/rotation으로 많은 바이트 transfer 가능
    - Realtime file 용으로, 또는 이미 run 중이던 process의 swapping 용
  - Direct access (=random access) 가능



### Linked Allocation

![image-20220523210111543](C:/Users/YoonJuhye/TIL/cs/os/os_11_File Systems Implementation.assets/image-20220523210111543.png)

- 각 블록이 다음 블록의 주소를 가지고 있다. 디렉토리는 파일의 시작과 끝 위치만 가지고 있다.
- 장점
  - external fragmentation (외부 단편화) 발생 안 함
- 단점
  - No random access
  - Reliability 문제
    - 한 sector가 고장나 pointer가 유실되면 많은 부분을 잃음
  - Pointer를 위한 공간이 block의 일부가 되어 공간 효율성을 떨어뜨림
    - 보통 512바이트(배수)로 저장됨.
    - 512 bytes/sector, 4 bytes/pointer (사실상 데이터를 저장할 수 있는 위치는 512-4 = 508 bytes)
    - 만약 512 bytes file을 저장하려면 2 sector에 저장해야 함
- 변형
  - File Allocation Table(FAT) 파일 시스템
    - 포인터를 별도의 위치에 보관하여 reliability와 공간효율성 문제 해결



### Indexed Allocation

![image-20220523210333636](C:/Users/YoonJuhye/TIL/cs/os/os_11_File Systems Implementation.assets/image-20220523210333636.png)

- Index block을 두어 파일의 내용을 가지고 있는 주소를 저장해둔다.
- 그림의 경우 총 5개의 블록으로 이루어져 있다.
- 장점
  - 외부 단편화가 발생하지 않는다.
  - Direct access 가능
- 단점
  - Small file의 경우 공간 낭비 (실제로 많은 file이 small)
    - 저장하는데 두 섹터나 필요함
  - Too large file의 경우 하나의 block으로는 index를 저장하기에 부족
    - 해결 방안
      1. linked scheme : index block의 실제 위치를 적다가 실제 파일의 위치가 아니라 또다른 블록의 인덱스를 표시
      2. multi-level index (2단계 페이지를 사용하듯이  함)



### UNIX 파일시스템의 구조

![image-20220523211538923](C:/Users/YoonJuhye/TIL/cs/os/os_11_File Systems Implementation.assets/image-20220523211538923.png)

- 유닉스 파일 시스템의 중요 개념
  - Boot block
    - 부팅에 필요한 정보 (bootstrap loader)
  - Super block
    - 파일 시스템에 관한 총체적인 정보를 담고 있다.
  - Inode
    - 파일 이름을 제외한 파일의 모든 meta data를 저장
  - Data block
    - 파일의 실제 내용을 보관





### FAT File system

![image-20220523212256984](C:/Users/YoonJuhye/TIL/cs/os/os_11_File Systems Implementation.assets/image-20220523212256984.png)



### Free-Space Management

- Bit map or bit vector

  ![image-20220523212426635](C:/Users/YoonJuhye/TIL/cs/os/os_11_File Systems Implementation.assets/image-20220523212426635.png)

  - bit map은 부가적인 공간을 필요로 함

  - 연속적인 n개의 free block을 찾는데 효과적이다.

- Linked List

  - 모든 free block들을 링크로 연결(free list)

  - 연속적인 가용공간을 찾는 것은 쉽지 않다.

  - 공간의 낭비가 없다.

- Grouping

  - linked list 방법의 변형

  - 첫 번째 free block이 n개의 pointer를 가짐

    - n-1 pointer는 free data block을 가리킴
    - 마지막 pointer가 가리키는 block은 또 다시 n pointer를 가짐

    ![image-20220523212628293](C:/Users/YoonJuhye/TIL/cs/os/os_11_File Systems Implementation.assets/image-20220523212628293.png)

- Counting

  - 프로그램들이 종종 여러 개의 연속적인 block을 할당하고 반납한다는 성질에 착안

  - (first free block, # of contiguous free blocks)를 유지



### Linked Free Space List on Disk

![image-20220523212701144](C:/Users/YoonJuhye/TIL/cs/os/os_11_File Systems Implementation.assets/image-20220523212701144.png)

### Directory Implementation

- Linear list

  - <file name, file metadata> 의 list

  - 구현이 간단

  - 디렉토리 내에 파일이 있는지 찾기 위해서는 linear search가 필요 ( time consuming)



- Hash Table

  - linear list + hashing

  - Hash table은 file name을 이 파일의 linear list의 위치로 바꾸어줌

  - search time을 없앰

  - Collision 발생 가능

  ![image-20220523212833180](C:/Users/YoonJuhye/TIL/cs/os/os_11_File Systems Implementation.assets/image-20220523212833180.png)



- File metadata의 보관 위치

  - 디렉토리 내에 직접 보관

  - 디렉토리에는 포인터를 두고 다른 곳에 보관
    - Inode, FAT 등

- Long file name의 지원

  - <File name, file metadata>의 list 에서 각 entry는 일반적으로 고정 크기

  - file name이 고정 크기보다 길어지는 경우 entry의 마지막 부분에 이름의 뒷부분이 위치한 곳의 포인터를 두는 방법

  - 이름 나머지 부분은 동일한 directory file의 일부에 존재

  ![image-20220523212943729](C:/Users/YoonJuhye/TIL/cs/os/os_11_File Systems Implementation.assets/image-20220523212943729.png)



### VFS & NFS

![image-20220523213017963](C:/Users/YoonJuhye/TIL/cs/os/os_11_File Systems Implementation.assets/image-20220523213017963.png)

- Virtual File System (VFS)
  - 서로 다른 다양한 file system에 대해 동일한 시스템 콜 인터페이스(API)를 통해 접근할 수 있게 해주는 OS layer
- Network File System (NFS)

  - 분산 시스템에서는 네트워크를 통해 파일이 공유될 수 있음
  - NFS는 분산 환경에서의 대표적인 파일 공유 방법임



### Page cache and Buffer Cache

- Page Cache
  - Virtual memory의 paging system에서 사용하는 page frame을 caching의 관점에서 설명하는 용어
  - Memory-mapped I/O를 쓰는 경우 file의 I/O에서도 page cache 사용
- Memory Mapped I/O
  - File의 일부를 virtual memory에 mapping 시킴
  - 매핑시킨 영역에 대한 메모리 접근 연산은 파일의 입출력을 수행하게 함
- Buffer Cache
  - 파일 시스템을 통한 I/O 연산은 메모리의 특정 영역인 buffer cache 사용
  - File 사용의 locality 활용
    - 한 번 읽어온 block에 대한 후속 요청시 buffer cache에서 즉시 전달
  - 모든 프로세스가 공용으로 사용
  - Replacement algorithm 필요 (LRU, LFU 등)
- Unified Buffer Cache
  - 최근의 OS에서는 기존의 buffer cache가 page cache에 통합됨

![image-20220523213447424](C:/Users/YoonJuhye/TIL/cs/os/os_11_File Systems Implementation.assets/image-20220523213447424.png)

![image-20220523213515235](C:/Users/YoonJuhye/TIL/cs/os/os_11_File Systems Implementation.assets/image-20220523213515235.png)



### 프로그램의 실행

![image-20220523213634265](C:/Users/YoonJuhye/TIL/cs/os/os_11_File Systems Implementation.assets/image-20220523213634265.png)

![image-20220523213710419](C:/Users/YoonJuhye/TIL/cs/os/os_11_File Systems Implementation.assets/image-20220523213710419.png)



# Chapter 12. Disk Management and Scheduling

### Disk Scheduling

- Access time의 구성

  - Seek time
    - 헤드를 해당 실린더로 움직이는데 걸리는 시간

  - Rotational latency
    - 헤드가 원하는 섹터에 도달하기까지 걸리는 회전지연시간

  - Transfer time
    - 실제 데이터의 전송 시간

- Disk Bandwidth
  - 단위 시간당 전송된 바이트의 수

- Disk Scheduling

  - seek time을 최소화하는 것이 목표

  - Seek time 은 seek distance 에 비례

![image-20220523213908499](C:\Users\YoonJuhye\AppData\Roaming\Typora\typora-user-images\image-20220523213908499.png)

### Disk Scheduling

- Logical block

  - 디스크의 외부에서 보는 디스크의 단위 정보 저장 공간들

  - 주소를 가진 1차원 배열처럼 취급

  - 정보를 전송하는 최소 단위

- Sector

  - Logical block이 물리적인 디스크에 매핑된 위치

  - Sector 0은 최외곽 실린더의 첫 트랙에 있는 첫 번째 섹터이다.



### Disk Management

- Physical formatting(Low-level formatting)

  - 디스크를 컨트롤러가 읽고 쓸 수 있도록 섹터들로 나누는 과정

  - 각 섹터는 header + 실제 data (보통 512 bytes) + trailer로 구성

  - header와 trailer는 sector number, ECC (Error-Correcting Code) 등의 정보가 저장되며 controller가 직접 접근 및 운영

- Partitioning

  - 디스크를 하나 이상의 실린더 그룹으로 나누는 과정

  - OS는 이것을 독립적 disk로 취급 (logical disk)

- Logical formatting

  - 파일 시스템을 만드는 것

  - FAT, inode, free space 등의 구조 포함

- Booting

  - ROM에 있는 "small bootstrap loader" 실행

  - sector 0 (boot block)을 load하여 실행

  - sector 0은 "full Bootstrap loader program"

  - OS를 디스크에서 load하여 실행



### Disk Scheduling Algorithm

- 큐에 다음과 같은 실린더 위치의 요청이 존재하는 경우 디스크 헤드 53번에서 시작한 각 알고리즘의 수행 결과는? (실린더의 위치는 0-199이다) 98, 183, 37, 122, 14, 124, 65, 67



#### FCFS (First Come First Served)

대단히 비효율적

![image-20220523214419151](C:\Users\YoonJuhye\AppData\Roaming\Typora\typora-user-images\image-20220523214419151.png)



#### SSTF(Shortest Seek Time First)

- 현재의 헤드 위치에서 제일 가까운 위치에 있는 헤드부터 처리 -> 이동 거리는 줄어듦

- starvation 문제 (계속 낮은 주소에서만 처리하게 됨)

![image-20220523214503133](C:\Users\YoonJuhye\AppData\Roaming\Typora\typora-user-images\image-20220523214503133.png)



#### SCAN (=엘리베이터 스케쥴링)

- disk arm이 디스크의 한쪽 끝에서 다른쪽 끝으로 이동하며 가는 길목에 있는 모든 요청을 처리한다.

- 다른 한쪽 끝에 도달하면 역방향으로 이동하며 오는 길목에 있는 모든 요청을 처리하며 다시 반대쪽 끝으로 이동한다.
- 문제점: 실린더의 위치에 따라 대기 시간이 다르다

![image-20220523214625234](C:\Users\YoonJuhye\AppData\Roaming\Typora\typora-user-images\image-20220523214625234.png)

![image-20220523215028438](C:/Users/YoonJuhye/TIL/cs/os/os_12_Disk Management and Scheduling.assets/image-20220523215028438.png)

#### C-SCAN

- SCAN의 문제점을 해결하기 위한 알고리즘

- 헤드가 한쪽 끝에서 다른쪽 끝으로 이동하며 가는 길목에 있는 모든 요청을 처리

- 다른쪽 끝에 도달했으면 요청을 처리하지 않고 곧바로 출발점으로 다시 이동

- SCAN보다는 균일한 대기 시간을 제공한다.

![image-20220523214815721](C:\Users\YoonJuhye\AppData\Roaming\Typora\typora-user-images\image-20220523214815721.png)

#### N-SCAN

- SCAN의 변형 알고리즘
- 일단 arm이 한 방향으로 움직이기 시작하면 그 시점 이후에 도착한 job은 되돌아올 때 service



#### LOOK & C-LOOK

- SCAN이나 C-SCAN은 헤드가 디스크 끝에서 끝으로 이동
- LOOK과 C-LOOK은 헤드가 진행 중이다가 그 방향에 더 이상 기다리는 요청이 없으면 헤드의 이동방향을 즉시 반대로 이동한다
- C-LOOK

![image-20220523215614076](C:/Users/YoonJuhye/TIL/cs/os/os_12_Disk Management and Scheduling.assets/image-20220523215614076.png)



#### Disk-Scheduling Algorithm의 결정

- SCAN, C-SCAN 및 응용 알고리즘은 LOOK, C-LOOK 등이 일반적으로 디스크 입출력이 많은 시스템에서 효율적인 것으로 알려져 있음
- File의 할당 방법에 따라 디스크 요청이 영향을 받음
- 디스크 스케줄링 알고리즘은 필요할 경우 다른 알고리즘으로 쉽게 교체할 수 있도록 OS와 별도의 모듈로 작성되는 것이 바람직하다



### Swap-Space Management

- Disk를 사용하는 2가지 이유

  - memory의 volatile(휘발성)한 특성 -> file system

  - 프로그램 실행을 위한 memory 공간 부족 -> swap space (swap area)

- Swap - Space

  - Virtual memory system에서는 디스크를 memory의 연장 공간으로 사용

  - 파일 시스템 내부에 둘 수도 있으나 별도 partition 사용이 일반적

    - 공간 효율성보다는 속도 효율성이 우선
    - 일반 파일보다 훨씬 짧은 시간만 존재하고 자주 참조됨
    - 따라서, block의 크기 및 저장 방식이 일반 파일시스템과 다름

    ![image-20220523215821278](C:/Users/YoonJuhye/TIL/cs/os/os_12_Disk Management and Scheduling.assets/image-20220523215821278.png)



### RAID

- RAID (Redundant Array of Independent Disks)

  - 여러 개의 디스크를 묶어서 사용

- RAID의 사용 목적

  - 디스크 처리 속도 향상

    - 여러 디스크에 block의 내용을 분산 저장
    - 병렬적으로 읽어옴 (속도 향상시킴)

  - 신뢰성(reliability) 향상

    - 동일 정보를 여러 디스크에 중복 저장

    - 하나의 디스크가 고장시 다른 디스크에서 읽어옴. (Mirroring, shadowing)

    - 단순한 중복 저장이 아니라 일부 디스크에 parity를 저장하여 공간의 효율성을 높일 수 있다.

    ![image-20220523220019258](os_12_Disk Management and Scheduling.assets/image-20220523220019258.png)

