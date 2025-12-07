import { useState } from 'react';
import './App.css';
import Capture from './components/Capture';
import InsertFace from './components/InsertFace';
import SearchFace from './components/SearchFace';
import LiveSearch from './components/LiveSearch';

function App() {
  const [dark,setDark] = useState(false);
  return (
    <div style={{ padding: 20, background: dark ? "#111" : "#f7f7f7", color: dark ? "#eee" : "#111", minHeight: "100vh" }}>
      <header style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <h1>Face Search UI</h1>
        <div>
          <label style={{marginRight: 8 }}>
            <input type="checkbox" checked={dark} onChange={e=> setDark(e.target.checked)} />Dark Mode
          </label>
        </div>
      </header>
      <main style={{ display: "grid", gridTemplateColumns: "1fr 380px", gap: 20, marginTop: 20 }}>
        <div>
          <LiveSearch />
          <hr style={{ margin: "20px 0" }} />
          <InsertFace />
          {/* <UploadMultiple /> */}
        </div>
        <aside>
          <SearchFace />
        </aside>
      </main>
    </div>



    // <div style={{padding:20}}>
    //   <h1>Face Search UI</h1>
    //   <Capture />
    //   <hr />
    //   <InsertFace />
    //   <hr />
    //   <SearchFace />
    // </div>
  );
}

export default App;
