#!/usr/bin/env awk -f

BEGIN { header = ""; sum = 0;}
{ 
	if( header != $1 && sum != 0){
		sum /= last_size;
		printf("%s\t%i\t%.3f\n",header, last_size, sum);
	}

	sum += $3;
	header = $1;
	last_size = $2;
}
END { sum /= last_size; printf("%s\t%i\t%.3f\n",header, last_size, sum); }
