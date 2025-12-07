const API_URL="http://127.0.0.1:8000"

export async function captureImage() {
  const resp = await fetch(`${API_URL}/capture`);
  return resp.json();
}

export async function insertFaceImage(personId,file) {
  const form = new FormData()
  form.append('file',file)

  const queryParams = {'person_id':personId}
  const url = new URL(`${API_URL}/insert`);
  Object.keys(queryParams).forEach(key=> url.searchParams.append(key,queryParams[key]))

  const resp = await fetch(url.toString(),{
       method:"POST",
       body: form,
  });
  return resp.json();
}

export async function searchFaceImage(file) {
  const form = new FormData();
  form.append('file',file);
  const resp = await fetch(`${API_URL}/search`,{
    method:"POST",
    body: form,
  });
  console.log(resp);
  return resp
}

export async function live_search_image(blob) {
  const form = new FormData();
  form.append("file",blob,"frame.jpg");
  const response = await fetch(`${API_URL}/live-search`,{
    method: "POST",
    "body": form
  });
  return await response.json();
}