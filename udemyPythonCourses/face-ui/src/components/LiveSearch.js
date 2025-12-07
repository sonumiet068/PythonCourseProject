import React,{useRef,useState,useEffect} from "react"
import CameraPreview from "./CameraPreview"
import { live_search_image } from "../api"

export default function LiveSearch() {
  const camRef = useRef(null)
  const [running,setRunning] = useState(false)
  const [matches,setMatches] = useState([])
  const [intervalMs,setIntervalMs] = useState(800)
  const [showBoxes,setShowBoxes] = useState(true)

  useEffect(()=>{
     let timer = null;
     if(running){
       const loop = async ()=>{
       if(!camRef.current) return;
       const blob = await camRef.current.captureFrame();
       if(!blob) return;
       try{
         const res = await live_search_image(blob);
         setMatches(res);
       }catch(e){
        console.error("LiveSearch error:",e);
       }
      };
      loop();
      timer = setIntervalMs(loop,intervalMs);
    }
    return () => timer && clearInterval(timer);           
  },[running,intervalMs]);

    return (
    <div style={{ display: "flex", gap: 20 }}>
      <div>
        <h3>Live Search</h3>
        <CameraPreview onFrame={camRef} />
        <div style={{ marginTop: 8 }}>
          <button onClick={() => setRunning(s => !s)}>{running ? "Stop" : "Start"}</button>
          <label style={{ marginLeft: 12 }}>
            Interval(ms):
            <input type="number" value={intervalMs} onChange={e => setIntervalMs(Number(e.target.value))} style={{ width: 80, marginLeft: 6 }} />
          </label>
          <label style={{ marginLeft: 12 }}>
            <input type="checkbox" checked={showBoxes} onChange={e => setShowBoxes(e.target.checked)} /> Show boxes
          </label>
        </div>
      </div>

      <div style={{ width: 320 }}>
        <h3>Matches</h3>
        {matches.length === 0 && <div>No faces matched yet.</div>}
        {matches.map((m, idx) => (
          <div key={idx} style={{ border: "1px solid #ddd", padding: 8, marginBottom: 8, borderRadius: 6 }}>
            <div style={{ display: "flex", gap: 8 }}>
              {m.match_image_url && <img src={m.match_image_url} alt="" style={{ width: 80, height: 80, objectFit: "cover", borderRadius: 4 }} />}
              <div>
                <div style={{ fontWeight: 700 }}>{m.name || m.id || "Unknown"}</div>
                <div>Score: {(m.score ?? 0).toFixed(3)}</div>
                <div>Box: {m.bbox ? `${m.bbox.x},${m.bbox.y},${m.bbox.w},${m.bbox.h}` : "-"}</div>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );  
}