int findDuplicate(int* nums, int numsSize){
    int i;
    int * key = (int*) malloc ((numsSize-1)*sizeof(int));
    for(i = 0; i < numsSize-1; i++)
        key[i] = 0;
    for(i = 0; i < numsSize; i++) {
        key[nums[i]-1]++;
    }
    for(i = 0; i < numsSize - 1; i++) {
        if (key[i]>= 2)
            return i+1;
    }

    return -1;
    free(key);
}