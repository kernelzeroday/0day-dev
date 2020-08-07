This repo is a collection of code and research samples intended to display techniques on generic exploit development methodology. I dont know what the fuck i am doing, this is a scratchpad to attempt to document not knowing anything to having a functional exploit. Starting off we have 2 exploits, both buffer overflow, the first via an argv[i] -> buf[256] and the second is gets() -> buf[1024] rather than argv. 

Neither work, both need signifigant engineering effort to create a generic process for automated exploit development but both are promising and should see progress shortly. DB access to enter private restricted beta after completion of generic vuln exploitation process demo poc tutorial writeup.

```
(ins)kod@a:~/rev$ vagrant up
Bringing machine 'default' up with 'virtualbox' provider...
==> default: Box 'puppetlabs/debian-8.2-32-puppet' could not be found. Attempting to find and install...
    default: Box Provider: virtualbox
    default: Box Version: >= 0
==> default: Loading metadata for box 'puppetlabs/debian-8.2-32-puppet'
    default: URL: https://vagrantcloud.com/puppetlabs/debian-8.2-32-puppet
==> default: Adding box 'puppetlabs/debian-8.2-32-puppet' (v1.0.1) for provider: virtualbox
    default: Downloading: https://vagrantcloud.com/puppetlabs/boxes/debian-8.2-32-puppet/versions/1.0.1/providers/virtualbox.box
Download redirected to host: s3.amazonaws.com
==> default: Successfully added box 'puppetlabs/debian-8.2-32-puppet' (v1.0.1) for 'virtualbox'!
==> default: Importing base box 'puppetlabs/debian-8.2-32-puppet'...
==> default: Matching MAC address for NAT networking...
==> default: Checking if box 'puppetlabs/debian-8.2-32-puppet' version '1.0.1' is up to date...
==> default: Setting the name of the VM: rev_default_1596757651183_74816
Vagrant is currently configured to create VirtualBox synced folders with
the `SharedFoldersEnableSymlinksCreate` option enabled. If the Vagrant
guest is not trusted, you may want to disable this option. For more
information on this option, please refer to the VirtualBox manual:

  https://www.virtualbox.org/manual/ch04.html#sharedfolders

This option can be disabled globally with an environment variable:

  VAGRANT_DISABLE_VBOXSYMLINKCREATE=1

or on a per folder basis within the Vagrantfile:

  config.vm.synced_folder '/host/path', '/guest/path', SharedFoldersEnableSymlinksCreate: false
==> default: Clearing any previously set network interfaces...
==> default: Preparing network interfaces based on configuration...
    default: Adapter 1: nat
==> default: Forwarding ports...
    default: 22 (guest) => 2222 (host) (adapter 1)
==> default: Running 'pre-boot' VM customizations...
==> default: Booting VM...
==> default: Waiting for machine to boot. This may take a few minutes...
    default: SSH address: 127.0.0.1:2222
    default: SSH username: vagrant
    default: SSH auth method: private key
    default: Warning: Connection reset. Retrying...
    default:
    default: Vagrant insecure key detected. Vagrant will automatically replace
    default: this with a newly generated keypair for better security.
    default:
    default: Inserting generated public key within guest...
    default: Removing insecure key from the guest if it's present...
    default: Key inserted! Disconnecting and reconnecting using new SSH key...
==> default: Machine booted and ready!
==> default: Checking for guest additions in VM...
    default: The guest additions on this VM do not match the installed version of
    default: VirtualBox! In most cases this is fine, but in rare cases it can
    default: prevent things such as shared folders from working properly. If you see
    default: shared folder errors, please make sure the guest additions within the
    default: virtual machine match the version of VirtualBox you have installed on
    default: your host and reload your VM.
    default:
    default: Guest Additions Version: 5.0.16
    default: VirtualBox Version: 6.1
==> default: Mounting shared folders...
    default: /vagrant => /home/kod/rev
(ins)kod@a:~/rev$ vagrant ssh-config
Host default
  HostName 127.0.0.1
  User vagrant
  Port 2222
  UserKnownHostsFile /dev/null
  StrictHostKeyChecking no
  PasswordAuthentication no
  IdentityFile /home/kod/rev/.vagrant/machines/default/virtualbox/private_key
  IdentitiesOnly yes
  LogLevel FATAL

(ins)kod@a:~/rev$ vagrant ssh-config > ~/.ssh/config
```


and fault

```
vagrant@localhost:/vagrant$ ./mini-ntpclient AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Segmentation fault
```


exploit.py

