#include<stdio.h>
#include<stdlib.h>
#include<math.h>

#define size 8

int queens[size];

int is_valid(int row, int col){
	int i;
	for(i = 0; i < row; ++i){
		if(queens[i] == col || abs(i - row) == abs(queens[i] - col)){
			return 0;
		}
	}
	return 1;
}

void show(){
	int i, j;
	for(i = 0; i < size; i++){
		for(j = 0; j < size; j++){
			if(queens[i] == j){
				printf("Q  ");
			} else {
				printf("-  ");
			}
		}
		printf("\n");
	}
	char c;
	printf("Press 'y' to see more, others to stop: ");
	scanf(" %c", &c);
	if(c == 'y' || c == 'Y'){
		printf("\n");
	} else {
		printf("Good bye ...");
		exit(0);
	}
}

void put_queens(int row){
	int col;
	for(col = 0; col < size; col++){
		if(is_valid(row, col)){
			queens[row] = col;
			if(row == size - 1){
				show();
			} else {
				put_queens(row + 1);
			}
			queens[row] = 0;
		}
	}
}

int main(){
	put_queens(0);
	return 0;
}
