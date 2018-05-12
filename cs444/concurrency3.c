#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <semaphore.h>
#include <stdlib.h>

   sem_t resource;

   void process();


int main(int argc, char **argv) {

   int numberOfThreads = 5;
   srand(3);

   if (sem_init(&resource, 0, 3) == -1)
      printf("Error initalizing semaphore\n");

   pthread_t processors[numberOfThreads];


   int i;
   for (i = 0; i < numberOfThreads; i++) {
      pthread_create(&processors[i], NULL, process, NULL);
   }


   for (i = 0; i < numberOfThreads; i++) {
      pthread_join(processors[i], NULL);
   }
   while (1){
      printf("In main\n");
      sleep(3);
   }

}


void process() {

   int waitTime = rand() % 15;
   int processTime = rand() % 10;

   sleep(waitTime);

   sem_wait(&resource);
   printf("Processing!     %d\n", waitTime);

   sleep(processTime);
   printf("Done processing %d\n", waitTime);
   return;
}

