
from fastapi import FastAPI, UploadFile,Form,Response

# 기본설정
from pydantic import BaseModel;
#서버에 정적파일 올리기 
from fastapi.staticfiles import StaticFiles;

###### 데이터 보낼떄 쓰는 ###
#sql문 사용하기 위해 import 해주기 
import sqlite3
# 변수에 메타 데이터 추가 가능  x: Annotated[int, "This is an integer"]
from typing import Annotated

###### 데이터를 프엔이 쓰기 쉽게 하기위해 쓰는것 ##### 
# # json 형태로 바꿔주기 
from fastapi.responses import JSONResponse;
# 
from fastapi.encoders import jsonable_encoder;




#db랑 연결시키기 
# 데이터 베이스 생성했던 파일이름 
con = sqlite3.connect('db.db', check_same_thread=False)
cur = con.cursor()


app = FastAPI()

#테이블에 추가하기 : post 
@app.post('/items')
async def create_item(
                image:UploadFile, 
                title:Annotated[str, Form()], 
                price:Annotated[int,Form()], 
                description:Annotated[str, Form()], 
                place: Annotated[str, Form()] ,
                insertAt: Annotated[int, Form()] #타임스템프, new Date의 기준 시간부터 현재시간까지 흐른시간 
                ):
    # 이미지의 경우 처리 시간이 필요함으로 awit이 필요 
    image_bytes = await image.read()
    # 데이터 베이스에 보내기 
    cur.execute(f"""
                  INSERT INTO items(title,image,price,description,place,insertAt)
                  VALUES ('{title}', '{image_bytes.hex()}', {price},'{description}','{place}',{insertAt})
                """)
    con.commit()
    return  '200'
  

@app.get('/items')
async def get_list():
    #컬럼명도 같이 가져오기 
    con.row_factory =sqlite3.Row
    cur  = con.cursor()
    rows = cur.execute(f"""SELECT * from items;""").fetchall()
    # 데이터 객체형태로 가공하기 
    # 도큐먼트형태로 변경 : 배열상태의 데이터를 : 다시 객체로 변경 
    # jsonable_encoder를 통해서 파이섰 객체를 json으로 인코딩하고 , JSONResponse을 통해 , json으로 응답 
    return JSONResponse(
      jsonable_encoder(dict(row) for row in rows
      ))

  
  #이미지 응답
  # 각주소(id)에 맞는 개별 이미지를 줘야하기 때문에 
@app.get('/images/{item_id}')
async def get_image(item_id):
    cur = con.cursor()
    #16진법
    image_bytes = cur.execute(f"""
                              SELECT image from items WHERE id={item_id}
                              """).fetchone()[0]
    return Response(content=bytes.fromhex(image_bytes))
  


app.mount("/", StaticFiles(directory="frontend", html=True), name="static")
