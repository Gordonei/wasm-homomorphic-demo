#include <stdio.h>
#include "/home/gordon/workspace/libpaillier/paillier.h"

int main(int argc, char ** argv) {
      	printf("Hello, (paillier) world!\n");

	// Setting the public key
	paillier_pubkey_t pubkey = *paillier_pubkey_from_hex("{{ public_key_hex }}");
	
        paillier_ciphertext_t a,b,res;
	
	// Setting the 'a' value (1)
	int set_res = mpz_init_set_str(a.c, "{{ encrypted_a }}", 0); 
	if (set_res){
		printf("Got %d when trying to assign 'a'\n", set_res);
	}

	char *a_str;
	a_str = mpz_get_str(NULL, 16, a.c);

	printf("a='%s'\n", a_str);

	// Setting the B value (3)
	set_res = mpz_init_set_str(b.c, "{{ encrypted_b }}", 0); 
	if (set_res){
		printf("Got %d when trying to assign 'b'\n", set_res);
	}
	char *b_str;
	b_str = mpz_get_str(NULL, 16, b.c);

	printf("b='%s'\n", b_str);

	// Doing the ~~multiplication~~ addition
	paillier_mul(&pubkey, &res, &a, &b);

	// Printing out the result
	char *res_str;
	res_str = mpz_get_str(NULL, 16, res.c);

	printf("%s\n", res_str);	
}