```
─── Output/messages ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

Program received signal SIGSEGV, Segmentation fault.
ptmalloc_init () at arena.c:399
399    arena.c: No such file or directory.
─── Assembly ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
 0xb7e9ba6d  ptmalloc_init+157 je     0xb7e9ba95 <ptmalloc_init+197>
 0xb7e9ba6f  ptmalloc_init+159 xor    %edx,%edx
 0xb7e9ba71  ptmalloc_init+161 jmp    0xb7e9ba84 <ptmalloc_init+180>
 0xb7e9ba73  ptmalloc_init+163 nop
 0xb7e9ba74  ptmalloc_init+164 lea    0x0(%esi,%eiz,1),%esi
 0xb7e9ba78  ptmalloc_init+168 cmpb   $0x4d,(%edi)
 0xb7e9ba7b  ptmalloc_init+171 je     0xb7e9bb12 <ptmalloc_init+322>
 0xb7e9ba81  ptmalloc_init+177 add    $0x4,%esi
 0xb7e9ba84  ptmalloc_init+180 mov    (%esi),%edi
 0xb7e9ba86  ptmalloc_init+182 test   %edi,%edi
─── Breakpoints ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─── Expressions ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─── History ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─── Memory ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─── Registers ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
     eax 0xb7fcfde0      ecx 0xb7fcf8d8      edx 0x00000000      ebx 0xb7fce000     esp 0xbffff070     ebp 0xbffff0c8     esi 0xbffff3a0     edi 0x39785c30     eip 0xb7e9ba78     eflags [ PF IF RF ]
      cs 0x00000073       ss 0x0000007b       ds 0x0000007b       es 0x0000007b      fs 0x00000000      gs 0x00000033
─── Source ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Cannot display "arena.c"
─── Stack ─────────────────────────────────────────────────────────────────────────────────────────────────\xe2\x94\x80───────────────────────────────────────────────────────────────────────────────────────────────
[0] from 0xb7e9ba78 in ptmalloc_init+168 at arena.c:399
[1] from 0xb7e9bf1d in malloc_hook_ini+61 at hooks.c:32
[2] from 0xb7e9bf1d in malloc_hook_ini+61 at hooks.c:31
[3] from 0xb7e9ac87 in __GI___libc_malloc+295 at malloc.c:2883
[4] from 0xb7f22636 in gethostbyname+422 at ../nss/getXXbyYY.c:102
[5] from 0x08048756 in main+214 at mini-ntpclient.c:124
[6] from 0x08048756 in main+214 at mini-ntpclient.c:193
─── Threads ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
[1] id 3488 name mini-ntpclient from 0xb7e9ba78 in ptmalloc_init+168 at arena.c:399
─── Variables ───────────────────────────────────────\xe2\x94\x80─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
loc runp = 0xbffff3a0: Cannot access memory at address 0x39785c30, di = {dli_fname = 0xb7fda838 "/lib/i386-linux-gnu/i686/cmov/libc.so.6", dli_fbase = 0xb7e25000, dli_sname…, l = 0xb7fda860: {l_addr = 3085062144, l_name = 0xb7fda838 "/lib/i386-linux-gnu/i686/cmov/libc…, s = <optimized out>, hook = <optimized out>
─────────\xe2\x94\x80─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
```


new shit today:

