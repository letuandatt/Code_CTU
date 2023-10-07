#include<stdio.h>
#include<stdlib.h>
#define MAX_LENGTH 100
#define EMPTY 0
#define GRID 4
struct Coord{
    int x;
    int y;
};

struct List_Coord{
    Coord Elements[MAX_LENGTH];
    int Size;
};

void Init_List_Coord(List_Coord *List){
    List->Size = 0;
}

void Append_List_Coord(List_Coord *List, Coord Point){
    List->Elements[List->Size++] = Point;
}

int Index_Of(Coord Point){
    return (GRID*Point.x+Point.y);
}

Coord Get_Point(int Index){
    Coord Point = {Index/GRID, Index%GRID};
    return Point;
}

struct Constrains{
    List_Coord Array_Coord;
    char Operation;
    int Value_Of_Cage;
};

struct Kenken{
    int Cells[GRID][GRID];
    Constrains Cages[MAX_LENGTH];
    int Size;
};

int Value_Of_Cell(Kenken Board, Coord Point){
    return Board.Cells[Point.x][Point.y];
}

void Init_Board(Kenken *Board){
    for(int i=0;i<GRID;i++){
        for(int j=0;j<GRID;j++){
            Board->Cells[i][j] = 0;
        }
    }
}

Kenken Input_Data(){
    freopen("data.txt","r",stdin);
    Kenken Board;
    Init_Board(&Board);
    scanf("%d",&Board.Size);
    for(int i=0;i<Board.Size;i++){
        Init_List_Coord(&Board.Cages[i].Array_Coord);
        int Num_Cage = 0;
        scanf("%d%c%d",&Board.Cages[i].Value_Of_Cage,&Board.Cages[i].Operation,&Num_Cage);
        for(int j=0;j<Num_Cage;j++){
            int x,y;
            scanf("%d%d",&x,&y);
            Coord Point = {x,y};
            Append_List_Coord(&Board.Cages[i].Array_Coord,Point);
        }
    }
    return Board;
}

int Get_Cage(Kenken Board, Coord Point){
    for(int i=0;i<Board.Size;i++){
        for(int j=0;j<Board.Cages[i].Array_Coord.Size;j++){
            int x = Board.Cages[i].Array_Coord.Elements[j].x;
            int y = Board.Cages[i].Array_Coord.Elements[j].y;
            if(x == Point.x && y == Point.y){
                return i;
            }
        }
    }
}

int Is_Filled(Kenken Board){
    for(int i=0;i<GRID;i++){
        for(int j=0;j<GRID;j++){
            if(Board.Cells[i][j]==EMPTY){
                return 0;
            }
        }
    }
    return 1;
}

int Is_Full_Cage(Kenken Board, int Index){
    for(int i=0;i<Board.Cages[Index].Array_Coord.Size;i++){
        if(Value_Of_Cell(Board,Board.Cages[Index].Array_Coord.Elements[i])==0){
            return 0;
        }
    }
    return 1;
}

int Check_Duplicate(Kenken Board, Coord Point, int Value){
    for(int i=0;i<GRID;i++){
        if(Board.Cells[i][Point.y]==Value){
            return 0;
        }
    }
    for(int i=0;i<GRID;i++){
        if(Board.Cells[Point.x][i]==Value){
            return 0;
        }
    }
    return 1;
}

