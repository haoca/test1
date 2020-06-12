//2019.11.3++2020.3.11

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>
#include <time.h>
void color(short x)	//自定义函根据参数改变颜色
{
    if(x>=0 && x<=15)//参数在0-15的范围颜色
    	SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), x);	//只有一个参数，改变字体颜色
    else//默认的颜色白色
    	SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 7);
}//设置颜色

int main()
{
	//登录部分
	int b=0;//b为条件
	printf("请输入用户名：\n");
	FILE*p; //设置一个文件指针
     char ch;
	 //int a;//a为密码长度，之后用函数取得。
     char user[50]="1",pwd[]="1";
     scanf("%s",&user);
	 char *firstName = user;
     char *lastName = ".txt";
     char *name = (char *) malloc(strlen(firstName) + strlen(lastName));
    sprintf(name, "%s%s", firstName, lastName);
    //printf("%s\n", name);
	while((b==0)&&((p=fopen(name,"r"))==NULL)){//判断账号（文件）是否存在
		printf("检测到你是第一次打开程序，请设置你的密码:\n");
		scanf("%s",&pwd);//密码
		p=fopen(name,"w+");//读写的方式打开
        //a=strlen(pwd);//取长度
        //printf("%d\n",a);
        fwrite(pwd,strlen(pwd)+1,1,p);//写入密码 ，由于\0存在，要+1
        fclose(p);//记得关闭文件
       //printf("%s\n",pwd);
        printf("你的");
        color(15);printf("%d",strlen(pwd));
        color(7);printf("位数的密码");
	    color(15);printf("%s",pwd);
	    color(7);printf("已成功设置了。\n");
	b=1;//设置密码成功，退出条件。
	}

	    //printf("%d\n",a);
	    char ch1[]="0";
		printf("检测到您已经注册过，请输入你的密码：\n");
		char string[50];
		char inpsd[50];

		p=fopen(name,"r+");//打开文件
		fread(ch1,50,1,p);//读文件p内容，交给ch1
		fclose(p);
		//a=strlen(ch1);
		//printf("%s\n",ch1);
		scanf("%s",&inpsd);//输入密码
		//printf("%d\n",a);


		if(strcmp(ch1,inpsd)==0) {//判断ch1与输入密码是否一致
		printf("我亲爱的");
		color(15);printf("%s",user);
	    color(7);printf(",恭喜你成功登录.\n");

        int i1=1,ran;//i1指颜色序号



	//计算部分
	while(1){//这个1是为了使程序循环利用
            int choose1;
            printf("请选择你需要的功能:\n【1】计算 \n【2】随机数 \n【3】质数 \n ");
            scanf("%d",choose1);
    if(choose1==1)
    {
        printf("【1】那么，");
	 color(15);printf("%s",user);
	 color(7);printf("，请问你有几个B数?\n");
	 color(i1);
	int i,s=0,addn,choose2;

	scanf("%d",&addn);
	int x[20]={0};
		for(i=0;i<addn;i++)//加法运算
		{
			printf("第%d个数x[%d]=\n",i+1,i+1);
			scanf("%d",&x[i]);
			printf("你输入了%d\n",x[i]);
		}
	printf("【2】请选择您的算法?\n[1]加法,[2]乘法\n");
	scanf("%d",&choose2);
	switch(choose2)
	{
		case 1:{
		for(i=0;i<addn;i++)
		{
			s=s+x[i];//乘法
		}
		printf("你所输入的数和为：%d\n",s);
		}
		break;
		case 2:{
			s=1;
		for(i=0;i<addn;i++)
		{
			s=s*x[i];
		}
		printf("你所输入的数乘积为：%d\n",s);
		}

	}
	    color(i1);
		printf("POWER BY TITO\n");
		color(i1+1);
		srand(time(0));
		ran=rand()%6+2;//生成【2.7】间的随机数
		printf("[本次句子序号为%d]\n",ran-1);
		switch(ran-1){
		case 1:printf("PS.我喜欢你是寂静的，仿佛你消失了一样。\n\n遥远而且悲哀，仿佛你已经死了。\n");break;
		case 2:printf("PS.静月楼台空烦恼\n何处梦醉寄逍遥\n瑶琴缥缈纷纷扰\n惊扰故人的好觉\n叹人生路兜兜转转\n与你余情未了\n");break;
		case 3:printf("PS.你离开的步调不轻不重刚刚好\n缓缓在我心头\n筑起一座半世的监牢\n");break;
		case 4:printf("PS.有多少人为了眼前放弃自己的明天\n有多少人为了明天又在扼杀今天\n有多少人为了今天寄生给了欺骗\n又有多少人欺骗只为换取一丝尊严\n有多少人为了尊严却活在别人的胯下\n有多少人活在胯下只为养活他一家\n有多少人为了一家老小四海为家又\n有多少人漂泊日夜思念朋友和爸妈\n有多少人指手画脚的给别人讲着道理\n有多少人讲完道理自己却不讲道义\n有多少人纹着道义却出卖自己的兄弟\n有多少人从你的兄弟变成了你的凶器\n有多少人付出总是很难得到回报\n有多少人面对镜子流着眼泪微笑\n有多少人笑着在暴雨中疯狂奔跑\n有多少人为了名利戴上了冰凉的手铐\n有多少人为了苟活背叛了最初的理想\n");break;
		case 5:printf("PS.风雨凄凄，鸡鸣喈喈。\n既见君子，云胡不夷。\n风雨潇潇，鸡鸣胶胶。\n既见君子，云胡不瘳。\n风雨如晦，鸡鸣不已。\n既见君子，云胡不喜。\n\n");break;
		case 6:printf("PS.江民羽笨蛋。。\n\n");break;
		}

	    i1++;//换颜色
	system("pause");
	system("cls");
	printf("这是第[%d]次输入\n",i1);
			}//while


		}//if

    }
else{
		color(15);
	int ran;
		printf("垃圾，再见。。\n");
		color(2);
		printf("POWER BY TITO\n");
		color(3);
		srand(time(0));
		ran=rand()%6+2;
		printf("[本次句子序号为%d]\n",ran-1);
		switch(ran-1){
		case 1:printf("PS.我喜欢你是寂静的，仿佛你消失了一样。\n\n遥远而且悲哀，仿佛你已经死了。\n");break;
		case 2:printf("PS.静月楼台空烦恼\n何处梦醉寄逍遥\n瑶琴缥缈纷纷扰\n惊扰故人的好觉\n叹人生路兜兜转转\n与你余情未了\n");break;
		case 3:printf("PS.你离开的步调不轻不重刚刚好\n缓缓在我心头\n筑起一座半世的监牢\n");break;
		case 4:printf("PS.有多少人为了眼前放弃自己的明天\n有多少人为了明天又在扼杀今天\n有多少人为了今天寄生给了欺骗\n又有多少人欺骗只为换取一丝尊严\n有多少人为了尊严却活在别人的胯下\n有多少人活在胯下只为养活他一家\n有多少人为了一家老小四海为家又\n有多少人漂泊日夜思念朋友和爸妈\n有多少人指手画脚的给别人讲着道理\n有多少人讲完道理自己却不讲道义\n有多少人纹着道义却出卖自己的兄弟\n有多少人从你的兄弟变成了你的凶器\n有多少人付出总是很难得到回报\n有多少人面对镜子流着眼泪微笑\n有多少人笑着在暴雨中疯狂奔跑\n有多少人为了名利戴上了冰凉的手铐\n有多少人为了苟活背叛了最初的理想");break;
		case 5:printf("PS.风雨凄凄，鸡鸣喈喈。\n既见君子，云胡不夷。\n风雨潇潇，鸡鸣胶胶。\n既见君子，云胡不瘳。\n风雨如晦，鸡鸣不已。\n既见君子，云胡不喜。\n\n");break;
		case 6:printf("PS.江民羽笨蛋。。\n\n");break;
		}
	system("pause");
	}


}
