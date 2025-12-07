import { useState } from "react";
import { searchFaceImage } from "../api";


export default function SearchFace() {

 const[file,setFile] = useState();
 async function searchHandler() {
  if(!file){
    alert("Please select image")
  }
  const result = await searchFaceImage(file);
  alert(result);
 }
return (
  <div>
    <h2>Search Face</h2>
    <input type="file" onChange={(e) => setFile(e.target.files[0])} />
    <button onClick={searchHandler}>Search Face</button>
  </div>
);

}