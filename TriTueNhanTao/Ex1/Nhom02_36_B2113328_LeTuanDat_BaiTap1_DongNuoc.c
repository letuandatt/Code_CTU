#include<stdio.h>
#define tankcapacity_x 9
#define tankcapacity_y 4
#define empty 0
#define goal 6
#define MaxLength 100

typedef struct{
	int x, y;
}State;

void make_null_state(State *state){
	state->x = 0;
	state->y = 0;
}

void print_state(State state){
	printf("\n   X:%d --- Y: %d", state.x, state.y);
}

int goalcheck(State state){
	return state.x == goal || state.y == goal;
}

int pourWaterFullX(State cur, State *result){
	if(cur.x < tankcapacity_x){
		result->x = tankcapacity_x;
		result->y = cur.y;
		return 1;
	}
	return 0;
}

int pourWaterFullY(State cur, State *result){
	if(cur.y < tankcapacity_y){
		result->x = cur.x;
		result->y = tankcapacity_y;
		return 1;
	}
	return 0;
}

int pourWaterEmptyX(State cur, State *result){
	if(cur.x > 0){
		result->x = empty;
		result->y = cur.y;
		return 1;
	}
	return 0;
}

int pourWaterEmptyY(State cur, State *result){
	if(cur.y > 0){
		result->x = cur.x;
		result->y = empty;
		return 1;
	}
	return 0;
}

int max(int a, int b){
	return a > b ? a : b;
}

int min(int a, int b){
	return a < b ? a : b;
}

int pourWaterXY(State cur, State *result){
	if(cur.x > 0 && cur.y < tankcapacity_y){
		result->x = max(cur.x - (tankcapacity_y - cur.y), empty);
		result->y = min(cur.x + cur.y, tankcapacity_y);
		return 1;
	}
	return 0;
}

int pourWaterYX(State cur, State *result){
	if(cur.y > 0 && cur.x < tankcapacity_x){
		result->x = min(cur.x + cur.y, tankcapacity_x);
		result->y = max(cur.y - (tankcapacity_x - cur.x), empty);
		return 1;
	}
	return 0;
}

int call_operator(State cur, State *result, int opt){
	switch(opt){
		case 1: return pourWaterFullX(cur, result);
		case 2: return pourWaterFullY(cur, result);
		case 3: return pourWaterEmptyX(cur, result);
		case 4: return pourWaterEmptyY(cur, result);
		case 5: return pourWaterXY(cur, result);
		case 6: return pourWaterYX(cur, result);
		default: printf("Error calls operators");
			return 0;
	}
}

const char* action[] = {"First State", "Pour Water Full X", "Pour Water Full Y",
						"Pour Water Empty X", "Pour Water Empty Y",
						"Pour Water X to Y", "Pour Water Y to X"};

int main(){
	State cur = {5, 4}, result;
	printf("Trang thai bat dau");
	print_state(cur);
	int opt;
	for(opt = 1; opt <= 6; opt++){
		int call = call_operator(cur, &result, opt);
		if(call == 1){
			printf("\nHanh dong %s thanh cong", action[opt]);
			print_state(result);
		}
		else printf("\nHanh dong %s KHONG thanh cong", action[opt]);
	}
	return 0;
}
