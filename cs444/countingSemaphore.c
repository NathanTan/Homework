#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <semaphore.h>
#include <stdlib.h>

sem_t resource;
sem_t super;

void process();
void checkSem();


int main(int argc, char **argv) {

   int numberOfThreads = 5;
   srand(3);

   if (sem_init(&resource, 0, 3) == -1)
      printf("Error initalizing semaphore\n");

   pthread_t processors[numberOfThreads + 1];


   int i;
   pthread_create(&processors[0], NULL, checkSem, NULL);
   for (i = 1; i < numberOfThreads; i++) {
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


void checkSem() {
   int* val = malloc(sizeof(int));
   int* superVal = malloc(sizeof(int));

   while(1) 
   {

      sleep(1);
      sem_getvalue(&resource, val);
      sem_getvalue(&super, superVal);

      if (*val == 0) {
         printf("\t\t\tBlocking on all new processes trying to access the resources\n");
         sem_wait(&super);
      }//TODO: pick up here, maybe use a mutex

      if (*val == 3) {
          printf("\t\t\tThe block has been lifted\n");
         sem_post(&super);
      }
      printf("\tSemVal: %d\n", *val);
   }
}

void process() {
   while(1) {
      sem_wait(&super);

      int waitTime = rand() % 15;
      int processTime = rand() % 10;

      sleep(waitTime);

      sem_wait(&resource);
      printf("Processing!     %d\n", waitTime);

      sleep(processTime);
      printf("Done processing %d\n", waitTime);
      sem_post(&resource);
   }
}
