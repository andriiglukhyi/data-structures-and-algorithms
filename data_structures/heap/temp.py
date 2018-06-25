
int sumOfMassiv(arr)
{
    int counter  = 0;
    float answer = 0; 
    int sum = 1;
    for (int i = 1; i <12; i++)
    {
        if ( i % 3 != 0)
        sum = sum * i;
        counter = counter + 1

        
    }

    answer = pow(sum, 1.0/counter)
    return answer
}