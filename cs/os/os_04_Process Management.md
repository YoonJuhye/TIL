# **Chapter 4. Process Management**

> 프로세스 생성, 종료

------

### **프로세스 생성 (Process Creation)**

Copy-On-Write (COW) : 자식은 부모 자원을 그대로 공유하여 사용하고 있다가 write 발생할 경우 복사

- 부모 프로세스(Parent process)가 자식 프로세스(children process)를 생성
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
  - 자식이 종료(terminate)될 때까지 부모가 기다리는(wait-블럭된 상태) 모델 - wait() 시스템 콜
- 주소 공간(Address space)
  - 자식은 부모의 공간을 복사함 (binary and OS data) -fork
  - 자식은 그 공간에 새로운 프로그램을 올림 (복제 생성 후 덮어 씌움-exec)
- UNIX의 예
  - **fork()** 시스템 콜이 새로운 프로세스를 생성
    - 부모를 그대로 복사 (OS data except PID + binary)
    - 주소 공간 할당
  - fork 다음에 이어지는 **exec()** 시스템 콜을 통해 새로운 프로그램을 메모리에 올림



### fork() 시스템 콜

- A process is created by the fork() system call.

  - creates a new address space that is a duplicate of the caller.

  - 부모 프로세스

    ```c
    int main()
    {	int pid;
    	pid = fork();
    	if (pid == 0) /* this is child */
    		printf("\n Hello, I am child!\n");
    	else if (pid > 0) /* this is parent */
    		printf("\n Hello, I am parent!\n");
    }
    ```

    위에서부터 실행하다가 fork를 만나면 새로운 프로세스를 만듦

    아래와 같은 자식 프로세스가 생기고, 

    함수 실행이 끝나면 부모 프로세스는 아래쪽의 코드를 계속 실행함

    자식 프로세스는 main 함수의 시작부터 실행하는 것이 아니라 fork 이후부터 실행함

  - 자식 프로세스

    ```c
    int main()
    {	int pid;
    	pid = fork();
    	if (pid == 0) /* this is child */
    		printf("\n Hello, I am child!\n");
    	else if (pid > 0) /* this is parent */
    		printf("\n Hello, I am parent!\n");
    }
    ```

    프로세스의 fork를 통한 복제 생성은 부모 프로세스의 문맥을 그대로 복사함. 부모 입장에서는 프로그램 카운터가 fork를 가리키고 있음. fork가 끝난 시점에 문맥이 이르고, 자식도 그대로 copy 하므로 main 함수의 제일 윗부분부터 실행하는 것이 아닌, 부모가 fork한 것을 그대로 이어 다음 코드 부분을 실행함.

  - 자식과 부모의 혼동 문제를 막기 위해, 구분 해줌

    부모 프로세스는 pork의 결과 값이 양수, 자식 프로세스는 0

    **Parent process**

    pid > 0

    **Child process**

    pid = 0



### exec() 시스템 콜

- A process can execute a different program by the exec() system call.

  - replaces the memory image of the caller with a new program.

    ```c
    int main()
    {	int pid;
    	pid = fork();
    	if (pid == 0) /* this is child */
        {	printf("\n Hello, I am child! Now I'll run date \n");
        	execlp("/bin/date", "/bin/date", (char *) 0);
        }	
    	else if (pid > 0) /* this is parent */
    		printf("\n Hello, I am parent!\n");
    }
    ```

    execlp 함수가 결국 exec() 시스템 콜을 하게 됨. 

    새로운 시스템으로 덮어 씌움. 

    /bin/date 는 리눅스에서의 커맨드, 프로그램임. 

    부모 프로세스 실행 후 자식은 "\n Hello, I am child! Now I'll run date \n"를 출력하고 이후 date라는 새로운 시스템으로 덮어 쓰는 식으로 실행이 되는 것.

    exec 한 뒤에는 다시 돌아갈 수 없음.

  - 꼭 자식을 만들어서 exec 할 필요는 없음

    ```c
    int main(){
    	printf("\n Hello, I am child! Now I'll run date \n");
        execlp("/bin/date", "/bin/date", (char *) 0);
    	printf("\n Hello, I am parent!\n");
    }
    ```

    