int Check_Cage(Kenken Board, Coord Point){
    int Index_Cage = Get_Cage(Board,Point);
    int Value = Board.Cages[Index_Cage].Value_Of_Cage;
    int Size = Board.Cages[Index_Cage].Array_Coord.Size;
    switch(Board.Cages[Index_Cage].Operation){
        case '+':{
            int total = 0;
            for(int i = 0; i < Board.Cages[Index_Cage].Array_Coord.Size; i++){
                total += Value_Of_Cell(Board, Board.Cages[Index_Cage].Array_Coord.Elements[i]);
            }
            
        }
        case '-':{
            if(!Is_Full_Cage(Board,Index_Cage)){
                return 1;
            }
            int Diff = 0;
            for(int i=0;i<Size;i++){
                Diff -= Value_Of_Cell(Board, Board.Cages[Index_Cage].Array_Coord.Elements[i]);
                Diff = abs(Diff);
            }
            if(Diff == Value){
                return 1;
            }else{
                return 0;
            }
        }
        case 'x':{
            int Mult = 1;
            for(int i=0;i<Size;i++){
                int Cell_Value = Value_Of_Cell(Board, Board.Cages[Index_Cage].Array_Coord.Elements[i]);
                if(Cell_Value == 0){
                    Mult *= 1;
                }else{
                    Mult *= Cell_Value;
                }
            }
            int DK_1 = 0;
            if(Mult==Value && Is_Full_Cage(Board,Index_Cage)){
                DK_1 = 1;
            }
            int DK_2 = 0;
            if(Mult<=Value && !Is_Full_Cage(Board,Index_Cage)){
                DK_2 = 1;
            }
            if(DK_1 || DK_2){
                return 1;
            }else{
                return 0;
            }
        }
        case '/':{
            if(!Is_Full_Cage(Board,Index_Cage)){
                return 1;
            }
            int Divi = 1;
            for(int i=0;i<Size;i++){
                int Cell_Value = Value_Of_Cell(Board, Board.Cages[Index_Cage].Array_Coord.Elements[i]);
                int Temp = Cell_Value;
                if(Cell_Value == 0){
                    Temp = 1;
                }
                if(Divi > Temp){
                    Divi = Divi / Temp;
                }else{
                    Divi = Temp / Divi;
                }
            }
            if(Divi == Value){
                return 1;
            }else{
                return 0;
            }
        }
        case '=':{
            if(Value == Value_Of_Cell(Board,Point)){
                return 1;
            }else{
                return 0;
            }
        }
        default: return 0;
    }
}
void Show_Board(Kenken Board){
	printf("KenKen Board :\n");
	for(int i=0;i<GRID;i++){
		if(i%GRID==0)
			printf("-----------------\n");
		for(int j=0;j<GRID;j++){
			if(j%GRID==0){
                printf("|");
            }
			printf("%2d |",Board.Cells[i][j]);
		}
		printf("\n");
	}
	printf("-----------------\n");
}

void Show_Cage(Kenken Board){
	printf("Board of CAGES:\n");
	for(int i=0;i<GRID;i++){
		if(i%GRID==0)
			printf("---------------------\n");
		for(int j=0;j<GRID;j++){
			Coord Point={i,j};
			if(j%GRID==0){
                printf("|");
            }
			printf("%2d%c |",Board.Cages[Get_Cage(Board,Point)].Value_Of_Cage,Board.Cages[Get_Cage(Board,Point)].Operation);
		}
		printf("\n");
	}
	printf("---------------------\n");
}

int Num_Of_State = 0;

int Solve_Board(Kenken *Board, int Row, int Col){
    if(Is_Filled(*Board)){
        return 1;
    }
    if(Col == GRID){
        Row += 1;
        Col = 0;
    }
    for(int Value=1;Value<=GRID;Value++){
		Coord Point ={Row,Col};
		if(Check_Duplicate(*Board,Point,Value)){
			Board->Cells[Row][Col] = Value;
			Num_Of_State++;
			if(Check_Cage(*Board,Point))
				if(Solve_Board(Board,Row,Col+1)==1)
					return 1;
		}
		Board->Cells[Row][Col] = 0;
	}
    return 0;
}
int main(int argc, char const *argv[]){
    Kenken Puzzle = Input_Data();
    Show_Board(Puzzle);
    Show_Cage(Puzzle);
    if(Solve_Board(&Puzzle,0,0)){
        printf("Tìm lời giải thành công!!!");
        Show_Board(Puzzle);
    }else{
        printf("Không thể tìm ra đáp án!!!");
    }
    printf("Số lượng trạng thái: %d",Num_Of_State);
}