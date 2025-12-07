import {useState} from "react";
import { insertFaceImage } from "../api";

export default function InsertFace() {
    const[personId,setPersonId] = useState("");
    const[file,setFile] = useState();
       
  async function insertFaceHandlers() {
    if(!personId || !file){
      alert("Please enter name and upload image");
    }
    const response = await insertFaceImage(personId, file);
    alert(JSON.stringify(response)); 
  }
  
  return (
  <div>
  <h1>Insert Face</h1>
  <input placeholder="Person Id" onChange={e=> setPersonId(e.target.value)} />
  <input type="file" onChange={e=> setFile(e.target.files[0])}/>
  <button onClick={insertFaceHandlers}>Submit Face</button>
  </div>);
}