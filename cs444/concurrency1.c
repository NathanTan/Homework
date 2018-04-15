#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <semaphore.h>
#include <stdlib.h>
#include "mt19937ar.c"

#define NUM_THREADS 30
#define BUFFER_SIZE 32

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

/* Function Headers */
unsigned int get_random_value(unsigned int ecx);
void *produce_event();
void *consume_event();
void print_buffer_item(int pos);
void print_buffer(int size);
void print_item(Item item);

/* Semaphores */
sem_t mutex;
sem_t items;
sem_t spaces;

/* Buffer */
Item buffer[BUFFER_SIZE];

unsigned int ecx;
int current_buff;

int main(int argc, char **argv)
{

    unsigned int eax;
    unsigned int ebx;
    unsigned int edx;
    unsigned int randd;
    Item event = {};
    current_buff = 0;

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
    int thread_count = 10;
    int i;
    for (i = 0; i < thread_count; i += 2)
    {
        pthread_create(&threads[i], NULL, produce_event, NULL);
        pthread_create(&threads[i + 1], NULL, consume_event, NULL);
    }

    for (i = 0; i < thread_count; i++)
    {
        pthread_join(threads[i], NULL);
    }

    // print_buffer(current_buff);

    return 0;
}

void *consume_event()
{
    while (1)
    {
        /* Consumer */
        Item event = {};

        sem_wait(&items);
        sem_wait(&mutex);

        if (current_buff > 0)
        {
            current_buff--;
            event = buffer[current_buff]; // Get the event

            sem_post(&mutex);
            sem_post(&spaces);

            // "Process" the event
            printf("\t\t\tSleeping for event [%d]: %u\n", current_buff, event.c_sleep);
            printf("\t\t\t(value: %u)\n", event.value);
            sleep(event.c_sleep);
        }
    }
}

/* Producer */
void *produce_event()
{
    int random = 0;
    int sleep_time = 0;

    while (1)
    {
        sleep_time = 0; // Reset sleep time

        random = get_random_value(ecx);

        // Loop to make sure the sleep time is valid
        while (sleep_time < 2 || sleep_time > 9)
        {

            sleep_time = (random % 8) + 2;
            random = get_random_value(ecx);
        }

        sleep((random % 4) + 3); // simulate waiting for event

        // Create the event
        Item new_item = {
            random,
            sleep_time

        };

        //Thread_Params *p = (Thread_Params *)(params);
        sem_wait(&spaces);
        sem_wait(&mutex);

        if (current_buff < 32)
        {

            // Add the new event to the buffer
            buffer[current_buff] = new_item;
            printf("Adding item [%d]\n", current_buff);
            print_item(new_item);
            current_buff++;
        }

        sem_post(&mutex);
        sem_post(&items);
    }
    return;
}

void print_buffer_item(int pos)
{
    printf("Buffer[%d]: \n", pos);
    printf("value: [%u]\n", buffer[pos].value);
    printf("time:  [%u]\n\n", buffer[pos].c_sleep);
}

void print_item(Item item)
{
    printf("value: [%u]\n", item.value);
    printf("time:  [%u]\n\n", item.c_sleep);
}

void print_buffer(int size)
{
    int i;
    printf("---------------------");
    for (i = 0; i < size; i++)
        print_buffer_item(i);
    printf("---------------------");
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