### wait() 시스템 콜

- 프로세스 A가 wait() 시스템 콜을 호출하면

  - 커널은 child가 종료될때 까지 프로세스 A를 sleep시킨다 (block 상태) - 잠들게 만듦
  - Chile process가 종료되면 커널은 프로세스 A를 깨운다 (ready 상태) 

  ```c
  main {
      int childPID;
      S1;
      
      childPID = fork(); /* fork를 한 뒤에 결과값이 0이면, */
      if(childPID == 0)
          <code for child process>
      else { /* 결과값이 0이 아니라면 (부모 프로세스라면) */ 
          
          wait(); /* wait을 넣어줘서 잠들게 됨. */
      } /* cpu를 얻지 못하고 자식 프로세스가 종료될 때까지 기다림 */
      
      S2;
  }
  ```




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



### exit() 시스템 콜

- 프로세스의 종료
  - 자발적 종료
    - 마지막 statement 수행 후 exit() 시스템 콜을 통해
    - 프로그램에 명시적으로 적어주지 않아도 main 함수가 리턴되는 위치에 컴파일러가 넣어줌
  - 비자발적 종료
    - 부모 프로세스가 자식 프로세스를 강제 종료시킴
      - 자식 프로세스가 한계치를 넘어서는 자원 요청
      - 자식에게 할당된 태스크가 더 이상 필요하지 않음
    - 키보드로 kill, break 등을 친 경우
    - 부모가 종료하는 경우
      - 부모 프로세스가 종료하기 전에 자식들이 먼저 종료됨



### 프로세스와 관련한 시스템 콜

- fork() : create a child (copy)
- exec() : overlay new image
- wait() : sleep until child is done
- exit() : frees all the resources, notify parent



### 프로세스 간 협력

- 독립적 프로세스 (Independent process)
  - 프로세스는 각자의 주소 공간을 가지고 수행되므로 원칙적으로 하나의 프로세스는 다른 프로세스의 수행에 영향을 미치지 못함
- 협력 프로세스 (Cooperating process)
  - 프로세스 협력 메커니즘을 통해 하나의 프로세스가 다른 프로세스의 수행에 영향을 미칠 수 있음
- 프로세스 간 협력 메커니즘 (IPC : Interprocess Communication)
  - 메시지를 전달하는 방법
    - **message passing** : 커널을 통해 메시지 전달
  - 주소 공간을 공유하는 방법
    - **shared memory** : 서로 다른 프로세스 간에도 일부 주소 공간을 공유하게 하는 shared memory 메커니즘이 있음 (처음에는 커널의 도움을 받지만 이후에는 프로세스 간 공유함-서로 신뢰할 수 있는 관계여야 함)
    - thread : thread는 사실상 하나의 프로세스이므로 프로세스 간 협력으로 보기는 어렵지만 동일한 process를 구성하는 thread들 간에는 주소 공간을 공유하므로 협력이 가능 (주소 공간 자체를 thread 자체가 완전 공유하기 때문에)



### Meassage Passing

- Message system

  - 프로세스 사이에 공유 변수(shared variable)를 일체 사용하지 않고 통신하는 시스템
  - 메시지를 직접 보낼 수 없고 운영체제 **커널**을 통해서 전달 가능

- Direct Communication

  - 통신하려는 프로세스의 이름(Q)을 **명시적**으로 표시

    ​		Process P 		=> 		Process Q

    Send (Q, message)	Receive (P, message)

- Indirect Communication

  - mailbox (또는 port)를 통해 메시지를 **간접** 전달

    ​		Process P 	=>	Mailbox M	=>	Process Q

    Send (M, message)							Receive (P, message)

- shared memory : 주소 공간을 공유하는 방법

  - shared memory : 서로 다른 프로세스 간에도 일부 주소 공간을 공유하게 하는 shared memory 메커니즘
  - thread : thread는 사실상 하나의 프로세스이므로 프로세스 간 협력으로 보기는 어렵지만 동일한 process를 구성하는 thread들 간에는 주소 공간을 공유하므로 협력이 가능



### Interprocess Communication

