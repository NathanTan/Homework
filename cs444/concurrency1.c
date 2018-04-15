#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <semaphore.h>
#include <stdlib.h>
#include "mt19937ar.c"

#define NUM_THREADS 30
#define BUFFER_SIZE 32

/* Function Headers */
unsigned int get_random_value(unsigned int ecx);
void *produce_event(void *params);
void *consumer_event(void *params);
void print_buffer_item(int pos);

typedef struct Item
{
    int value;
    int c_sleep; // Time consumer should sleep before consuming the next item.
} Item;

typedef struct Thread_Params
{
    int random_value;
    int buffer_pos;
    int consumer_sleep_time;
} Thread_Params;

/* Semaphores */
sem_t mutex;
sem_t items;
sem_t spaces;

/* Buffer */
Item buffer[BUFFER_SIZE];

int main(int argc, char **argv)
{

    unsigned int eax;
    unsigned int ebx;
    unsigned int ecx;
    unsigned int edx;
    unsigned int randd;
    int current_buff = 0;
    Item event = {};

    char vendor[13];

    init_genrand(5); // Seed mt19937

    eax = 0x01;

    __asm__ __volatile__(
        "cpuid;"
        : "=a"(eax), "=b"(ebx), "=c"(ecx), "=d"(edx)
        : "a"(eax));

    // randd = get_random_value(ecx);

    // randd = (randd % 8) + 2;

    // printf("%u\n", randd);

    /* Semaphore Initalization */

    if (sem_init(&mutex, 0, 1) == -1)
        printf("Error\n");
    if (sem_init(&items, 0, 0) == -1)
        printf("Error\n");
    if (sem_init(&spaces, 0, BUFFER_SIZE) == -1)
        printf("Error\n");

    /* Algorithm taken from the little book of semaphores */

    pthread_t threads[NUM_THREADS];
    int result;
    int t = 0;
    int random = 0;
    while (1)
    {
        // Produce Item
        if (current_buff < 31)
        {

            // Wait 3-7 seconds before starting next event
            sleep((get_random_value(ecx) % 4) + 3);

            random = get_random_value(ecx);

            Thread_Params params = {random, current_buff, (random % 8) + 2};

            result = pthread_create(threads + t, NULL, produce_event, (void *)&params);

            sleep(1);
            print_buffer_item(current_buff);

            t++;
            current_buff++;
        }
    }

    return 0;
}

void *consumer_event(void *params)
{
    /* Consumer */
    // Item event = {};

    // sem_wait(&items);
    // sem_wait(&mutex);
    // event = buffer[current_buff];
    // sem_post(&mutex);
    // sem_post(&spaces);

    // // "Process" the event
    // wait(2);
}

/* Producer */
void *produce_event(void *params)
{
    Thread_Params *p = (Thread_Params *)(params);

    Item new_item = {p->random_value, p->consumer_sleep_time};

    sem_wait(&spaces);
    sem_wait(&mutex);

    // Add the new event to the buffer
    buffer[p->buffer_pos] = new_item;

    sem_post(&mutex);
    sem_post(&items);

    return;
}

void print_buffer_item(int pos)
{
    printf("Buffer[%d]: \n", pos);
    printf("value: [%u]\n", buffer[pos].value);
    printf("time:  [%u]\n\n", buffer[pos].c_sleep);
}

unsigned int get_random_value(unsigned int ecx)
{
    /* Generate random number */

    unsigned int random_value;

    if (ecx & 0x40000000)
    {
        //use rdrand

        int i = 0;
        unsigned int rand = 0;
        unsigned char ok = 0;
        for (i = 0; i < 9; i++)
        {
            __asm__ __volatile__(
                "rdrand %0; setc %1"
                : "=r"(rand), "=qm"(ok));
        }

        random_value = rand;
        //        printf("%u\n", rand);
    }
    else
    {
        //use mt19937

        random_value = genrand_int32();
        //printf("%u\n", random_value);
    }

    return random_value;
}