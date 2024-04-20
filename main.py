
from fastapi import FastAPI, UploadFile,Form,Response,Depends

# 기본설정
from pydantic import BaseModel;
#서버에 정적파일 올리기 
from fastapi.staticfiles import StaticFiles;
#로그인라이브러리 
from fastapi_login import LoginManager
#에러처리 
from fastapi_login.exceptions import InvalidCredentialsException

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


# 배포를 위한 서버단 테이블 생성하기 
#테이블이 없을 떄만 
cur.execute(f"""
            CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            image BLOB,
            price INTEGER NOT NULL,
            description TEXT,
            place TEXT NOT NULL,
            insertAt INTEGER NOT NULL
          )
            """)




app = FastAPI()


#로그인 셋팅 
#암호화를 위해 시크릿 코드가 하나 필요 
SERCRET = 'super-coding'
# 아래의 코드중 /login의 의미, 해당 경로에서만 토큰이 발급되도록 
manager = LoginManager(SERCRET ,'/login')


@manager.user_loader()
# 넘어어는 access토큰이 하나일떄와 객체일떄의처리 
def query_user(data):
  WHERE_STATEMENTS = f'''userid ="{data}"'''
  if type(data) == dict:
    WHERE_STATEMENTS = f'''userid = "{data['userid']}"'''
  con.row_factory = sqlite3.Row
  cur = con.cursor()
  user =  cur.execute(f'''
                        SELECT * from users WHERE {WHERE_STATEMENTS}
                      ''').fetchone()
  return user

@app.post('/login')
def login(
          userid:Annotated[str, Form()],
          userpsw:Annotated[str, Form()]):
    user = query_user(userid)
    print(userpsw)
    print(user['userpsw'])
    if not user: 
        raise InvalidCredentialsException
    elif userpsw != user['userpsw']:
        raise InvalidCredentialsException
    
    #세션의 경우 정보를 db에 저장 했다가 필요할떄 서버가 디비를 조회 데이터 가지고 오는거 
    # jwt 는 토큰안에다 정보를인코딩해서 가지고 있는거 
    access_token = manager.create_access_token(data={
      'sub':{
          'userid': user['userid'],
          'name': user['name'],
          'email': user['email'],
      }
    })
    
    return {'access_token' : access_token}
    





#테이블에 추가하기 : post 
@app.post('/items')
async def create_item(
                image:UploadFile, 
                title:Annotated[str, Form()], 
                price:Annotated[int,Form()], 
                description:Annotated[str, Form()], 
                place: Annotated[str, Form()] ,
                insertAt: Annotated[int, Form()],
                user=Depends(manager),
                #타임스템프, new Date의 기준 시간부터 현재시간까지 흐른시간 
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
  

#아이템 가져오기
@app.get('/items')
async def get_list(user=Depends(manager)):
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
    return Response(content=bytes.fromhex(image_bytes), media_type='image/*')
  
  
  #중복아이디검사로직 필요!! 
  
  
  
  
  
#회원가입
@app.post('/siginup')
def siginUp(
              userid:Annotated[str, Form()],
              userpsw:Annotated[str, Form()],
              name: Annotated[str, Form()],
              email:Annotated[str,Form()],
            ):
  
    cur = con.cursor()
    row = cur.execute(f'''
                        INSERT INTO users(userid,name,email,userpsw)
                        VALUES('{userid}','{name}','{email}', '{userpsw}')
                      ''')
    con.commit()
    print(userid, userpsw, name, email)
    return '200'


app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
