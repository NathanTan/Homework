#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <semaphore.h>
#include <stdlib.h>

typedef struct LightSwitch
{
   int counter;
   sem_t lock;
} LightSwitch;

sem_t resources;
sem_t output;
sem_t super;
LightSwitch lightSwitch;

/* Function Definitions */
void unlock(LightSwitch *ls, sem_t *sem);
void lock(LightSwitch *ls, sem_t *sem);
void *process(void *processId);

int main(int argc, char **argv)
{
   int numberOfThreads = 3;

   srand(3);

   /* Initalize Semaphors */
   if (sem_init(&resources, 0, 3) == -1)
      printf("Error initalizing semaphore\n");
   lightSwitch.counter = 0;
   if (sem_init(&lightSwitch.lock, 0, 1) == -1)
      printf("Error initalizing semaphore\n");
   if (sem_init(&output, 0, 1) == -1)
      printf("Error initalizing semaphore\n");
   if (sem_init(&super, 0, 1) == -1)
      printf("Error initalizing semaphore\n");

   pthread_t processors[numberOfThreads + 1];

   int i;
   int ids[3] = {1, 2, 3};

   for (i = 0; i < numberOfThreads; i++)
   {
      pthread_create(&processors[i], NULL, process, &ids[i]);
   }

   for (i = 0; i < numberOfThreads; i++)
   {
      pthread_join(processors[i], NULL);
   }
   while (1)
   {
      printf("In main\n");
      sleep(3);
   }
}

void unlock(LightSwitch *ls, sem_t *sem)
{
   printf("\t\tWaiting on ls\n");
   sem_wait(&ls->lock);
   ls->counter--;
   if (ls->counter == 0)
   {
      sem_post(sem);
   }
   sem_post(&ls->lock);
   printf("\t\tGiving up ls\n");
}

void lock(LightSwitch *ls, sem_t *sem)
{
   sem_wait(&ls->lock);
   ls->counter++;
   if (ls->counter == 1)
   {
      sem_wait(sem);
   }
   sem_post(&ls->lock);
   return;
}

void *process(void *processId)
{
   int *id = (int *)processId;
   while (1)
   {
      int waitTime = rand() % 15;
      int processTime = (rand() % 8) + 2;

      lock(&lightSwitch, &super);
      sem_wait(&resources);

      sem_wait(&output);
      printf("Thread (%lu) is using a resource\n", *id);
      sem_post(&output);

      sleep(2);

      sem_wait(&output);
      printf("Process %lu finished\n", *id);
      sem_post(&output);

      sem_post(&resources);
      unlock(&lightSwitch, &super);

      sleep(processTime);
   }
}
