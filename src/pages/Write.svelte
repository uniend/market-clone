
<script>
  import { getDatabase, ref, push } from "firebase/database";
  import Footer from "../components/Footer.svelte";
  import { getDownloadURL, getStorage, ref as refimg, uploadBytes } from "firebase/storage";

  let title;
  let price;
  let description;
  let place;
  let files;


  const storage = getStorage();




  function writeUserData(urlImg) {
    const db = getDatabase();
    push(ref(db, 'items/'), {
      title,
      price,
      description,
      place,
      insertAt: new Date().getTime(),
      urlImg
    });
    alert('글쓰기가완료되었습니다. ')
    window.location.hash = '/'
  }

  
  const uploadFile = async () => {
    const file = files[0];
    const name = file.name;
    const imgRef = refimg(storage, name);
    await uploadBytes(imgRef, file);
    const url = await getDownloadURL(imgRef);
    return url;
  }

  const handleSubmint =  async () => {
    const url = await uploadFile();
    writeUserData(url)
  }
</script>





<form id="write-form" on:submit|preventDefault ={handleSubmint}>

  <div>
    <label for="image">이미지</label>
    <input type="file" id="image" name="image" bind:files={files}>
  </div>
  <div>
    <label for="title">제목</label>
    <input type="text" id="title" name="title" bind:value={title}>
  </div>
  <div>
    <label for="price">가격</label>
    <input type="number" id="price" name="price" bind:value={price}>
  </div>
  <div>
    <label for="description">설명</label>
    <input type="text" id="description" name="description" bind:value={description}>
  </div>
  <div>
    <label for="place">장소</label>
    <input type="text" id="place" name="place" bind:value={place}>
  </div>

  <div >
    <button type="submit" class="submit_btn">제출하기</button>
  </div>
  
</form>


<Footer location = 'wirte' />


<style>
  .submit_btn{
    background-color: tomato;
    margin: 10px;
    padding: 10px 15px;
    color: white;
    border-radius: 25px;
    cursor: pointer;
  }

</style>