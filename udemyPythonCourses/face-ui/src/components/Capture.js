import {useState} from "react";
import { captureImage } from "../api";

export default function Capture() {
  const[messsage,setMessage]= useState("");
  async function handlerCapture() {
   const response = await captureImage();
   setMessage(JSON.stringify(response));
  }
return(
  <div>
    <h2>Capture Image from Camera</h2>
    <button onClick={handlerCapture}>Capture</button>
    <p>{messsage}</p>
  </div>);
  }
