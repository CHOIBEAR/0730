#=============================1교시===========================================
# pandas 설치 방법 
# 1.uv init
# 2.uv가 설치된 폴더로 cd 해주기
# 3.uv add pandas
# 4.import pandas as pd
#   print(pd.__version__)
#   이 코드로 판다즈의 버전 확인.
# Numpy 
# pandas 데이터 분석을 위한 라이브러리. 
# import pandas as pd
#as pd 하는 이유 pandas  전부 입력하면 너무 길어지니 as 를 붙여서 별명으로 부르겠다 선언한것.

# print(pd.__version__)

# a = [1,2,3,4,5]
# # a = ["1","2","3","4","5"]
# i= ["1","2","3","4","5"] #<-인덱스를 변경하는게 가능하다.
# pd.Series(data=a)
# # data = pd.Series(data=a)
# data = pd.Series(data=a,index=i)
# # print(data)

# # loc[] 로케이션, iloc[] 인덱스 로케이션 이라 하는 함수들로 데이터를 하나씩 꺼내올 수 있다.
# # print(data.iloc[1]) <- 값의 인덱스 위치를 찾아 값을 찾아주는 함수는 iloc
# # print(data.loc[1])<- 인덱스의 값을 찾아 찾아주는 함수는 loc
# print(data.loc["3"],data[4])

# data = pd.Series(data=[1,2,3,4])
# print(data[ :2]) # 출력 결과는 인덱스 0 1 ,값은 1 2 파이썬처럼 인덱싱과 슬라이싱을 할 수 있음.

# b= [1,2,3,4] <- 위의 판다스 코드와 
# print(b[ :2])<- 아래의 파이썬 코드의 작동원리는 같다.

#==========================================2교시========================================

# import pandas as pd

# data = pd.Series(data=[1,2,3,4])
# print(data[ [1,2] ]) # <- 인덱스의 범위를 지정해서 꺼내는게 가능.
# print(data[1:3]) # 위의 코드와 동일한것임.

# # b= [1,2,3,4] 
# # print(b[ :2]) # print (b[[1,2]]) <-이건 불가능. 그러나 판다즈가 가능.

# data = pd.Series([3.0,5.0,7.0,9.0])# 이런식으로 직접 리스트를 넣는게 가능함.
# print(data)

# data=pd.Series(["가","나","다","라"])#문자열도 문제 없음.
# print(data)

# data = pd.Series([3.0,5.0,7.0,9.0],["가","나","다","라"])
# #앞에 들어가는 리스트는 요소값,데이터 이고 뒤로 들어가는 리스트는 인덱스이다.
# #인덱스를 변경할 수 있는 판다즈라 가능한 방법.
# print (data)

# arr = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# data = pd.DataFrame(arr)
# print(data[:2]) #2차원데이터에서도 슬라이싱이 가능하다.

# arr = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# idx = ["1행","2행","3행"]
# col = ["1열","2열","3열"] 
# data = pd.DataFrame(data=arr,index=idx,columns=col)
# print(type(data.loc["2행"])) # 꺼냈을때 형태가 바뀌는데 당연한것이다. 2차원데이터의 일부를 꺼내면
#                              # 1차원으로 변경된다.
#데이터 프레임은 시리즈로 이루어진 2차원 데이터이다.

# siri=[1,2,3,4,5,6,7,8,9]
# d=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# idx=["1행","2행","3행"]
# #idx = ["1행","2행","3행","4행","5행","6행","7행","8행","9행"]
# col = ["1열","2열","3열"]
# data=pd.DataFrame(data=d,index=idx,columns=col)
# #data=pd.Series(data=siri,index=idx)
# print(data)


#====================================3교시===========================================

import pandas as pd
import numpy as np #다차원 분석용 모듈.

# data=np.array([1,2,3,4,5])
# print(data)
# print(type(data))
# print(data[data>3]) # 넘파이는 비교자를 사용 가능하다.
# r= data * 3 한번에 리스트의 요소에 곱셈을 넣어 결과를 출력 가능.
# print(r)


# data=pd.read_csv("./data1.csv",index_col=0)#.csv 확장자명을 읽어오는 함수.
#                                #ㄴ인덱스를 제어하는 명령어.
# # print (data.index)
# for i in data.index: # 변수.인덱스를 이용하여 인덱스를 하나씩 반복해서 찾기.
#     s = data.loc[i]  # 변수 i에 담긴 요소를 s변수에 넣는 선언.
#     dan= s.loc["dan"] # 관리하기 편하게 찾은 요소들을 이름에 맞는 변수로 관리.
#     num= s.loc["num"] # 관리하기 편하게 찾은 요소들을 이름에 맞는 변수로 관리.
#     print(f'{dan}* {num}={dan*num}')


