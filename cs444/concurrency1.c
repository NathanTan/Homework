#include <stdio.h>
#include <string.h>
#include "mt19937ar.c"

/* Function Headers */
unsigned int get_random_value(unsigned int ecx);    

int main(int argc, char **argv)
{

	unsigned int eax;
	unsigned int ebx;
	unsigned int ecx;        
    unsigned int edx;
    unsigned int randd;

	char vendor[13];
	
	eax = 0x01;

	__asm__ __volatile__(
	                     "cpuid;"
	                     : "=a"(eax), "=b"(ebx), "=c"(ecx), "=d"(edx)
	                     : "a"(eax)
	                     );
    
    randd = get_random_value(ecx);

    randd = (randd % 8) + 2;
    
    printf("%u\n", randd);

	return 0;
}

unsigned int get_random_value(unsigned int ecx) {
    /* Generate random number */                 
    
    unsigned int random_value;
    
	if(ecx & 0x40000000){
        //use rdrand
        
        int i = 0;
        unsigned int rand = 0;
        unsigned char ok = 0;
        for(i = 0; i < 9; i++){
            __asm__ __volatile__ (
                "rdrand %0; setc %1" 
                : "=r" (rand), "=qm" (ok)
            );
        }

        random_value = rand;
        //        printf("%u\n", rand);
    }
	else{
        //use mt19937
        printf("Using mt19937\n");

        init_genrand(5);
        random_value = genrand_int32();
        printf("%u\n", random_value);
    }

    return random_value;
}