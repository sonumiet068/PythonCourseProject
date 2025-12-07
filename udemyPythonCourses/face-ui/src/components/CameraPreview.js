import React,{useRef,useEffect} from "react";

export default function CameraPreview({onFrame}) {
  const videoRef = useRef(null);
  const canvasRef = useRef(null);
  useEffect(()=>{
    let stream;
    async function start() {
      try{
        stream = await navigator.mediaDevices.getUserMedia({
          video: {facingMode:"user"},
          audio:false
        });
        if(videoRef.current){
          videoRef.current.srcObject = stream;
          // Wait for metadata to load  befor play()
          videoRef.current.onloadedmetadata = ()=>{
            videoRef.current.play().catch(err =>{
              console.error("Video play error:",err);
            });
          };
        }

      }catch(err) {
        console.err("Camera error:", err);
        alert("Camera Facing error");
      }
    }
    start();

    return () => {
      if (stream) {
        stream.getTracks().forEach(t => t.stop());
      }
    };
  },[]);

  const captureFrame = async ()=>{
    const vid= videoRef.current;
    const canvas = canvasRef.current;
    if(!vid || !canvas) return;
    canvas.width = vid.videoWidth;
    canvas.height = vid.videoHeight;
    const ctx = canvas.getContext("2d");
    ctx.drawImage(vid,0,0,canvas.width,canvas.height);
    return await new Promise(resolve => canvas.toBlob(resolve,"image/jpg",0.8));
  };

  useEffect(()=>{ 
   if(!onFrame) return;
   onFrame.current = {captureFrame};  
  },[onFrame]);

  return(
    <div style={{position:"relative"}}>
      <video ref={videoRef} style={{width:"100%",maxWidth:640}} muted/>
      <canvas ref={canvasRef} style={{display: "none"}} />
    </div>
  );

}