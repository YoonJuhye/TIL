# **Process Management**

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
  - 자식이 종료(terminate)될 때까지 부모가 기다리는(wait-블럭된 상태) 모델
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

  - 커널은 child가 종료될때 까지 프로세스 A를 sleep시킨다 (block 상태)
  - Chile process가 종료되면 커널은 프로세스 A를 깨운다 (ready 상태)

  ```c
  main {
      int childPID;
      S1i
      
      childPID = fork();
      if(childPID == 0)
          <code for child process>
      else {
          
          wait()i
      }
      
      S2i
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
