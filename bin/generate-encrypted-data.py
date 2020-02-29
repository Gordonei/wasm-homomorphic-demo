from phe import paillier
import sys

import jinja2

try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    assert a>=0 and b>=0
except:
    print(f"Having trouble converting {','.join(sys.argv[1:])} into positive integers")

# Generating key-pair
public_key, private_key = paillier.generate_paillier_keypair()
print(f"public_key=\n{hex(public_key.n)}\n\n")

# Encrypting the inputs
encrypted_a = public_key.raw_encrypt(a)
encrypted_b = public_key.raw_encrypt(b)

print(f"encrypted_a=\n{hex(encrypted_a)}\n")
print(f"encrypted_b=\n{hex(encrypted_b)}\n")

# Generating the template
with open("src/paillier_hello_template.c", "r") as template_file, \
     open("dist/paillier_hello.c", "w") as output_file:
    template_content = template_file.read()
    template = jinja2.Template(template_content)
    output = template.render(public_key_hex=hex(public_key.n)[2:],
                             encrypted_a=encrypted_a,
                             encrypted_b=encrypted_b)
    output_file.write(output)

print("Generated 'dist/paillier_hello.c' - please compile, and load")
print("Compile: emcc -o ./dist/paillier_hello.html ./dist/paillier_hello.c <PATH to libpaillier>/libpaillier/*.c <Path to libGMP>/libgmp.a")
print("Load: emrun --no_browser --port 8080 ./dist")

# Getting the result
result = input(">> encrypted_result=")

# Decrypting
result_value = paillier.EncryptedNumber(public_key, int(result, 16))
decrypted_result = private_key.decrypt(result_value)

print(f"decrypted_result=\n{decrypted_result}")

test_result = a + b
if decrypted_result == test_result:
    print("Results match!")