```
─── Output/messages ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
line     : aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaama

Program received signal SIGSEGV, Segmentation fault.
0x0000555555555751 in main () at parse.c:46
46	    while ( *l ) {
─── Assembly ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
 0x0000555555555737  main+1442 mov    edx,0x13
 0x000055555555573c  main+1447 mov    esi,0x1
 0x0000555555555741  main+1452 lea    rdi,[rip+0x977]        # 0x5555555560bf
 0x0000555555555748  main+1459 call   0x555555555090 <fwrite@plt>
 0x000055555555574d  main+1464 mov    rax,QWORD PTR [rbp-0x10]
 0x0000555555555751  main+1468 movzx  eax,BYTE PTR [rax]
 0x0000555555555754  main+1471 test   al,al
 0x0000555555555756  main+1473 jne    0x55555555521b <main+134>
 0x000055555555575c  main+1479 jmp    0x55555555575f <main+1482>
 0x000055555555575e  main+1481 nop
─── Breakpoints ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─── Expressions ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─── History ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─── Memory ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─── Registers ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
   rax 0xffffffffffffc750    rbx 0x0000000000000000    rcx 0x0000000000000000   rdx 0x0000000000000000   rsi 0x000055555555a2b0      rdi 0x00007ffff7f9c4c0
   rbp 0x00007fffffffe3b0    rsp 0x00007fffffffc740     r8 0x0000000000000000    r9 0x000000000000003e   r10 0x00007fffffffc750      r11 0x0000000000000246
   r12 0x00005555555550b0    r13 0x00007fffffffe490    r14 0x0000000000000000   r15 0x0000000000000000   rip 0x0000555555555751   eflags [ IF RF ]         
    cs 0x00000033             ss 0x0000002b             ds 0x00000000            es 0x00000000            fs 0x00000000               gs 0x00000000        
─── Source ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
 41      cattail[0] = '\0';
 42  
 43      xsection = 0;
 44      ysection = 0;
 45  
 46      while ( *l ) {
 47      if ( tail[0] ) {
 48          strcat(cattail, "[");
 49          strcat(cattail, tail);
 50          strcat(cattail, "]");
─── Stack ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
[0] from 0x0000555555555751 in main+1468 at parse.c:46
─── Threads ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
[1] id 2218795 name parse from 0x0000555555555751 in main+1468 at parse.c:46
─── Variables ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
loc filename = "\000\340\377\377\377\177\000\000\361\343\375\367\377\177\000\000\001\000\000\000\000\000\000\000\27…, xsect = "\001\000\000\000\000\000\000\000\000\000\224\257\001\000\000\000\220\341\377\367\377\177\000\000\33…, ysect = "\360\355\377\367\377\177\000\000\220\344\377\377\377\177\000\000@\003\000\000\000\000\000\000\177EL…, x0 = 0x0, x1 = 0x0, y0 = 0x0, y1 = 0x0, xsection = 0x0, ysection = 0x0, extn = "\000\326\377\377\377\177\000\000\370\252\375\367\377\177", '\000' <repeats 11 times>, "P\002\000\00…, exti = 0xffffffff, tail = '\000' <repeats 1023 times>, cattail = '\000' <repeats 1023 times>, line = "aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaama", '\000' <repeats 973 times>, l = 0xffffffffffffc750 <error: Cannot access memory at address 0xffffffffffffc750>: Cann…, k = 0x0: Cannot access memory at address 0x0, i = 0x0, n = 0x0, length = 0x0
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

[ Legend: Modified register | Code | Heap | Stack | String ]
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── registers ────
$rax   : 0xffffffffffffc750
$rbx   : 0x0               
$rcx   : 0x0               
$rdx   : 0x0               
$rsp   : 0x00007fffffffc740  →  0x0000000000000000
$rbp   : 0x00007fffffffe3b0  →  0x0000555555555990  →  <__libc_csu_init+0> push r15
$rsi   : 0x000055555555a2b0  →  "line     : aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaa[...]"
$rdi   : 0x00007ffff7f9c4c0  →  0x0000000000000000
$rip   : 0x0000555555555751  →  <main+1468> movzx eax, BYTE PTR [rax]
$r8    : 0x0               
$r9    : 0x3e              
$r10   : 0x00007fffffffc750  →  "aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaama"
$r11   : 0x246             
$r12   : 0x00005555555550b0  →  <_start+0> xor ebp, ebp
$r13   : 0x00007fffffffe490  →  0x0000000000000001
$r14   : 0x0               
$r15   : 0x0               
$eflags: [zero carry parity adjust sign trap INTERRUPT direction overflow RESUME virtualx86 identification]
$cs: 0x0033 $ss: 0x002b $ds: 0x0000 $es: 0x0000 $fs: 0x0000 $gs: 0x0000 
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── stack ────
0x00007fffffffc740│+0x0000: 0x0000000000000000	 ← $rsp
0x00007fffffffc748│+0x0008: 0x0000000000000000
0x00007fffffffc750│+0x0010: "aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaama"	 ← $r10
0x00007fffffffc758│+0x0018: "caaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaama"
0x00007fffffffc760│+0x0020: "eaaafaaagaaahaaaiaaajaaakaaalaaama"
0x00007fffffffc768│+0x0028: "gaaahaaaiaaajaaakaaalaaama"
0x00007fffffffc770│+0x0030: "iaaajaaakaaalaaama"
0x00007fffffffc778│+0x0038: "kaaalaaama"
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── code:x86:64 ────
   0x555555555741 <main+1452>      lea    rdi, [rip+0x977]        # 0x5555555560bf
   0x555555555748 <main+1459>      call   0x555555555090 <fwrite@plt>
   0x55555555574d <main+1464>      mov    rax, QWORD PTR [rbp-0x10]
 → 0x555555555751 <main+1468>      movzx  eax, BYTE PTR [rax]
   0x555555555754 <main+1471>      test   al, al
   0x555555555756 <main+1473>      jne    0x55555555521b <main+134>
   0x55555555575c <main+1479>      jmp    0x55555555575f <main+1482>
   0x55555555575e <main+1481>      nop    
   0x55555555575f <main+1482>      movzx  eax, BYTE PTR [rbp-0x1460]
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── source:parse.c+46 ────
     41	 	cattail[0] = '\0';
     42	 
     43	 	xsection = 0;
     44	 	ysection = 0;
     45	 
             // l=0x00007fffffffe3a0  →  0xffffffffffffc750
 →   46	     while ( *l ) {
     47	 	if ( tail[0] ) {
     48	 	    strcat(cattail, "[");
     49	 	    strcat(cattail, tail);
     50	 	    strcat(cattail, "]");
     51	 	}
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── threads ────
[#0] Id 1, Name: "parse", stopped 0x555555555751 in main (), reason: SIGSEGV
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── trace ────
[#0] 0x555555555751 → main()
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
(ins)gef➤  

```

look in parse.py
