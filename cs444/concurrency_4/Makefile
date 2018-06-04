all:
	make barber
	make debugSmokers

barber:
	gcc --std=c99 -lpthread barbershop.c -o barbershop
smokers:
	gcc --std=c99 -lpthread smokingProblem.c -o smokingProblem

debugSmokers:
	gcc --std=c99 -DDEBUG -lpthread smokingProblem.c -o smokingProblem

clean:
	rm barbershop
	rm smokingProblem
