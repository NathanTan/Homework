concurrency1: concurrency1.c
	gcc --std=c99 -lpthread concurrency1.c -o concurrency1
concurrency2: concurrency2.c
	gcc --std=c99 -lpthread concurrency2.c -o concurrency2
concurrency3: 
	gcc --std=c99 -lpthread concurrency3_p1.c -o concurrency3_p1
	gcc --std=c99 -lpthread concurrency3_p2.c -o concurrency3_p2

clean:
	rm concurrency1 concurrency2 concurrency3_p1 concurrency3_p2
